@echo off
setlocal

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing build dependencies...
pip install -r requirements.build.txt

echo Creating executable...
pyinstaller --onefile --windowed --add-data "venv\Lib\site-packages\spellchecker\resources;spellchecker\resources" src/app.py

echo Build completed! Executable is in dist\
pause