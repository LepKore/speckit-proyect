[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string] $Script,

    [Parameter(Position = 1, ValueFromRemainingArguments = $true)]
    [string[]] $Arguments
)

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
$scriptPath = Join-Path $repoRoot ".specify\scripts\bash\$Script"

if (-not (Test-Path -LiteralPath $scriptPath -PathType Leaf)) {
    throw "No se encontró el script Spec Kit: $scriptPath"
}

$bashCandidates = @(
    (Join-Path ${env:ProgramFiles} 'Git\bin\bash.exe'),
    (Join-Path ${env:ProgramFiles} 'Git\usr\bin\bash.exe')
)
$bashPath = $bashCandidates | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
if (-not $bashPath) {
    throw 'No se encontró Bash de Git for Windows. Instale Git for Windows para ejecutar los scripts de Spec Kit.'
}

& $bashPath $scriptPath @Arguments
exit $LASTEXITCODE
