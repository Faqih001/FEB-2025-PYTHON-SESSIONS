import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import numpy as np

# Task 1: Load and Explore the Dataset
def load_and_explore_data():
    try:
        # Load Iris dataset
        iris = load_iris()
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
        
        # Display first few rows
        print("First 5 rows of the dataset:")
        print(df.head())
        print("\nDataset Info:")
        print(df.info())
        
        # Check for missing values
        print("\nMissing Values:")
        print(df.isnull().sum())
        
        # Since Iris dataset is clean, no need to handle missing values
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Task 2: Basic Data Analysis
def analyze_data(df):
    try:
        # Basic statistics
        print("\nBasic Statistics:")
        print(df.describe())
        
        # Group by species and compute mean with observed=False
        print("\nMean measurements by species:")
        print(df.groupby('species', observed=False).mean())
        
        # Additional insights
        print("\nKey Observations:")
        print("- Setosa has the smallest petal length and width on average.")
        print("- Virginica has the largest sepal and petal measurements.")
        print("- Versicolor falls between Setosa and Virginica in most measurements.")
    except Exception as e:
        print(f"Error analyzing data: {e}")

# Task 3: Data Visualization
def create_visualizations(df):
    try:
        # Set seaborn style
        sns.set_style("whitegrid")
        
        # 1. Line chart: Mean measurements per species
        plt.figure(figsize=(10, 6))
        species_means = df.groupby('species', observed=False).mean()
        for column in species_means.columns:
            plt.plot(species_means.index, species_means[column], marker='o', label=column)
        plt.title('Mean Measurements by Iris Species')
        plt.xlabel('Species')
        plt.ylabel('Measurement (cm)')
        plt.legend()
        plt.savefig('iris_line_chart.png')
        plt.close()
        
        # 2. Bar chart: Average petal length per species
        plt.figure(figsize=(8, 6))
        sns.barplot(x='species', y='petal length (cm)', data=df)
        plt.title('Average Petal Length by Species')
        plt.xlabel('Species')
        plt.ylabel('Petal Length (cm)')
        plt.savefig('iris_bar_chart.png')
        plt.close()
        
        # 3. Histogram: Distribution of sepal length
        plt.figure(figsize=(8, 6))
        sns.histplot(data=df, x='sepal length (cm)', bins=20, kde=True)
        plt.title('Distribution of Sepal Length')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Count')
        plt.savefig('iris_histogram.png')
        plt.close()
        
        # 4. Scatter plot: Sepal length vs Petal length
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', 
                       hue='species', size='species', sizes=(50, 200))
        plt.title('Sepal Length vs Petal Length')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Petal Length (cm)')
        plt.legend(title='Species')
        plt.savefig('iris_scatter_plot.png')
        plt.close()
        
        print("\nVisualizations saved as PNG files.")
    except Exception as e:
        print(f"Error creating visualizations: {e}")

# Main execution
if __name__ == "__main__":
    df = load_and_explore_data()
    if df is not None:
        analyze_data(df)
        create_visualizations(df)