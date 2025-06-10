from django.shortcuts import render
from dotenv import load_dotenv
load_dotenv()
import requests
import os

def weather_view(request):
    if request.method=='POST':
        location=request.POST.get('location')
        if location:
            API_KEY = os.getenv('API_KEY')
            URL=f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"
            resp=requests.get(URL).json()
            print(resp)
            params={}
            params['temp']=resp['main']['temp']-273
            params['min_temp']=resp['main']['temp_min']-273
            params['max_temp']=resp['main']['temp_max']-273
            params['description']=resp['weather'][0]['description']
        return render(request,"form.html",{"results":params})
    else:
        return render(request,"form.html")