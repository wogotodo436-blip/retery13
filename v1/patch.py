import re

path = r'c:\Users\User\Downloads\project lauch\src\App.tsx'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add isPanelLocked helper + fix togglePanelLock
old1 = (
    'const togglePanelLock = (panelId: string) => {\n'
    '    setPanelLocks(prev => ({ ...prev, [panelId]: !prev[panelId] }));\n'
    '  };'
)
new1 = (
    'const togglePanelLock = (panelId: string) => {\n'
    '    setPanelLocks(prev => ({ ...prev, [panelId]: prev[panelId] !== false }));\n'
    '  };\n'
    '\n'
    '  const isPanelLocked = (panelId: string) => panelLocks[panelId] !== false;'
)
assert old1 in content, 'old1 not found'
content = content.replace(old1, new1, 1)

# 2. Fix getDragProps
old2 = 'const isDraggable = isPanelsUnlocked && !panelLocks[panelId];'
new2 = 'const isDraggable = !isPanelLocked(panelId);'
assert old2 in content, 'old2 not found'
content = content.replace(old2, new2, 1)

# 3. Remove early return from renderPanelLock so lock always visible
old3 = (
    'renderPanelLock = (panelId: string) => {\n'
    '    if (!isPanelsUnlocked) return null;\n'
    '    const isLocked = panelLocks[panelId];'
)
new3 = (
    'renderPanelLock = (panelId: string) => {\n'
    '    const isLocked = isPanelLocked(panelId);'
)
assert old3 in content, 'old3 not found'
content = content.replace(old3, new3, 1)

# 4. Fix lock button style: locked = subtle grey, unlocked = amber
old4 = (
    "className={`absolute -top-2 -right-2 p-1 rounded-full shadow-lg border z-50 "
    "${isLocked ? 'bg-indigo-900 border-indigo-500 text-indigo-300' : 'bg-amber-600 border-amber-400 text-amber-100'}`}"
)
new4 = (
    "className={`absolute -top-2 -right-2 p-1 rounded-full shadow-lg border z-50 transition-colors "
    "${isLocked ? 'bg-slate-800/90 border-slate-600 text-slate-400 hover:border-amber-500 hover:text-amber-300' : 'bg-amber-600 border-amber-400 text-amber-100'}`}"
)
assert old4 in content, 'old4 not found'
content = content.replace(old4, new4, 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('All replacements done successfully')
