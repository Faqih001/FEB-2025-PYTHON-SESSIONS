import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv('sales_data.csv')

# Total Revenue
total_revenue = df['Revenue ($)'].sum()

# Best-Selling Product
best_selling = df.groupby('Product')['Quantity Sold'].sum().sort_values(ascending=False)
top_product = best_selling.idxmax()
top_quantity = best_selling.max()

# Highest Sales Day
daily_sales = df.groupby('Date')['Revenue ($)'].sum()
top_day = daily_sales.idxmax()
top_day_revenue = daily_sales.max()

# Save results
with open('sales_summary.txt', 'w') as f:
    f.write(f"Total Revenue: ${total_revenue:,.2f}\n")
    f.write(f"Best-Selling Product: {top_product} ({top_quantity} units sold)\n")
    f.write(f"Highest Sales Day: {top_day} (${top_day_revenue:,.2f})\n")

# Print insights
print(f"📊 Total Revenue: ${total_revenue:,.2f}")
print(f"🏆 Best-Selling Product: {top_product} ({top_quantity} units sold)")
print(f"📅 Highest Sales Day: {top_day} (${top_day_revenue:,.2f})")

# Bonus: Plot sales trend
plt.figure(figsize=(8, 4))
daily_sales.plot(marker='o')
plt.title('📈 Daily Revenue Trend')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.grid(True)
plt.tight_layout()
plt.savefig('sales_trend.png')
plt.show()
