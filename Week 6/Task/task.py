# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Task 1: Create a NumPy array of numbers from 1 to 10 and calculate the mean
numbers = np.array(range(1, 11))
mean_value = np.mean(numbers)
print(f"Mean of numbers from 1 to 10: {mean_value}")

# Task 2: Load a small dataset into a pandas DataFrame and display summary statistics
# Example dataset: List of people's names and ages
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 30, 35, 40, 22]
}
df = pd.DataFrame(data)
print("\nSummary statistics of the dataset:")
print(df.describe())

# Task 3: Fetch data from a public API using requests and print a key piece of information
# Let's fetch a random joke using the 'https://official-joke-api.appspot.com/random_joke' API
response = requests.get('https://official-joke-api.appspot.com/random_joke')
joke_data = response.json()
print(f"\nHere's a random joke: {joke_data['setup']} - {joke_data['punchline']}")

# Task 4: Plot a simple line graph using matplotlib
# Example data: Numbers and their squares
x = np.array(range(1, 11))
y = x**2

# Plotting the line graph
plt.plot(x, y, label='x squared', color='b')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Graph: y = x^2')
plt.legend()
plt.show()
