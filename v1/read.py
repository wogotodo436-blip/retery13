path = r'c:\Users\User\Downloads\project lauch\src\App.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
idx = content.find('renderPanelLock = (panelId')
snippet = content[idx:idx+600]
with open(r'c:\Users\User\Downloads\project lauch\out.txt', 'w', encoding='utf-8') as f:
    f.write(snippet)
print('written')
