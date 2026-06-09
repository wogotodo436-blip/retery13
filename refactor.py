import re

with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update renderPanelLock
old_lock = '''  const renderPanelLock = (panelId: string) => {
    const isLocked = isPanelLocked(panelId);
    return (
      <button
        onClick={(e) => {
          e.stopPropagation();
          togglePanelLock(panelId);
        }}
        onPointerDownCapture={(e) => e.stopPropagation()}
        className={`w-fit p-0.5 rounded transition-colors flex-shrink-0 relative z-[999] pointer-events-auto ${panelId === "catalog" ? "absolute bottom-[4px] left-[-32px] z-[999]" : "self-start"} ${isLocked ? "text-slate-600 hover:text-amber-400" : "text-amber-400 hover:text-slate-500"}`}
        title={isLocked ? "Разблокировать панель" : "Заблокировать панель"}
      >
        {isLocked ? (
          <Lock className="w-4 h-4" />
        ) : (
          <Unlock className="w-4 h-4 text-amber-300" />
        )}
      </button>
    );
  };'''

new_lock = '''  const renderPanelLock = (panelId: string) => {
    const isLocked = isPanelLocked(panelId);

    let positionClass = "top-4 left-[-28px] rounded-l-lg border-y border-l";
    if (panelId === 'catalog') {
      positionClass = "top-4 right-[-28px] rounded-r-lg border-y border-r";
    } else if (panelId === 'tophud') {
      positionClass = "bottom-[-28px] left-4 rounded-b-lg border-x border-b";
    }

    return (
      <button
        onClick={(e) => {
          e.stopPropagation();
          togglePanelLock(panelId);
        }}
        onPointerDownCapture={(e) => e.stopPropagation()}
        className={`absolute ${positionClass} w-7 h-7 flex items-center justify-center transition-all z-[999] pointer-events-auto ${isLocked ? "bg-[#070716]/95 border-white/10 text-slate-500 hover:text-amber-400" : "bg-emerald-950/95 border-emerald-500/50 text-emerald-400 shadow-[0_0_15px_rgba(16,185,129,0.3)]"}`}
        title={isLocked ? "Разблокировать панель" : "Заблокировать панель"}
      >
        {isLocked ? (
          <Lock className="w-3.5 h-3.5" />
        ) : (
          <Unlock className="w-3.5 h-3.5 text-amber-300" />
        )}
      </button>
    );
  };'''

content = content.replace(old_lock, new_lock)

# 2. Update panel structures
panels = [
    ("tophud", 'absolute top-[-42px] left-[-2px] z-50 pointer-events-auto'),
    ("decryptor", 'absolute top-[-20px] right-[-35px] z-30 pointer-events-auto'),
    ("parametris_efir", 'absolute bottom-4 right-4 z-30 pointer-events-auto'),
    ("map", 'absolute top-[120px] right-4 z-30 pointer-events-auto'),
    ("size", 'absolute top-[120px] right-4 z-30 pointer-events-auto'),
    ("spheresize", 'absolute top-[120px] right-4 z-30 pointer-events-auto'),
    ("perf", 'absolute top-[120px] right-4 z-30 pointer-events-auto'),
    ("navigator", 'absolute bottom-[-45px] right-[-35px] z-20 pointer-events-auto'),
]

for panel_id, abs_cls in panels:
    pattern = r'(<motion\.div[^>]*?\{\.\.\.getDragProps\("' + panel_id + r'"\)\}\s*className=\{`)([^`]+)(`\}\s*>\s*\{renderPanelLock\("' + panel_id + r'"\)\})'

    def repl(m):
        orig_classes = m.group(2)
        inner_cls = orig_classes
        for token in ['absolute', 'top-[-42px]', 'left-[-2px]', 'top-[-20px]', 'right-[-35px]', 'bottom-4', 'right-4', 'top-[120px]', 'bottom-[-45px]', 'z-50', 'z-30', 'z-20', 'pointer-events-auto']:
            inner_cls = inner_cls.replace(token, '')
        inner_cls = " ".join(inner_cls.split())

        inner_cls = re.sub(r'\$\{isPanelsUnlocked \? "[^"]+" : ""\}', f'${{!isPanelLocked("{panel_id}") ? "ring-2 ring-emerald-500/50" : "border-white/5"}}', inner_cls)
        # also remove border-white/5 from default to avoid double borders if we replaced it
        if "border-white/5" in inner_cls and "border-white/5" in f'${{!isPanelLocked("{panel_id}")':
           inner_cls = inner_cls.replace("border-white/5", "", 1)

        return f'{m.group(1)}{abs_cls}{m.group(3)}\n            <div className={{`{inner_cls} w-full h-full`}}>'

    content = re.sub(pattern, repl, content)

# 3. For catalog panel specifically
cat_pattern = r'(<motion\.div[^>]*?whileDrag=\{\{ transition: \{ duration: 0 \} \}\}\s*className=\{`)([^`]+)(`\}\s*>)'
def repl_cat(m):
    inner_cls = m.group(2)
    for token in ['absolute', 'bottom-[6px]', 'left-0', 'z-40', 'pointer-events-auto']:
        inner_cls = inner_cls.replace(token, '')
    inner_cls = " ".join(inner_cls.split())
    inner_cls = re.sub(r'\$\{isPanelsUnlocked \|\| isCatalogMovable \? "[^"]+" : ""\}', f'${{!isPanelLocked("catalog") ? "ring-2 ring-emerald-500/50" : "border-white/20"}}', inner_cls)

    abs_cls = 'absolute bottom-[6px] left-0 z-40 pointer-events-auto'

    # We must insert the renderPanelLock("catalog") OUTSIDE the inner div, so it stays attached to motion.div
    # Notice that for catalog, the renderPanelLock was actually BEFORE the motion.div!
    # Let's check original: it was `<> {renderPanelLock("catalog")} <motion.div...>`
    # We will remove it from outside and put it inside the motion.div, before the inner wrapper
    return f'{m.group(1)}{abs_cls}{m.group(3)}\n            {{renderPanelLock("catalog")}}\n            <div className={{`{inner_cls} w-full h-full`}}>'

content = re.sub(cat_pattern, repl_cat, content)

# Remove the old external catalog lock
content = content.replace('{renderPanelLock("catalog")}\n              <motion.div', '<motion.div')

# 4. Insert closing </div> tags
content = re.sub(r'(\s*)</motion\.div>(\s*)\}\s*</AnimatePresence>', r'\1  </div>\1</motion.div>\2}\n      </AnimatePresence>', content)
content = re.sub(r'(\s*)</motion\.div>(\s*)</>\s*\}\s*</AnimatePresence>', r'\1  </div>\1</motion.div>\2</>\n        }\n      </AnimatePresence>', content)

# For tophud, it doesn't have an AnimatePresence wrapper.
# tophud ends before "      {/* DETAILED ETHER ADJUSTMENT PANEL */}"
tophud_end = r'(              <LayoutGrid className="w-4 h-4" />\n            </button>\n          </motion\.div>)'
content = re.sub(tophud_end, r'              <LayoutGrid className="w-4 h-4" />\n            </button>\n            </div>\n          </motion.div>', content)

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
