import pandas as pd

df=pd.read_csv('../data/synthetic_transactions.csv')

print("Summary Statistics:")
print(df.describe())

print("\nUnique Customers:", df['CustomerID'].nunique())
print("Average Transaction Amount:", df['TransactionAmount'].mean())
