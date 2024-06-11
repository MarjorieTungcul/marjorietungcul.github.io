@echo off

:convert
set /p input="Enter time (24-hour format, e.g. 00:00): "

set /a hours=1%input:~0,2%-100
set /a minutes=1%input:~3,2%-100

if %hours% lss 12 (
    set am_pm=AM
    if %hours% equ 0 (
        set hours=12
    )
) else (
    set am_pm=PM
    if %hours% gtr 12 (
        set /a hours-=12
    )
)

if %hours% lss 10 set hours=0%hours%
if %minutes% lss 10 set minutes=0%minutes%

echo Converted time: %hours%:%minutes% %am_pm%

choice /c yn /m "Do you want to try again?"
    if errorlevel 2 goto end
    if errorlevel 1 goto convert

:end
echo Goodbye