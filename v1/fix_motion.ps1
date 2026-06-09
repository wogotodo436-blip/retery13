$file = "C:\Users\User\Downloads\project lauch\src\App.tsx"
$lines = Get-Content $file

$stack = @()
$newLines = @()

for ($i = 0; $i -lt $lines.Count; $i++) {
    $line = $lines[$i]

    if ($line -match '^(\s*)<motion\.div') {
        $indent = $matches[1].Length
        $stack += @{lineNum = $i; indent = $indent}
    }
    elseif ($line -match '^(\s*)</div>') {
        $indent = $matches[1].Length
        while ($stack.Count -gt 0 -and $stack[-1].indent -ge $indent) {
            $stack = $stack[0..($stack.Count - 2)]
        }
        if ($stack.Count -gt 0 -and $stack[-1].indent -eq $indent) {
            $newLines += $line -replace '</div>', '</motion.div>'
            $stack = $stack[0..($stack.Count - 2)]
            continue
        }
    }

    $newLines += $line
}

Set-Content $file $newLines
