import pandas as pd 
import sqlalchemy 


new_name= {
    "Country.of.Origin": "country_of_origin",
    "Farm.Name": "farm_name"
}

robusta_data_cleaned = pd.read_csv("video learning/robusta_data_cleaned.csv", parse_dates= ["Expiration"] )
robusta_data_cleaned = robusta_data_cleaned.rename(columns= new_name)
filter_data = robusta_data_cleaned[["Owner", "country_of_origin", "farm_name", "Company","Color","Expiration","altitude_mean_meters"]]
save_csv = filter_data.to_csv("new_robusta_data.csv", index= False)
print(f'{save_csv} has been downloaded')