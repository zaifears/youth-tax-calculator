# Antigravity Skill Installer for Windows
# Skill: youth-tax-calculator
Write-Host "Installing youth-tax-calculator skill to Antigravity global config..." -ForegroundColor Cyan

$targetDir = Join-Path $HOME ".gemini\config\skills\youth-tax-calculator"
if (-not (Test-Path $targetDir)) {
    New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
}

$sourceDir = Join-Path $PSScriptRoot "skills\youth-tax-calculator"
if (Test-Path $sourceDir) {
    Copy-Item -Path "$sourceDir\*" -Destination $targetDir -Recurse -Force
} else {
    $fallbackFile = Join-Path $PSScriptRoot "bd-income-tax-filing.SKILL.md"
    Copy-Item -Path $fallbackFile -Destination (Join-Path $targetDir "SKILL.md") -Force
}

# Clean up any obsolete previous names
$oldDir1 = Join-Path $HOME ".gemini\config\skills\bd-youth-tax-expert"
if (Test-Path $oldDir1) { Remove-Item -Path $oldDir1 -Recurse -Force }
$oldDir2 = Join-Path $HOME ".gemini\config\skills\bd-tax-filing-expert"
if (Test-Path $oldDir2) { Remove-Item -Path $oldDir2 -Recurse -Force }

Write-Host "Success! youth-tax-calculator has been installed globally." -ForegroundColor Green
Write-Host "Target Location: $targetDir" -ForegroundColor Yellow
Write-Host "You can now ask Antigravity about Bangladesh student, intern, and employee tax filing in any project." -ForegroundColor Cyan
