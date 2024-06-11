@echo off

:create
setlocal enabledelayedexpansion
set /p integer="Enter an integer: "

if "!integer!"=="" goto create

set "valid=true"
for /f "tokens=1 delims=0123456789" %%a in ("%integer%") do set "valid=false"
if "%valid%"=="true" (
    echo This is the Reverse Multiplication Table for %integer%:
    
    set "column=  "
    for /l %%k in (1,1,%integer%) do (
        if %%k lss 10 (
            set "column=!column! %%k "
        ) else (
            set "column=!column!%%k "
        )
    )
    echo !column!

    for /l %%i in (1,1,%integer%) do (
        set "row="
        set /a multiplier=%%i
        set "row=!row!%%i "

        for /l %%j in (1,1,%integer%) do (
            set /a product=multiplier*%%j
            if !product! lss 10 (
                set "row=!row! !product! "
            ) else (
                set "row=!row!!product! "
            )
        )
        echo !row!
    )
) else (
    echo Invalid input. Please enter a valid integer only.
)
endlocal

choice /c yn /m "Do you want to try again?"
        if errorlevel 2 goto end
        if errorlevel 1 goto create

:end
echo Goodbye

