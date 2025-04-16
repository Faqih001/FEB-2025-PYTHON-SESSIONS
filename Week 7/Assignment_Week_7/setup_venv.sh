#!/bin/bash

# setup_venv.sh (Unix/macOS)
# This script sets up a Python virtual environment and installs the required dependencies for the assignment.
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install pandas matplotlib seaborn scikit-learn numpy

# Notify user
echo "Virtual environment created and dependencies installed."
echo "To activate the virtual environment, run: source venv/bin/activate"
echo "To run the script, run: python assignment.py"

# To deactivate the virtual environment, run: deactivate
# To remove the virtual environment, run: rm -rf venv
# Note: Make sure to run this script in the directory where you want to create the virtual environment.
# Usage:
# chmod +x setup_venv.sh
# ./setup_venv.sh
# This script is intended for Unix/macOS systems. For Windows, use the setup_venv.bat script.
# Note: This script assumes that Python 3 and pip are already installed on your system.
# If you encounter any issues, please refer to the Python documentation for troubleshooting.
# For more information on virtual environments, refer to the Python documentation: