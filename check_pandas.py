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
