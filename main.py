import requests

API_KEY='5fe2a78ea1f396c14e6f694ae9857057'
location=input("Enter location: ")

URL=f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"


resp=requests.get(URL).json()

print(resp['weather'])