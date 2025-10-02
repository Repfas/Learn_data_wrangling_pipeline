import json
import pandas as pd
import requests

a = requests.get("https://raw.githubusercontent.com/Kurikulum-Sekolah-Pacmann/data_api_preclass/refs/heads/main/data_api.json")
json_data = a.json()
# print(json_data["entries"])
df = pd.DataFrame(json_data['entries'])
print(df)
df[df["Category"] == "Animals"]
print(df)


