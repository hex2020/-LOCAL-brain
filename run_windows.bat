@echo on
title Local Brain Debug Mode
cd /d %~dp0

echo ---------------------------------------------------
echo 🧠 STARTING IN DEBUG MODE (WINDOW WILL NOT CLOSE)
echo ---------------------------------------------------

:: 1. Check for Python
python --version
if %errorlevel% neq 0 (
    echo [ERROR] Python not found. Install Python 3.10+ and check "Add to PATH".
    cmd /k
)

:: 2. Check/Create Environment
if not exist "venv" (
    echo [INFO] Creating virtual environment...
    python -m venv venv
)

:: 3. Force Install Libraries (Visual Mode)
echo [INFO] checking libraries...
venv\Scripts\python.exe -m pip install streamlit langchain langchain-community langchain-ollama langchain-chroma chromadb pymupdf

:: 4. Run App (With error catching)
echo [INFO] Launching App...
venv\Scripts\python.exe -m streamlit run app.py

if %errorlevel% neq 0 (
    echo.
    echo [CRASH DETECTED] The app crashed with the error above.
    echo.
)

:: 5. FORCE WINDOW TO STAY OPEN
echo.
echo ===================================================
echo    DO NOT CLOSE THIS WINDOW. CHECK ERRORS ABOVE.
echo ===================================================
cmd /k