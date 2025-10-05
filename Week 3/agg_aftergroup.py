import pandas as pd 

# doing aggretation after groupping

superstore = pd.read_csv("video learning/superstore.csv")
print(superstore.info())

superstore_cat = superstore.groupby("Category")
superstore_cat_max = superstore_cat.max()
print(superstore_cat_max.info()) 

# spesific one: 

superstore_cat_avg_quantity = superstore_cat["Quantity"].mean()
# print(superstore_cat_avg_quantity)

# mini excercise:
bank_term_deposit_df = pd.read_csv("video learning/bank_term_deposit.csv")
group_marital = bank_term_deposit_df.groupby("marital")
agg_age_balance = {
    "age":["min","max","mean"],
    "balance":["min","max"]
}
aggregation_based_on = ["age","balance"]

# based on mean
group_marital_mean = group_marital[aggregation_based_on].mean()
print(f'the mean is {group_marital_mean}')

# base on max 
group_marital_max = group_marital[aggregation_based_on].max()
print(f'the max is {group_marital_max}')

group_marital_min = group_marital[aggregation_based_on].min()
print(f'the min is {group_marital_min}')
