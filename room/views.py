from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.utils.text import slugify
from django.utils import timezone
from django.db.models import Q
from accounts.models import RPiUser
import requests
from .scripts import temp_humidity

global temp, hum



@login_required
def index(request):
    if request.user.is_authenticated:

        # temp = temp_humidity.temperature()
        # hum = temp_humidity.humidity()

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=a01c87a82cf43b953f9b305db7369f68'
        city = 'Mulki,IN'
        
        r = requests.get(url.format(city)).json()
        
        current_conditions = {
            # 'temperature': temp,
            # 'humidity': hum,
            'city' : r['name'],
			'temperature' : r['main']['temp'],
			'description' : r['weather'][0]['description'],
			'icon' : r['weather'][0]['icon'],
		}
        
        context = {'current_conditions' : current_conditions}
        
        return render(request, 'room/index.html', context)