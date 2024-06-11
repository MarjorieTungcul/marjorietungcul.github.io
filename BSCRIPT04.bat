@echo off
setlocal enabledelayedexpansion

rem These are the dummy text files
if not exist C:\"My Text Files" mkdir C:\"My Text Files"
cd C:\My Text Files
echo hello > hello.txt
echo Good Day > good.txt
echo CC22 > cc22.txt
echo CITCS > citcs.txt
echo Marjorie > marj.txt

rem This sorts the text files on Drive C: by date.
echo Sorting text files by date...
echo ====================================================
cd C:\My Text Files
dir /a-d /o:d *.txt
echo ====================================================
pause

rem This archives the older files to a folder on Drive Z:
echo Archiving older files to Z:\Archive...
echo ====================================================
if not exist Z:\Archive mkdir Z:\Archive
for %%i in (*.txt) do (
    move "%%i" Z:\Archive
)
echo ====================================================
pause

rem This sorts the archived files by size.
echo Sorting archived files by size...
echo ====================================================
cd /d Z:\Archive
dir /o:s *.txt
echo ====================================================
pause

rem This prompts the user for permission to delete old, large files.
choice /c yn /m "Do you want to delete old and large files?"
echo ====================================================
if errorlevel 2 (
    echo Deletion canceled. No old and large files were removed.
) else (
     for %%i in (*.txt) do (
        del "%%i"
    )
    echo The old and large files have been deleted.
)
echo ====================================================
pause

rem This deletes the created folders
rd C:\"My Text Files"
echo My Text Files folder has been deleted.
cd Z:\
rd Z:\Archive
if not exist Z:\Archive (
    echo Archive Folder has been deleted.
) else (
    echo Please remove first the files inside the Archive Folder.
)

pause
echo ====================================================
echo Goodbye

