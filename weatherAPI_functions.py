import pandas as pd
import requests, sqlalchemy, datetime
from sqlalchemy import create_engine

def gather_input(): 
	city = input("Enter city name: ")
	apiKey = input("Enter Open Weather Map API Key: ")
	return city, apiKey

def build_url(city, apiKey): 
	return 'https://api.openweathermap.org/data/2.5/weather?units=imperial&q=' + city + '&appid=' + apiKey

def get_json(url): 
	response = requests.get(url)
	return response.json()

def build_dataframe(json): 
  #creating data frame to add data to
  col_names = ['timestamp', 'city', 'temp', 'feels_like']
  df  = pd.DataFrame(columns = col_names)
  df.loc[len(df.index)] = [datetime.datetime.now(), json['name'], json['main']['temp'], json['main']['feels_like']]
  return df

def write_table(dataframe, dbName, tableName): 
  engine = create_engine('mysql://root:codio@localhost/{}'.format(dbName))
  dataframe.to_sql(tableName, con=engine, if_exists='replace', index=False)

def main():
  city, apiKey = gather_input()
  url = build_url(city, apiKey)
  json = get_json(url)
  df = build_dataframe(json)
  write_table(df, 'weather', 'weather_data')
  

if __name__ == "__main__":
    main()
    

