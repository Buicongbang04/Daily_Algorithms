import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv("LAB 2.1/sales_data.csv")

# Step 2: Data Exploration
# View the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Check for missing data
print("\nMissing data summary:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Filter the data for a specific product (e.g., Product A)
product_a_data = df[df["Product"] == "Product A"]


print("Data Infor")
print(df.info())

# Step 3: Basic Data Visualization
# Create a bar chart for product sales
product_sales = df.groupby("Product")["Amount"].sum()
product_sales.plot(kind="bar", title="Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

# Create a line chart for daily sales
df["Date"] = pd.to_datetime(df["Date"])
daily_sales = df.groupby("Date")["Amount"].sum()
daily_sales.plot(kind="line", title="Daily Sales")
plt.xlabel("Date")
plt.ylabel("Sales Amount")
plt.show()

# Create a scatter plot for product sales by date
plt.scatter(df["Date"], df["Amount"])
plt.title("Product Sales by Date")
plt.xlabel("Date")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.show()
