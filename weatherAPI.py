import requests

APIkey = ''

city = input("Enter city name: ")

url = 'https://api.openweathermap.org/data/2.5/weather?units=imperial&q='
url += city + '&appid=' + APIkey

response = requests.get(url)
# print(response.json())

weatherList = response.json()
main = weatherList['main']

print("Current Temp: {}".format(main['temp']))
print("Feels Like: {}".format(main['feels_like']))
