import pandas as pd 

# aggretation mean converting every value into one summary 
# mean() --> average 
# std() --> standard deviation
# median() --> middle value 
# max() --> find the max value 
# min() --> find the min value 
# count() --> count how many data in one column
# nunique() --> find the unique value 

# syntax:
# DataFrame.column_name.aggretation_function

superstore = pd.read_csv("video learning/superstore.csv")
print(superstore)

mean_sales = superstore.Sales.mean()
print(f"the sales mean is {round(mean_sales,3)}")

max_sales = superstore.Sales.max()
print(f"the max value of sales is {max_sales}")

unique_cat = superstore.Category.nunique()
print(f'the total unique category is {unique_cat}')

# doing aggregate more than 2
# using a .agg(func = ["agg1","agg2",...],axis = 0/1)

cardiac_disease_df = pd.read_csv("video learning/Cardiovascular_Disease.csv")
print(cardiac_disease_df.info())
# the axis = 1 mean that aggretation about row 
# axis  =0 mean aggretation abour column 
min_max_carddisease = cardiac_disease_df.agg(func=["min","max","nunique"],axis=0)

print(min_max_carddisease)
min_max_carddisease = cardiac_disease_df.agg(func=["min","max","nunique"],axis=1)

print(min_max_carddisease)
# if we want to do aggretation each column
# .agg({column1:"agg1",{column2:agg2})
# and if want to duplicate it use list on dict


agg_information = {
    "age":["min","max","mean"],
    "restingBP":["min","max","mean"],
    "gender":"count"
}

multi_agg_cardisease = cardiac_disease_df.agg(agg_information)
print(multi_agg_cardisease)

# MINI EXCERCISE
bank_term_deposit_df = pd.read_csv("video learning/bank_term_deposit.csv")
print(bank_term_deposit_df.info())

agg_age_balance = {
    "age":["min","max","mean"],
    "balance":["min","max"]
}
agg_marital = {
    "marital":["mode"],
    "education":["mode"]
}


agg_bank_term_ab = bank_term_deposit_df.agg(agg_age_balance)
agg_bank_term_mar_ed = bank_term_deposit_df.agg(agg_marital)

print(agg_bank_term_ab)
print("-"*100)
print(agg_bank_term_mar_ed)