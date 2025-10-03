import pandas as pd 

imdb_movies = pd.read_csv("live class/IMDB_Movies.csv")

# 1.shape
print(imdb_movies.shape)
# 2. select data 
data_needed = ["movie_title","title_year","genres", "duration", "director_name","imdb_score"]

selected_data = imdb_movies[data_needed]
print(selected_data.info())

# 2b.  imdb > 6.5 
data_needed = selected_data.astype({"imdb_score":"float"})
good_review = selected_data[(selected_data["imdb_score"] > 6.5)]

print(good_review.info())

print(good_review["director_name"].value_counts())

