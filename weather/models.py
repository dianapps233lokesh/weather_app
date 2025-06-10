from django.db import models

class WeatherModel(models.Model):
    location=models.CharField(max_length=200)
