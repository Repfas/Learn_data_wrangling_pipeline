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
# the header parameter is using for row as a title ex: header = 1 so the scnd row gonna be a title
# the names is to create a tittle names 
name_title = ['product_name',"category","price","quantity"]
data = pd.read_csv('Week 2/video learning/example-data-2.csv', header = None, names= name_title)

print(data)
a= data.head
print(a)
# how to change the 