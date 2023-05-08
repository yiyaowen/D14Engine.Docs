@echo off

if "%1" == "clean" (
    rmdir /S /Q build >NUL 2>NUL
) ^
else if "%1" == "html" (
    rmdir /S /Q build/html >NUL 2>NUL
    sphinx-build -b html . build/html
    sphinx-build -b html -D language=en_US . build/html/en_US
) ^
else if "%1" == "open" (
    build\html\index.html >NUL 2>NUL
) ^
else if "%1" == "trans" (
    rmdir /S /Q build/trans >NUL 2>NUL
    sphinx-build -b gettext . build/trans
    sphinx-intl update -p build/trans -l en_US
)
