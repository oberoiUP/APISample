import pandas as pd
import requests
import os
import sqlalchemy
import datetime
from sqlalchemy import create_engine


def gather_input():
    city = input("Enter city name: ")
    apiKey = input("Enter Open Weather Map API Key: ")
    return city, apiKey


def build_url(city, apiKey):
    return 'https://api.openweathermap.org/data/2.5/weather?units=imperial&q='\
      + city + '&appid=' + apiKey


def get_json(url):
    response = requests.get(url)
    return response.json()


def build_dataframe(json):
    # creating data frame to add data to
    col_names = ['timestamp', 'city', 'temp', 'feels_like']
    df = pd.DataFrame(columns=col_names)
    df.loc[len(df.index)] = [datetime.datetime.now(),
                             json['name'],
                             json['main']['temp'],
                             json['main']['feels_like']]
    return df


def create_engine_function(dbName):
    return create_engine('mysql://root:codio@localhost/' + dbName)


def write_table(dataframe, dbName, tableName):
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '
              + dbName + '; "')
    dataframe.to_sql(tableName, con=create_engine_function(dbName),
                     if_exists='replace',
                     index=False)


def save_data_to_file(dataframe, dbName, tableName, fileName):
    dataframe.to_sql(tableName, con=create_engine_function(dbName),
                     if_exists='replace',
                     index=False)
    os.system('mysqldump -u root -pcodio {} > {}.sql'.format(dbName, fileName))


def load_database(dbName, fileName):
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '
              + dbName + '; "')
    os.system('mysql -u root -pcodio ' + dbName + ' < ' + fileName + '.sql')


def update_database(dbName, tableName, fileName):
    load_database(dbName, fileName)
    # write_table(dataframe, dbName, tableName, 'append')
    df = pd.read_sql_table(tableName, con=create_engine_function(dbName))
    return df


def main():

    database = 'weather'
    table = 'weather_data'
    filename = 'dump'

    df = update_database(database, table, filename)

    city, apiKey = gather_input()
    url = build_url(city, apiKey)
    json = get_json(url)

    df.loc[len(df.index)] = [datetime.datetime.now(),
                             json['name'],
                             json['main']['temp'],
                             json['main']['feels_like']]

    write_table(df, database, table)

    save_data_to_file(df, database, table, filename)

    # manual record inserts
    # os.system('mysql -u root -pcodio -e "USE weather;"'))
    # os.system('mysql -u root -pcodio -e "INSERT DATABASE IF NOT EXISTS '
    # + database_name + '; "')


if __name__ == "__main__":
    main()
