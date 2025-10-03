import pandas as pd 
import requests
import json

resp = requests.get("https://www.cheapshark.com/api/1.0/deals?upperPrice=30&pageSize=1000")
print(resp)

json_cheap_shark = resp.json()
print(json_cheap_shark)

cheap_shark = pd.DataFrame(json_cheap_shark)
selected_data = ["title","storeID","gameID","salePrice","normalPrice","steamRatingText","steamRatingCount","releaseDate","lastChange"]

cheap_shark_selected = cheap_shark[selected_data]
print(cheap_shark_selected.info())

index_to40 = cheap_shark_selected.iloc[1:41]
print(index_to40)
new_column_title = {
    "storeID": "store_id",
    "gameID": "game_id",
    "salePrice": "sale_price",
    "normalPrice": "normal_price",
    "steamRatingText": "steam_rating_text",
    "steamRatingCount": "steam_rating_count",
    "releaseDate": "release_date",
    "lastChange": "last_change",
    }

index_to40 = index_to40.rename(columns= new_column_title)
print(index_to40.info())
index_to40["release_date"] = pd.to_datetime(index_to40["release_date"], unit='s')
print(index_to40["release_date"])