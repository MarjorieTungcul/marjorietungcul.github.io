@echo off

:menu
echo Please select one among the three shapes:
echo 1. Circle
echo 2. Triangle
echo 3. Quadrilateral
echo 4. Exit

choice /c 1234 /m "Please enter the number of your chosen shape:"
echo ============================================================
if errorlevel 4 goto end
if errorlevel 3 goto Quadrilateral
if errorlevel 2 goto Triangle
if errorlevel 1 goto Circle

:Circle
setlocal enabledelayedexpansion
set /p radius=Please enter the radius of the circle: 
if "!radius!"=="" goto Circle

for /f %%a in ('powershell -command "$radius = !radius!; [math]::Pi * $radius * $radius"') do set "circle_area=%%a"

echo The Area of the circle is: !circle_area!
echo ============================================================
endlocal
pause
goto menu

:Triangle
set /p side_1=Please enter the length of side 1 of the triangle: 
if "%side_1%"=="" goto Triangle 
set /p side_2=Please enter the length of side 2 of the triangle: 
if "%side_2%"=="" goto Triangle
set /p side_3=Please enter the length of side 3 of the triangle: 
if "%side_3%"=="" goto Triangle 

for /f %%b in ('powershell -command "(%side_1% + %side_2% + %side_3%) / 2"') do set "s=%%b"
for /f %%c in ('powershell -command "$s = %s%; $side_1 = %side_1%; $side_2 = %side_2%; $side_3 = %side_3%; $area = [math]::Sqrt($s*($s-$side_1)*($s-$side_2)*($s-$side_3)); $area"') do set "triangle_area=%%c"

echo The area of the triangle is: %triangle_area%

if %side_1%==%side_2% (
    if %side_1%==%side_3% (
        echo The triangle is equilateral.
    ) else (
        echo The triangle is isosceles.
    )
) else (
    if %side_1%==%side_3% (
        echo The triangle is isosceles.
    ) else if %side_2%==%side_3% (
        echo The triangle is isosceles.
    ) else (
        echo The triangle is scalene.
    )
)
echo ============================================================
pause
goto menu

:Quadrilateral
setlocal enabledelayedexpansion
set /p length=Please enter the length of the quadrilateral: 
if "%length%"=="" goto Quadrilateral 
set /p width=Please enter the width of the quadrilateral: 
if "%width%"=="" goto Quadrilateral
set /a quadrilateral_area= %length% * %width%

echo The area of the quadrilateral is: %quadrilateral_area%

if %length%==%width% (
    echo The quadrilateral is a square.
) else (
    echo The quadrilateral is a rectangle.
)
echo ============================================================
endlocal
goto menu

:end
echo Goodbye
