import pandas as pd
# Load dataset (make sure CSV is in same folder)
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# 1. View first rows
print("First 5 rows:\n")
print(df.head())

# 2. Column names
print("\nColumns:\n")
print(df.columns)

# 3. Total Sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# 4. Total Quantity
total_quantity = df["Quantity"].sum()
print("\nTotal Quantity Sold:", total_quantity)

# 5. Top 5 Products (Highest Sales)
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)
print("\nTop 5 Products by Sales:\n")
print(top_products.head())

# 6. Lowest 5 Products (Lowest Sales)
low_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=True)
print("\nLowest 5 Products by Sales:\n")
print(low_products.head())

# 7. Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()
print("\nSales by Category:\n")
print(category_sales)

# 8. Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:\n")
print(region_sales)

# 9. Top 5 Customers
top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False)
print("\nTop 5 Customers:\n")
print(top_customers.head())

# 10. Save output file
top_products.head().to_csv("top_products.csv")

print("\nAnalysis Completed Successfully!")
