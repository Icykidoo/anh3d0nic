@echo off
REM Anh3d0nic Launcher for Windows

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║                     Anh3d0nic AI Agent                        ║
echo ║                  Starting Local AI Brain...                   ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo Please install Python from https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

REM Check if gpt4all is installed
python -c "import gpt4all" >nul 2>&1
if errorlevel 1 (
    echo Installing gpt4all...
    echo This is a one-time setup. Please wait...
    echo.
    python -m pip install gpt4all
    echo.
    echo Installation complete!
    echo.
)

REM Launch Anh3d0nic
python anh3d0nic.py

pause
