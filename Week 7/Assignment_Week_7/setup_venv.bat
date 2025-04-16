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

:: Deactivate virtual environment
deactivate
:: Notify user
echo Virtual environment deactivated.
echo To reactivate, run: venv\Scripts\activate
:: End of script
:: Note: This script is intended for Windows. For Unix-based systems, use setup_venv.sh
:: Usage:
:: 1. Save this script as setup_venv.bat
:: 2. Open Command Prompt
:: 3. Navigate to the directory where the script is saved
:: 4. Run the script by typing: setup_venv.bat
:: 5. Follow the instructions provided in the script output
:: 6. To run the assignment script, ensure the virtual environment is activated
:: 7. To deactivate the virtual environment, simply type: deactivate
:: 8. To reactivate the virtual environment, run: venv\Scripts\activate
:: 9. To remove the virtual environment, delete the 'venv' directory
:: 10. To remove the script, delete this file
:: 11. To remove the dependencies, delete the 'venv' directory and the 'requirements.txt' file
:: 12. To remove the script, delete this file
:: 13. To remove the virtual environment, delete the 'venv' directory