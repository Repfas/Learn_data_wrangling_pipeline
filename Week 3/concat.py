import pandas as pd 

# concate: its stacking data
df1 = {
    'pet': ['Dog', 'Cat'],
    'color' : ['Black', 'White'],
    'tall':['100cm',"50 cm"]
}

df2 = {
    'pet': ['Fish', 'Turtle'],
    'color' : ['Yellow', 'Black'],
    "length" :["5 cm","15 cm"]
}

pdf1 = pd.DataFrame(df1)
pdf2 = pd.DataFrame(df2)

print(pdf1.head())
print(pdf2.head())
# axis 1 = add more coloumn and axis = 0 add row
# key is to separate the concate data
concat_data = pd.concat([pdf1,pdf2], axis = 0, keys = ["land","water"])
print(concat_data)

# read data reddit_opinion_climate_change.csv
rocc = pd.read_csv("video learning/reddit_opinion_climate_change.csv")
rocca = pd.read_csv("video learning/reddit_opinion_climate_change_author.csv")
# Menampilkan 5 data teratas
print(rocc.head())
print(rocca.head())

concat_reddit = pd.concat([rocc,rocca],axis=0,join='inner')
print(concat_reddit)