import pandas as pd 
# group by = group data and calculate the statistic

superstore = pd.read_csv("video learning/superstore.csv")
# print(superstore,superstore.info())

superstore_group_cat = superstore.groupby("Category")
# print(superstore_group_cat)
# the result is DataFrame object 
# if want to see it(result already grouped by ) as a result, use .first()
print(superstore_group_cat.first())
# if want to see the summarize use .size()
print(superstore_group_cat.size())
# if want to seeing the data the data from each grouped use looping

for cat,dataframe in superstore_group_cat:
    print(cat) #the only category i grouped before
    print("-"*40 + "dataframe"+"-"*40)
    print(dataframe) #its a result data i was grouped

# want to seeing a single category. use .get_group("cat").head()
print("="*10 + "only furniture"+"-"*10)
print(superstore_group_cat.get_group("Furniture").head())

# want to group data > 2:
superstore_group_cat_market = superstore.groupby(["Category","Market"])
print(superstore_group_cat_market.size())

# mini excersize 
netflix = pd.read_csv("video learning/Netflix_TV_Shows_and_Movies.csv")
# print(netflix.info())

netflix_type_agecertified = netflix.groupby(["type","age_certification"])
print(netflix_type_agecertified.size())
print(netflix_type_agecertified.first())
# seeing the type movie and NC-17 
print(netflix_type_agecertified.get_group(("MOVIE","NC-17")).head())
