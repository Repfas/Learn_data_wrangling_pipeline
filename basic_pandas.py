import pandas as pd 

# 2 type of data structure in pandas 
# 1. Series --> single data column 
dict_data = {
    "IDMF": 5,
    "TROF": 2,
    "GODF": 1,
    "DETN": 1
}
series_data = pd.Series(dict_data)
print(series_data)

list_data = [5, 2, 1, 1]
index_data = ["IDMF", "TROF", "GODF", "DETN"]

series_data_2 = pd.Series(list_data,index= index_data)
print(series_data_2)

# 2. DataFrame --> 2D table with rows and column using dict of list 

data = {
    "Product name": ['Indomie',"Black soy","My Coffee","Teaaaaaly"],
    "type_product": ['Noodle',"Soy sauce","Coffee sachet","Tea"],
    "amount": [5,2,3,1]
}

df = pd.DataFrame(data)

print(df)
print("-------------------------"*5)
# if wanna add the index: index mean the first row in the table 
df_with_index = pd.DataFrame(data,index=index_data)

print(df_with_index)

# import csv data 
data = pd.read_csv('Week 2/video learning/example-data-1.csv')

print(data)
# if want to make an "kode barang" as indext 

data = pd.read_csv('Week 2/video learning/example-data-1.csv',index_col= "kode_barang")
print(data)

# rename the titles
# the header parameter is using for row as a title ex: header = 1 so the 2nd row gonna be a title
# the names is to create a tittle names 
name_title = ['product_name',"category","price","quantity"]
data = pd.read_csv('Week 2/video learning/example-data-2.csv', header = None, names= name_title)

print(data)
print("-"*100)
# data.head(n) is using for showing the data from upper(top data)
# data.tail is using for showing the column title (lower data)
# data.column is for showing the data title column
print(data.columns)
print("-"*100)
print(data.head)
print("-"*100)
# how to change the data column
# just overwrite it
data.columns = ["name","cat","price","quant"]
print(data)
data_mall_cust = pd.read_csv("Week 2/video learning/mall-customers.csv")
print(data_mall_cust.head(7))
print(data_mall_cust.tail(3))
print("-"*100)
# LEARN IMPORT FROM API
import requests 

pokemon_data = requests.get("https://pokeapi.co/api/v2/pokemon?limit=500")
poke_json = pokemon_data.json()
# print(poke_json)
data_tab_pokemon = pd.DataFrame(poke_json["results"])
print(data_tab_pokemon)


# DATABASE:
# from sqlalchemy import create_engine 
# engine = create_engine("postgresql://postgres:cobapassword@localhost/data-wrangling")
# query = "SELECT * FROM Rrobusta_data_cleaned.csv"

# data = pd.read_sql(sql= query, con = engine)
# print(data)

# SELECTING DATA
data_supermarket = pd.read_csv("Week 2/video learning/supermarket_sales.csv")
selected_data = ["Invoice ID", "City", "Customer type"]
print(data_supermarket[selected_data])

# filter data
print("-"*40 + "cash payment"+ "-"*45)
e_wallet_payment = data_supermarket[data_supermarket["Payment"] == "Cash"]
print(e_wallet_payment)

extra_bonus = data_supermarket[(data_supermarket["Payment"] == "Ewallet") & (data_supermarket["Total"] >= 700)]
print(extra_bonus)

big_sales_except_yangon = data_supermarket[(data_supermarket["Branch"] != "A") & (data_supermarket['Total'] >= 700)]
print(big_sales_except_yangon[["Branch","City","Total","cogs"]])