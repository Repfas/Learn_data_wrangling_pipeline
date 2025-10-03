import pandas as pd
# 1.a read the sales_data_2019.csv
data_2019 = pd.read_csv("live class/sales_data_2019.csv")
# print(data_2019.info(),data_2019.head(100))

# 2.a remove Order_id

remove_order_id = data_2019[["Order Date","Product","Quantity Ordered","Price Each",\
                            "Purchase Address"]]
print(remove_order_id.head())
# 2.b slicing  data 150-4213 

print(remove_order_id.iloc[150:4214])

# 3. quantity order > 2 or price each >= 125 
data_filter = remove_order_id.iloc[150:4214][(remove_order_id["Quantity Ordered"] >2) | (remove_order_id["Price Each"] >= 125) ]

print(data_filter)

save_csv = data_filter.to_csv("new_sales_data.csv",index= False)
print(f'{save_csv} has been saved')