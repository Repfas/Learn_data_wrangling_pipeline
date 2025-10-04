import pandas as pd 

opinion_climate_change = pd.read_csv("video learning/opinion_climate_change.csv")
opinion_author = pd.read_csv("video learning/opinion_climate_change_author.csv")

print(opinion_author.info())
print(opinion_climate_change.info())
# a method to combine 2 data based on column or index

# parameter: 
# right(dataframe that merge),how(type of merge),left_on/right_on(for column)
# left/right_index(for index)
opinion_merge = opinion_climate_change.merge(opinion_author,left_on="comment_id",\
                                             right_on="id_comment")
print(opinion_merge.info())