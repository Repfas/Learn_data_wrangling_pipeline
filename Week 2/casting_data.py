import pandas as pd
# casting data = change the type of data for analyse 

supermarket_sales = pd.read_csv("video learning/supermarket_sales.csv")

print(supermarket_sales.head())
# how to know type data each coloumn
supermarket_sales.info()
# to change type data use a  astype:
# supermarket_sales["Total"]= supermarket_sales["Total"].astype('int64')
# print(supermarket_sales.loc[:,"City":"Date"])
# # value_count to know the count of data 

# print(supermarket_sales["Gender"].value_counts())


# want to change a lot of type data
# 1. while read data 
new_type = {
    "Payment": "category"
}

new_data = pd.read_csv("video learning/supermarket_sales.csv",dtype=new_type, parse_dates=["Date","Time"])

print(new_data.info())