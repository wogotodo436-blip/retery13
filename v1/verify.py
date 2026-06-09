path = r'c:\Users\User\Downloads\project lauch\src\App.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

checks = [
    ('isPanelLocked helper added', 'const isPanelLocked = (panelId: string) => panelLocks[panelId] !== false;'),
    ('togglePanelLock fixed', 'prev[panelId] !== false'),
    ('getDragProps uses isPanelLocked', 'const isDraggable = !isPanelLocked(panelId);'),
    ('renderPanelLock always shows', 'renderPanelLock = (panelId: string) => {\n    const isLocked = isPanelLocked(panelId);'),
    ('no early return', 'if (!isPanelsUnlocked) return null' not in content),
    ('lock button styled correctly', 'bg-slate-800/90 border-slate-600 text-slate-400'),
]

for name, check in checks:
    if isinstance(check, bool):
        status = 'OK' if check else 'FAIL'
    else:
        status = 'OK' if check in content else 'FAIL'
    print(f'{status}: {name}')
