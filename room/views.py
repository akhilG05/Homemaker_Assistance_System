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

@login_required
def index(request):
    if request.user.is_authenticated:

        temp = temp_humidity.temperature
        hum = temp_humidity.humidity

        room_condition = {
            'Temperature': temp,
            'Humidity': hum,
	}

        context = {'room_condition' : room_condition}

        return render(request, 'room/index.html', context)
