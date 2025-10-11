import pandas as pd
from sqlalchemy import create_engine 

engine = create_engine("postgresql://postgres:P@localhost:5432/pandas_trying")
connection = engine.connect()
query = "SELECT * FROM film"
data_pagila_sql = pd.read_sql(sql = query,con= engine)
print(data_pagila_sql)

selected_column = ["film_id","title","release_year","rental_rate",\
                   "length","rating","last_update"]

pagila_selected = data_pagila_sql[selected_column]
# 4. value_count
print(pagila_selected.value_counts("rating"))
# filter rating = PG and length > 90
filter_rating = pagila_selected[(pagila_selected["rating"] == "PG") & \
                                (pagila_selected["length"] >= 90)]
print(filter_rating.head)

