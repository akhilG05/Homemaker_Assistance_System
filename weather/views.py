from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,JsonResponse
from django.template import Template, Context, loader
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.utils.text import slugify
from django.db.models import Q
import json
import requests
from datetime import datetime

@login_required
def index(request):
    if request.user.is_authenticated:
        city = 'Mulki,IN'
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=3196433639887d6b6ab0af665e2dc25d'

        w = requests.get(url.format(city)).json()

        riseTimestamp = w['sys']['sunrise']
        riseTime = datetime.fromtimestamp(riseTimestamp)
        setTimestamp = w['sys']['sunset']
        setTime = datetime.fromtimestamp(setTimestamp)
            
        weather = {
            'city' : w['name'],
            'temperature' : w['main']['temp'],
            'description' : w['weather'][0]['description'],
            'icon' : w['weather'][0]['icon'],
            'rise' : riseTime.time,
            'set' : setTime.time,
            'minTemp' : w['main']['temp_min'],
            'maxTemp' : w['main']['temp_max'],
        }

        context = {'weather_data' : weather}

        return render(request, 'weather/index.html', context)
    
    else:
        return redirect('landing-page')