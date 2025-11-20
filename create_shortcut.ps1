param(
    [string]$TargetPath = "\\wsl.localhost\Ubuntu-20.04\home\na-hara\TIMER\dist\StopWatch.exe",
    [string]$ShortcutName = "StopWatch.lnk"
)

$startup = [Environment]::GetFolderPath('Startup')
$w = New-Object -ComObject WScript.Shell
$sc = $w.CreateShortcut((Join-Path $startup $ShortcutName))
$sc.TargetPath = $TargetPath
$sc.WorkingDirectory = Split-Path $TargetPath
$sc.Save()
Write-Host "Shortcut created in: $startup"
