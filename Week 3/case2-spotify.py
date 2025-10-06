import pandas as pd

spotify_albumdf = pd.read_csv("live class/spotify-album.csv")
spotify_trackdf = pd.read_csv("live class/spotify-track.csv")

print(spotify_albumdf.info(),spotify_trackdf.info())

merge_spotifydf = spotify_trackdf.merge(spotify_albumdf,left_on="track_id",right_on="id_track")
merge_spotifydf.drop(columns="id_track",inplace= True)
print(merge_spotifydf.info())
merge_spotifydf["track_album_release_date"] = merge_spotifydf["track_album_release_date"].astype("datetime64[ns]")

merge_spotifydf["year"] = merge_spotifydf["track_album_release_date"].dt.year 
merge_spotifydf["month"] = merge_spotifydf["track_album_release_date"].dt.month 
merge_spotifydf["day"] = merge_spotifydf["track_album_release_date"].dt.day

print(merge_spotifydf["year"],merge_spotifydf["month"])
print(merge_spotifydf.info())
# print the year of highest popularity
highest_track_popularity = merge_spotifydf.track_popularity.max()

print(merge_spotifydf[merge_spotifydf["track_popularity"]==highest_track_popularity].max())
# group the data into year album and show the year album (2016-2020)

year_group = merge_spotifydf.groupby("year")
print(year_group.first())

# show data

data_2016_2020 = merge_spotifydf[(merge_spotifydf["year"]>= 2016) & (merge_spotifydf["year"]<=2020)]

print(data_2016_2020)
      
year_group_2016_2020 = data_2016_2020.groupby("year")
track = year_group_2016_2020['track_popularity'].idxmax()

most_popular = merge_spotifydf.loc[track]
print(most_popular)