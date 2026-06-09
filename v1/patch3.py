path = r'c:\Users\User\Downloads\project lauch\src\App.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the full button block and replace with a tiny inline icon
old = (
    'renderPanelLock = (panelId: string) => {\n'
    '    const isLocked = isPanelLocked(panelId);\n'
    '    return (\n'
    '      <button \n'
    '        onClick={(e) => { e.stopPropagation(); togglePanelLock(panelId); }}\n'
    '        className={`absolute -top-2 -right-2 p-1 rounded-full shadow-lg border z-50 transition-colors ${isLocked ? \'bg-slate-800/90 border-slate-600 text-slate-400 hover:border-amber-500 hover:text-amber-300\' : \'bg-amber-600 border-amber-400 text-amber-100\'}`}'
)

assert old in content, 'block not found'

new = (
    'renderPanelLock = (panelId: string) => {\n'
    '    const isLocked = isPanelLocked(panelId);\n'
    '    return (\n'
    '      <button \n'
    '        onClick={(e) => { e.stopPropagation(); togglePanelLock(panelId); }}\n'
    '        className={`p-0.5 rounded transition-colors flex-shrink-0 ${isLocked ? \'text-slate-600 hover:text-amber-400\' : \'text-amber-400 hover:text-slate-500\'}`}'
)

content = content.replace(old, new, 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
