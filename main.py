import requests

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


location=input("Enter location: ")

URL=f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"


resp=requests.get(URL).json()

print("temp",resp['main']['temp'])
print("temp_min",resp['main']['temp'])
print("temp_max",resp['main']['temp'])
print("description",resp['weather'][0]['description'])