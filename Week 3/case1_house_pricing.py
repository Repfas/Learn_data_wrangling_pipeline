import pandas as pd 

house_pricingdf = pd.read_csv("live class/house-pricing.csv")
house_spesifictaionsdf = pd.read_csv("live class/house-spesifications.csv")

print(house_pricingdf.info(),house_spesifictaionsdf.info())

#1. JOIN THE DATA (USING AN INNERJOIN)

house_pricingdf = house_pricingdf.set_index("house_id")
house_spesifictaionsdf = house_spesifictaionsdf.set_index("house_id")

join_house = house_spesifictaionsdf.join(house_pricingdf,on=("house_id"),how="inner"\
                                        )

print(join_house.head())

# 2.Aggretation to find a min_price,max_price,average 
min_price = join_house.Price.min()
max_price = join_house.Price.max()
average_price = join_house.Price.mean()

print(f'the min_price is{min_price},max_price is {max_price},average is {average_price}')

# 2.b lowest price 
data_lowest_price= join_house[join_house.Price == min_price]
print(data_lowest_price)
# highest price
data_highest_price = join_house[join_house.Price == max_price]
# above average 
data_above_avarage = join_house[join_house.Price > average_price]
# under average 
data_under_avarage = join_house[join_house.Price < average_price]

print(data_above_avarage,data_highest_price,data_under_avarage)

print(join_house.info())

custom_bins = [1000,1500,2000,2500,3000]
custom_label = ["Small Homes","Medium Homes","Midsize Homes","Large Homes"]

join_house["house_category"] = pd.cut(join_house["SquareFeet"],bins= custom_bins\
                                      ,labels= custom_label)

print(join_house)

# 4. Grouping the house category
house_cat_table = join_house.groupby("house_category")

print(house_cat_table.first())
# seeing an every group 

print(house_cat_table.get_group("Small Homes").head())
print(house_cat_table.get_group("Medium Homes").head())
print(house_cat_table.get_group("Midsize Homes").head())
print(house_cat_table.get_group("Large Homes").head())

# min_small_homes
min_price_small_home = house_cat_table.get_group("Small Homes").Price.min()
print(min_price_small_home)
# max_small_homes
max_price_small_home = house_cat_table.get_group("Small Homes").Price.max()
print(max_price_small_home)

# min_max medium home 
min_price_medium_home = house_cat_table.get_group("Medium Homes").Price.min()
max_price_medium_home = house_cat_table.get_group("Medium Homes").Price.max()

print(house_cat_table.get_group("Medium Homes")[house_cat_table.get_group("Medium Homes")["Price"]== min_price_medium_home])
