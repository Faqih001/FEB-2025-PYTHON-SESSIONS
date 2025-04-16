# Iris Analysis Project

This project performs data analysis and visualization on the Iris dataset using Python, Pandas, Matplotlib, and Seaborn. It includes loading and exploring the dataset, computing basic statistics, and creating four types of visualizations to uncover patterns in the data.

## Project Structure

- `assignment.py`: Main Python script that performs data loading, analysis, and visualization.
- `setup_venv.sh`: Bash script to set up a virtual environment and install dependencies (for Unix/macOS).
- `setup_venv.bat`: Batch script to set up a virtual environment and install dependencies (for Windows).
- `README.md`: This file, providing project documentation.

## Requirements

- Python 3.6 or higher
- Visual Studio Code (recommended) or any Python-compatible IDE
- Internet connection (for installing dependencies)

## Setup Instructions

### 1. Clone or Download the Project

Download the project files or clone the repository to your local machine.

### 2. Create and Activate Virtual Environment

#### Unix/macOS

1. Open a terminal in the project directory.
2. Make the setup script executable:
   ```bash
   chmod +x setup_venv.sh
   ```
3. Run the setup script to create a virtual environment and install dependencies:
   ```bash
   ./setup_venv.sh
   ```
4. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

#### Windows

1. Open a Command Prompt or PowerShell in the project directory.
2. Run the setup script to create a virtual environment and install dependencies:
   ```bat
   setup_venv.bat
   ```
3. Activate the virtual environment:
   ```bat
   venv\Scripts\activate
   ```

The virtual environment (`venv`) will be created, and the following dependencies will be installed:

- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `numpy`

### 3. Configure VS Code

1. Open the project folder in VS Code.
2. Open `assignment.py`.
3. Press `Ctrl+Shift+P`, search for `Python: Select Interpreter`, and choose the interpreter from the `venv` folder (e.g., `./venv/bin/python` or `.\venv\Scripts\python.exe`).

## Usage

1. Ensure the virtual environment is activated (see step 2 in Setup Instructions).
2. Run the script:
   ```bash
   python assignment.py
    ```
   Alternatively, in VS Code, click the "Run" button or press `F5` with `assignment.py` open.
3. The script will:
   - Load the Iris dataset using `scikit-learn`.
   - Display the first few rows, dataset info, and check for missing values.
   - Compute basic statistics and group means by species.
   - Generate four visualizations saved as PNG files in the project directory:
     - `iris_line_chart.png`: Line chart of mean measurements by species.
     - `iris_bar_chart.png`: Bar chart of average petal length by species.
     - `iris_histogram.png`: Histogram of sepal length distribution.
     - `iris_scatter_plot.png`: Scatter plot of sepal length vs. petal length.
4. Check the terminal for printed outputs and the project directory for the generated PNG files.

## Output

- **Console Output**: Dataset head, info, missing values, statistics, group means, and key observations.
- **Visualizations**: Four PNG files saved in the project directory, as described above.

## Notes

- The Iris dataset is clean, so no missing value handling is required.
- Visualizations are saved as PNG files to ensure compatibility across environments. To display plots interactively, add `plt.show()` after each `plt.savefig()` in `create_visualizations` (requires a graphical backend).
- If dependency installation fails, ensure internet access and try running `pip install pandas matplotlib seaborn scikit-learn numpy` manually in the activated virtual environment.
- For non-VS Code environments, ensure the Python interpreter is set to the virtual environment's interpreter.

## Troubleshooting

- **Permission Issues (Unix/macOS)**: Ensure `setup_venv.sh` is executable (`chmod +x setup_venv.sh`).
- **Interpreter Not Found in VS Code**: Verify the virtual environment was created and select the correct interpreter path.
- **Module Not Found Errors**: Confirm the virtual environment is activated and dependencies are installed.

## License

This project is for educational purposes and uses the Iris dataset, which is publicly available via `scikit-learn`.