import pandas as pd 

# feature engineer --> process create a new input features from existing data
# extraction --> extract one data into small pieces of details

superstoredf = pd.read_csv("video learning/superstore.csv")

selected_sstore = superstoredf[["Category","Order.Date","Profit"]]

selected_sstore["Order.Date"] = selected_sstore["Order.Date"].astype("datetime64[ns]")
print(selected_sstore.info())
selected_sstore["year"] = selected_sstore["Order.Date"].dt.year 

selected_sstore["Month"] = selected_sstore["Order.Date"].dt.month
selected_sstore["day"] = selected_sstore["Order.Date"].dt.day
print(selected_sstore.info())

# df['jumlah_kata'] = df['kolom_teks'].apply(lambda x: len(x.split()))

# Encoding --> turn word into number for numerical format

selected_sstore["Category"] = selected_sstore["Category"].astype("category")

print(selected_sstore.info())

selected_sstore["cat_label"] = selected_sstore["Category"].cat.codes 

print(selected_sstore)

# One hot encoding --> to make the machine learning understand it
# using a .get_dumies()
superstore_encoded = pd.get_dummies(selected_sstore,columns=["Category"], dtype= int)

print(superstore_encoded)


# Binning --> classify the numeric into interval

cardiovasdisease = pd.read_csv("")