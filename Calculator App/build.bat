@echo off
echo ====================================
echo Murakkab Kalkulyator - EXE Yaratish
echo ====================================
echo.

echo [1/4] PyInstaller o'rnatilmoqda...
pip install pyinstaller

echo.
echo [2/4] Eski build fayllarini tozalash...
if exist "build" rmdir /s /q build
if exist "dist" rmdir /s /q dist
if exist "*.spec" del /q *.spec

echo.
echo [3/4] EXE fayl yaratilmoqda...
pyinstaller --name="Murakkab_Kalkulyator" ^
    --onefile ^
    --windowed ^
    --icon=NONE ^
    --add-data "templates;templates" ^
    --add-data "static;static" ^
    --hidden-import=flask ^
    --hidden-import=werkzeug ^
    app.py

echo.
echo [4/4] Tayyor!
echo.
echo ====================================
echo EXE fayl manzili: dist\Murakkab_Kalkulyator.exe
echo ====================================
echo.
pause
