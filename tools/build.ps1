param(
    [switch]$commit,
    [switch]$push,
    [switch]$release,
    [string]$version,
    [switch]$bump,
    [switch]$publish,
    [switch]$pre
)

# Configuration
$repoRoot = Split-Path -Parent $PSScriptRoot
$pyprojectPath = Join-Path $repoRoot "pyproject.toml"

# Function to get current version from pyproject.toml
function Get-CurrentVersion {
    if (Test-Path $pyprojectPath) {
        $content = Get-Content $pyprojectPath
        foreach ($line in $content) {
            if ($line -match '^version\s*=\s*"([^"]+)"') {
                return $matches[1]
            }
        }
    }
    return "0.0.0"
}

# Function to bump version
function Bump-Version {
    param([string]$currentVersion)
    if ($currentVersion -match '^(\d+)\.(\d+)\.(\d+)$') {
        $major = [int]$matches[1]
        $minor = [int]$matches[2]
        $patch = [int]$matches[3] + 1
        return "$major.$minor.$patch"
    }
    return $currentVersion
}

# Function to update version in pyproject.toml
function Update-Version {
    param([string]$newVersion)
    $pyprojectPath = "..\pyproject.toml"
    if (Test-Path $pyprojectPath) {
        $content = Get-Content $pyprojectPath
        $newContent = $content | ForEach-Object {
            if ($_ -match '^version\s*=\s*"[^"]+"') {
                $_ -replace 'version\s*=\s*"[^"]+"', "version = `"$newVersion`""
            } else { $_ }
        }
        $newContent | Set-Content $pyprojectPath
        Write-Host "Updated SDK version to $newVersion in $pyprojectPath"
    }
}

$doAll = -not ($commit -or $push -or $release -or $version -or $bump -or $publish -or $pre)
$currentVersion = Get-CurrentVersion
$targetVersion = $currentVersion

if ($bump -or $doAll) { $targetVersion = Bump-Version -currentVersion $currentVersion }
if ($version) { $targetVersion = $version }

if ($bump -or $version -or $doAll) { Update-Version -newVersion $targetVersion }

if ($commit -or $doAll) {
    Write-Host "Committing SDK changes..."
    Push-Location $repoRoot
    try {
        git add .
        $changes = git status --porcelain
        if ($changes) {
            git commit -m "v${targetVersion}: Release SDK"
            if ($release -or $doAll) { git tag "v${targetVersion}" -f }
        }
    } finally { Pop-Location }
}

if ($push -or $doAll) {
    Write-Host "Pushing SDK to GitHub..."
    Push-Location $repoRoot
    try {
        git push origin main
        if ($release -or $doAll) { git push origin "v${targetVersion}" -f }
    } finally { Pop-Location }
}

if ($publish -or $doAll) {
    Write-Host "Publishing SDK to PyPI..."
    $env:PYPI_TOKEN = [System.Environment]::GetEnvironmentVariable("PYPI_TOKEN", "User")
    Push-Location $repoRoot
    try {
        Remove-Item -Path "dist" -Recurse -ErrorAction SilentlyContinue
        python -m build
        python -m twine upload -u "__token__" -p "$env:PYPI_TOKEN" dist/* --non-interactive --skip-existing
    } finally { Pop-Location }
}

Write-Host "SDK Build completed. Version: $targetVersion"
