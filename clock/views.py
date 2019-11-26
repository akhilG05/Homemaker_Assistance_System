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

@login_required
def index(request):
	return render(request, 'clock/index.html')

@login_required
def alarm(request):
	return render(request, 'clock/alarm.html')