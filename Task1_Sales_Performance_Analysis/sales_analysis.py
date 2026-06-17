import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SampleSuperstore.csv", encoding="latin1")

print(df.head())
print(df.info())
print(df.describe())

print("Mean Sales:", df["Sales"].mean())

print("Median Sales:", df["Sales"].median())

print("Mode Sales:")
print(df["Sales"].mode())

print(df.isnull().sum())

sales_by_category = df.groupby("Category")["Sales"].sum()
sales_by_category.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

plt.figure(figsize=(8,5))
df["Sales"].plot(kind="hist", bins=20)
plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

region_sales = df.groupby("Region")["Sales"].sum()
plt.figure(figsize=(8,8))
region_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.show()

