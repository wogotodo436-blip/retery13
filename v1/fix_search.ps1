$file = "C:\Users\User\Downloads\project lauch\src\App.tsx"
$content = Get-Content $file -Raw

$content = $content -replace '(\{\!isSearchExpanded \? \([\s\S]*?<)motion\.div(>)', '$1div$2'
$content = $content -replace '(\s+<button[\s\S]*?Свернуть поиск[\s\S]*?<)motion\.div(>)', '$1div$2'

Set-Content $file $content
