from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse
import requests
from .voice_recognizer import get_redirect_url

# Create your views here.

# def voice_recognizer(request):
# 	if request.method == 'POST':
# 		if request.is_ajax():
# 			print("data")
# 			data = request.POST.get('target')
# 			print(data)
# 			redirect_url = get_redirect_url(data,request.user)
# 			if redirect_url == 0:
# 				return redirect('home')
# 				print("Invalid voice command found")
# 				return JsonResponse({
# 	    			'success': False,
# 				})
# 			else:
# 				return redirect_url
# 		else:
# 			return redirect('home')


def voice_recognizer(request):
	if request.method == 'POST':
		# print("data")
		data = request.POST.get('target')
		print(data)
		redirect_url = get_redirect_url(data,request.user)
		if redirect_url == 0:
			# return redirect('home')
			print("Invalid voice command found")
			return JsonResponse({
    			'success': False,
			})
		else:
			return redirect_url
	else:
		return redirect('home')



# def voice_recognizer(request):
# 	if request.method == 'POST':
# 		data = request.POST.get('target')
# 		print(data)
# 		redirect_url = get_redirect_url(data,request.user)
# 		if redirect_url == 0:
# 			print("Invalid voice command found")
# 			return redirect('home')
# 		else:
# 			return redirect_url