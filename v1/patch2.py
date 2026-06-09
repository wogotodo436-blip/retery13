path = r'c:\Users\User\Downloads\project lauch\src\App.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# locked = true means locked, undefined/false means unlocked
# We need the opposite: default = unlocked
# panelLocks[panelId] === true means locked, anything else = unlocked

old1 = 'const isPanelLocked = (panelId: string) => panelLocks[panelId] !== false;'
new1 = 'const isPanelLocked = (panelId: string) => panelLocks[panelId] === true;'
assert old1 in content, 'old1 not found'
content = content.replace(old1, new1, 1)

old2 = 'setPanelLocks(prev => ({ ...prev, [panelId]: prev[panelId] !== false }));'
new2 = 'setPanelLocks(prev => ({ ...prev, [panelId]: prev[panelId] !== true }));'
assert old2 in content, 'old2 not found'
content = content.replace(old2, new2, 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
