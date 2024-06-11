@echo off

:menu
echo ===================================================================
echo Please select one among the 7 fundamental Windows utilities:
echo 1. ipconfig
echo 2. tasklist / taskkill
echo 3. chkdsk
echo 4. format
echo 5. defrag
echo 6. find
echo 7. attrib
echo 8. exit
echo ===================================================================
choice /c 12345678 /m "Please enter the number of your chosen utility: "
echo ===================================================================

if errorlevel 8 goto end
if errorlevel 7 goto attrib
if errorlevel 6 goto find
if errorlevel 5 goto defrag
if errorlevel 4 goto format
if errorlevel 3 goto chkdsk
if errorlevel 2 goto tasklist
if errorlevel 1 goto ipconfig

:ipconfig
ipconfig
pause
goto menu

:tasklist
tasklist
choice /c yn /m "Do you want to kill a task?"
if errorlevel 2 (
    echo Skipping taskkill.
) else (
    setlocal enabledelayedexpansion
    set /p PID=Enter the PID of the process you want to kill:
    if "!PID!"=="" (
        echo No PID entered. Returning to menu
    ) else (
        taskkill /PID !PID! /f
    )
    endlocal    
)
pause
goto menu

:chkdsk
setlocal enabledelayedexpansion
set /p check_drive=Enter the letter of the drive you want to check (For example, enter C for C drive): 
if "!check_drive!"=="" (
    echo No drive letter entered. Returning to menu.
    pause
    goto menu
) else if not exist !check_drive!:\ (
    echo The drive you have specified does not exist.
    pause 
    goto menu
) else (
    chkdsk !check_drive!:
)
endlocal
pause
goto menu

:format
setlocal enabledelayedexpansion
set /p format_drive=Enter the letter of the drive you want to format (For example, enter C for C drive):
if "!format_drive!"=="" (
    echo No drive letter entered. Returning to menu.
    pause
    goto menu
) else if not exist !format_drive!:\ (
    echo The drive you have specified does not exist.
    pause
    goto menu
) else (
    choice /c yn /m "Are you sure you want to format !format_drive!?:"
    if errorlevel 2 (
        echo Formatting cancelled.
    ) else (
        format !format_drive!:
    )
)
endlocal
pause
goto menu

:defrag
setlocal enabledelayedexpansion
set /p defrag_drive=Enter the letter of the drive you want to defrag (For example, enter C for C drive): 
if "!defrag_drive!"=="" (
    echo No drive letter entered. Returning to menu.
    pause
    goto menu
) else if not exist !defrag_drive!: (
    echo The specified drive does not exist.
    pause
    goto menu
) else (
    defrag !defrag_drive!: /U
)
endlocal
pause
goto menu

:find
setlocal enabledelayedexpansion
set /p text=Enter the text you want to find : 
if "!text!"=="" (
    echo No text entered. Returning to menu.
    pause
    goto menu
)
set /p file=Enter the file to search in (For example, hi.txt):
if "!file!"=="" (
    echo No file entered. Returning to menu.
    pause
    goto menu
) else if not exist "!file!" (
    echo File does not exist.
) else (
    find "!text!" "!file!"
)
endlocal
pause
goto menu

:attrib
setlocal enabledelayedexpansion
set /p file=Enter the file you want to change attributes: 
if "!file!"=="" (
    echo No file entered. Returning to menu.
    pause
    goto menu
) else if not exist "!file!" (
    echo File does not exist.
    pause
    goto menu
)
set /p attributes=Enter the attributes you want to set (For example, enter +r to add the read-only attribute): 
attrib %attributes% %file%
endlocal
pause
goto menu

:end
echo Goodbye
