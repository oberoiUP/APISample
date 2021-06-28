import requests

APIkey = '0b9ec521e0c913cd98a5430c6fae3baf'

city = input("Enter city name: ")

url = 'https://api.openweathermap.org/data/2.5/weather?units=imperial&q=' + city + '&appid=' + APIkey
#myobj = {'text': text}

#response = requests.post(url, data = myobj)
response = requests.get(url)
#print(response.json())

weatherList = response.json()
main = weatherList['main']

print("Current Temp: {}".format(main['temp']))
print("Feels Like: {}".format(main['feels_like']))



#api.openweathermap.org/data/2.5/weather?q=London&appid=0b9ec521e0c913cd98a5430c6fae3baf