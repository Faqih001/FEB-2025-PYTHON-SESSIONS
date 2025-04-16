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