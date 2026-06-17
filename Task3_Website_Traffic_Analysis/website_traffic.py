import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("website_traffic.csv")

print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nMean Page Views:", df["Page Views"].mean())
print("Median Page Views:", df["Page Views"].median())

print("\nMode Page Views:")
print(df["Page Views"].mode())

print("\nMissing Values:")
print(df.isnull().sum())

traffic_count = df["Traffic Source"].value_counts()
traffic_count.plot(kind="bar")
plt.title("Traffic Source Distribution")
plt.xlabel("Traffic Source")
plt.ylabel("Visitors")
plt.show()

df["Page Views"].plot(kind="hist", bins=10)
plt.title("Distribution of Page Views")
plt.xlabel("Page Views")
plt.ylabel("Frequency")
plt.show()

df["Session Duration"].plot(kind="hist", bins=10)
plt.title("Session Duration Distribution")
plt.xlabel("Session Duration")
plt.ylabel("Frequency")
plt.show()