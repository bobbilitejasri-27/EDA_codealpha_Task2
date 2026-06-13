import pandas as pd

data = pd.read_csv("quotes_dataset.csv")

print("===== FIRST 5 ROWS =====")
print(data.head())

print("\n===== DATASET INFO =====")
data.info()

print("\n===== MISSING VALUES =====")
print(data.isnull().sum())

print("\n===== SUMMARY =====")
print(data.describe(include="all"))