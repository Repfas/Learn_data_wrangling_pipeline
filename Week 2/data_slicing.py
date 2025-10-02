# Data slicing --> selecting data using an indexing 
# 2 type of indexing in data slicing
# .iloc(index based/index position) & loc(spesific name based/label position)
import pandas as pd 

cust_data = pd.read_csv("video learning/customers_data.csv", index_col = None)

print(cust_data.head())

print(cust_data.iloc[:2, 3:])
print(cust_data.loc[0:3, "name":"country"])

