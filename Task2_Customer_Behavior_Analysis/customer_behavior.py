import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("shopping_trends.csv")

print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nMean Age:", df["Age"].mean())
print("Median Age:", df["Age"].median())

print("\nMode Age:")
print(df["Age"].mode())

print("\nMissing Values:")
print(df.isnull().sum())

gender_count = df["Gender"].value_counts()
gender_count.plot(kind="bar")
plt.title("Customers by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()

category_count = df["Category"].value_counts()
category_count.plot(kind="bar")
plt.title("Purchases by Category")
plt.xlabel("Category")
plt.ylabel("Number of Purchases")
plt.show()

df["Age"].plot(kind="hist", bins=10)
plt.title("Age Distribution of Customers")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()