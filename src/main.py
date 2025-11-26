
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('../data/transactions.csv')

print("Descriptive Statistics for TransactionAmount:")
stats=df['TransactionAmount'].describe()
print(stats)

print("\nUnique Customers:", df['CustomerID'].nunique())
print("Average Transaction Amount:", df['TransactionAmount'].mean())

print("\nSUMMARY OF FINDINGS:")
print("Total transactions:", len(df))
print("Mean amount:", round(df['TransactionAmount'].mean(),2))
print("Median amount:", round(df['TransactionAmount'].median(),2))
print("Most frequent categories:", df['ProductCategory'].value_counts().head().to_dict())

plt.hist(df['TransactionAmount'])
plt.title('Transaction Amount Distribution')
plt.xlabel('Amount ($)')
plt.ylabel('Frequency')
plt.savefig('../outputs/hist_amount.png')
plt.close()

df['ProductCategory'].value_counts().plot(kind='bar')
plt.title('Product Category Distribution')
plt.xlabel('Category')
plt.ylabel('Count')
plt.savefig('../outputs/bar_category.png')
plt.close()
