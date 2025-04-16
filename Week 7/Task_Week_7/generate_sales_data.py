import pandas as pd
import random
from datetime import datetime, timedelta

# Define products and base prices
products = {
    'Laptop': 1000,
    'Mouse': 20,
    'Keyboard': 50,
    'Monitor': 200,
    'Headphones': 80,
    'Webcam': 60
}

# Generate data for 30 days
start_date = datetime(2025, 3, 1)
data = []

for i in range(30):  # 30 days
    current_date = start_date + timedelta(days=i)
    for product, price in products.items():
        quantity = random.randint(1, 20)
        fluctuation = random.uniform(0.95, 1.10)  # Price fluctuation
        revenue = round(price * quantity * fluctuation, 2)
        data.append({
            'Date': current_date.strftime('%Y-%m-%d'),
            'Product': product,
            'Quantity Sold': quantity,
            'Revenue ($)': revenue
        })

# Convert to DataFrame and save
df = pd.DataFrame(data)
df.to_csv('sales_data.csv', index=False)

print("✅ Realistic 'sales_data.csv' has been generated with 180+ records.")
