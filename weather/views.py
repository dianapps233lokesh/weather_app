from django.shortcuts import render
from dotenv import load_dotenv
load_dotenv()
import requests
import os

def weather_view(request):
    try:
        if request.method=='POST':
            location=request.POST.get('location')
            if location:
                API_KEY = os.getenv('API_KEY')
                URL=f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"
                resp=requests.get(URL).json()
                
                print(resp)
                params={}
                params['temp']=round(resp['main']['temp']-273,1)
                params['min_temp']=round(resp['main']['temp_min']-273,1)
                params['max_temp']=round(resp['main']['temp_max']-273,1)
                params['description']=resp['weather'][0]['description']
            return render(request,"form.html",{"results":params})
        else:
            return render(request,"form.html")
    
    except Exception as e:
        # err={"msg":e}
        return render(request,"form.html",{"err":"City not found"})