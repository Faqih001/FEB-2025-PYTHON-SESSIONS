@echo off
REM setup_venv.bat (Windows)

REM This script sets up a Python virtual environment and installs the required dependencies
REM for the assignment. It assumes Python is already installed and available in the PATH.
:: Create virtual environment
python -m venv venv

:: Activate virtual environment
call venv\Scripts\activate

:: Upgrade pip
pip install --upgrade pip

:: Install dependencies
pip install pandas matplotlib seaborn scikit-learn numpy

:: Notify user
echo Virtual environment created and dependencies installed.
echo To activate the virtual environment, run: venv\Scripts\activate
echo To run the script, run: python assignment.py