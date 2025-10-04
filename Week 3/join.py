
import pandas as pd 


# JOIN = a method to combine all dataframe based matched by index
product_data = pd.read_csv("video learning/product.csv")
order_data = pd.read_csv("video learning/order.csv")

print(product_data.info() , order_data.info())

# join data 
# there's a parameter on join:
# dataframe(required), on(which column to use matching *optional). 
# sort(sorting the data), lsuffix(point the same column name on left ), 
# rsuffix (point the same column name on right)
product_order_join = product_data.join(order_data, on= "produk_id",lsuffix="_left",rsuffix="_right")

# if we want to join it without using a suffix:
# set the same column with a set index 
product_data.set_index("produk_id", inplace= True)
order_data.set_index("produk_id",inplace=True)

product_order_join_set = product_data.join(order_data, on=("produk_id"))
print(product_order_join_set.head())