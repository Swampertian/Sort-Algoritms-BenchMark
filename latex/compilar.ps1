$ErrorActionPreference = 'Stop'
Push-Location $PSScriptRoot
try {
    $compilerPath = Join-Path $PSScriptRoot '..\.tools\tectonic\tectonic.exe'
    if (Test-Path -LiteralPath $compilerPath) {
        & $compilerPath --keep-logs relatorio.tex
        if ($LASTEXITCODE -ne 0) { throw 'Falha na compilação com Tectonic.' }
    } elseif (Get-Command pdflatex -ErrorAction SilentlyContinue) {
        1..2 | ForEach-Object {
            pdflatex -interaction=nonstopmode -halt-on-error relatorio.tex
            if ($LASTEXITCODE -ne 0) { throw 'Falha na compilação com pdfLaTeX.' }
        }
    } else {
        throw 'Instale Tectonic ou pdfLaTeX, ou compile a pasta latex no Overleaf.'
    }
    Write-Output (Join-Path $PSScriptRoot 'relatorio.pdf')
} finally {
    Pop-Location
}
