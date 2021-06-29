import requests

text = input("Enter text: ")

url = 'http://text-processing.com/api/sentiment/'
myobj = {'text': text}

response = requests.post(url, data=myobj)
print(response.json())
