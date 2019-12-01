from django.http import JsonResponse
from django.urls import reverse
from django.contrib import messages
from mobile.models import Contact
from television.models import Brand, Remote
import os
import requests
import csv

basedir = os.path.abspath(os.path.dirname(__file__))

def preprocess_text_data(raw_text_data):
	#home
	if (raw_text_data == 'open home') or (raw_text_data == 'go to home') or (raw_text_data == 'go home') or (raw_text_data == 'open homepage') or (raw_text_data == 'homepage') or (raw_text_data == 'go to homepage') or (raw_text_data == 'go homepage'):
		raw_text_data = "home"
	#signin	
	elif (raw_text_data == 'sign in') or (raw_text_data == 'open login page') or (raw_text_data == 'open sign in page') or (raw_text_data == 'login page') or (raw_text_data == 'log me in') or (raw_text_data == 'sign me in') or (raw_text_data == 'sign in page'):
		raw_text_data = "login"
	#mobile	
	elif raw_text_data == 'open mobile':
		raw_text_data = raw_text_data.split( )
		raw_text_data =  raw_text_data[1]
	#contacts	
	elif (raw_text_data == 'open contacts') or (raw_text_data == 'show contacts') or (raw_text_data == 'open contact') or (raw_text_data == 'show contact') or (raw_text_data == 'contacts book') or (raw_text_data == 'phone book') or (raw_text_data == 'contact book') or (raw_text_data == 'go to contacts'):
		raw_text_data = "contacts"
	#tv
	elif ((raw_text_data == 'open tv') or (raw_text_data == 'open TV') or (raw_text_data == 'go to TV') or (raw_text_data == 'go to television') or (raw_text_data == 'open television')):
		raw_text_data = raw_text_data.split( )
		raw_text_data =  raw_text_data[1]
	#remote	
	elif (raw_text_data == 'Add Remote') or (raw_text_data == 'add remote') or (raw_text_data == 'open remote') or (raw_text_data == 'remote') or (raw_text_data == 'go to remote') or (raw_text_data == 'show remote') or (raw_text_data == 'select remote') or (raw_text_data == 'show remote list'):
		raw_text_data = "remote"
	# elif (raw_text_data == 'open contacts') or (raw_text_data == 'show contacts') or (raw_text_data == 'open contact') or (raw_text_data == 'show contact') or (raw_text_data == 'contacts book') or (raw_text_data == 'phone book') or (raw_text_data == 'contact book') or (raw_text_data == 'go to contacts'):
		# raw_text_data = "contacts"
	#news
	elif (raw_text_data == 'open news') or (raw_text_data == 'news') or (raw_text_data == 'go to news') or (raw_text_data == 'show news') or (raw_text_data == 'news open'):
		raw_text_data = "news"
	#calculator
	elif (raw_text_data == 'open calculator') or (raw_text_data == 'calculator') or (raw_text_data == 'go to calculator') or (raw_text_data == 'show calculator') or (raw_text_data == 'calculator open'):
		raw_text_data = "calculator"
	#clock
	elif (raw_text_data == 'open clock') or (raw_text_data == 'clock') or (raw_text_data == 'go to clock') or (raw_text_data == 'show clock') or (raw_text_data == 'clock show'):
		raw_text_data = "clock"
	#alarm	
	elif (raw_text_data == 'open alarm') or (raw_text_data == 'alarm') or (raw_text_data == 'go to alarm') or (raw_text_data == 'show alarm') or (raw_text_data == 'set alarm'):
		raw_text_data = "alarm"
	#calendar	
	elif (raw_text_data == 'open calendar') or (raw_text_data == 'calendar') or (raw_text_data == 'go to calendar') or (raw_text_data == 'show calendar') or (raw_text_data == 'calendar show'):
		raw_text_data = "calendar"
	#music	
	elif (raw_text_data == 'open music') or (raw_text_data == 'music') or (raw_text_data == 'go to music') or (raw_text_data == 'show music') or (raw_text_data == 'play music') or (raw_text_data == 'songs'):
		raw_text_data = "music"
	#condition
	elif (raw_text_data == 'show current conditions') or (raw_text_data == 'current conditions') or (raw_text_data == 'show room temperature') or (raw_text_data == 'what is room temperature') or (raw_text_data == 'show room humidity') or (raw_text_data == 'what is room humidity') or (raw_text_data == 'open current conditions'):
		raw_text_data = "room"
<<<<<<< HEAD
	elif (raw_text_data == 'show team') or (raw_text_data == 'team') or (raw_text_data == 'open team page') or (raw_text_data == 'meet the team') or (raw_text_data == 'team page') or (raw_text_data == 'open team'):
		raw_text_data = "team"
=======
	#weather
	elif (raw_text_data == 'show current weather') or (raw_text_data == 'current weather') or (raw_text_data == 'weather') or (raw_text_data == 'how is weather today') or (raw_text_data == 'go to weather') or (raw_text_data == 'open weather') or (raw_text_data == 'open current weather'):
		raw_text_data = "weather"
	
>>>>>>> 31ae3028b1cedccc639dedfcc0721ce378c5d59e
	elif (("open" in raw_text_data) or ("show" in raw_text_data)) and (("contacts" in raw_text_data) or ("contact" in raw_text_data)):
		raw_text_data = raw_text_data.split( )
		for text_Data in raw_text_data:
			if (text_Data!="open") and (text_Data!="show") and (text_Data!="contact") and (text_Data!="contacts"):
				raw_text_data =  "open " + "contact " + text_Data
				break
	return raw_text_data

def get_redirect_url(raw_text_data,user):
	print(user)
	data = preprocess_text_data(raw_text_data)
	if data == 'home':
		responseurl = 'home'
		slug = ''
	elif data == 'login':
		responseurl = 'accounts:login'
		slug = ''
	elif data == 'logout':
		responseurl = 'accounts:logout'
		slug = ''
	elif data == 'mobile':
		responseurl = 'mobile:index'
		slug = ''
	elif data == 'contacts':
		responseurl = 'mobile:all-contacts'
		slug = ''
	elif data == 'tv':
		responseurl = 'television:index'
		slug = ''
	elif data == 'remote':
		responseurl = 'television:brands'
		slug = ''
	elif data == 'news':
		responseurl = 'newsapp:index'
		slug = ''
	elif data == 'calculator':
		responseurl = 'calculator:index'
		slug = ''
	elif data == 'clock':
		responseurl = 'clock:index'
		slug = ''
	elif data == 'alarm':
		responseurl = 'clock:alarm'
		slug = ''
	elif data == 'calendar':
		responseurl = 'eventCalendar:calendar'
		slug = ''
	elif data == 'room':
		responseurl = 'room:index'
		slug = ''
	elif data == 'weather':
		responseurl = 'weather:index'
		slug = ''	
	elif data == 'music':
		responseurl = 'music:index'
		slug = ''
	elif data == 'team':
		responseurl = 'team'
		slug = ''
	elif "open contact" in data:
		name = data.split( )
		try:
			get_contact = Contact.objects.filter(user=user,original_name=name[2])
			if get_contact.count() == 0:
				responseurl = ''
				slug = ''
			elif get_contact.count() == 1:
				responseurl = '/mobile/contact/'
				slug = name[2]+str(user)
			else:
				responseurl = '/mobile/contacts/'
				slug = name[2]
		except:
			pass
		voice_log_data(raw_text_data,responseurl+slug)
		return JsonResponse({
			'success': True,
			'url': responseurl+slug,
		})
	elif data == 'create contact' or data == 'add contact':
		responseurl = 'mobile:add-contact'
		slug = ''
	elif "edit contact" in data:
		name = data.split( )
		responseurl = '/mobile/contact/edit/'
		slug = name[2]+str(user)
		voice_log_data(raw_text_data,responseurl+slug)
		return JsonResponse({
			'success': True,
			'url': responseurl+slug,
		})
	elif "delete contact" in data:
		name = data.split()
		responseurl = '/mobile/contact/delete/'
		slug = name[2]+str(user)
		voice_log_data(raw_text_data,responseurl+slug)
		return JsonResponse({
			'success': True,
			'url': responseurl+slug,
		})
	elif data.startswith('call'):
		name = data.split()
		if len(name) == 1:
			responseurl = 'mobile:call-select-contact'
			slug = ''
		else:
			responseurl = '/mobile/call/'
			slug = name[1]+str(user)
			voice_log_data(raw_text_data,responseurl+slug)
			return JsonResponse({
				'success': True,
				'url': responseurl+slug,
			})
	elif data.startswith('message'):
		name = data.split()
		if len(name) == 1:
			responseurl = 'mobile:message-select-contact'
			slug = ''
		else:
			responseurl = '/mobile/message/'
			slug = name[1]+str(user)
			voice_log_data(raw_text_data,responseurl+slug)
			return JsonResponse({
				'success': True,
				'url': responseurl+slug,
			})
	elif data.startswith('show'):
		name = data.split()
		# get_remote = Remote.objects.filter(user=user, original_name=name[1])
		if len(name) == 1:
			responseurl = 'television:brands'
			slug = ''
		else:
			responseurl = '/television/'
			slug = name[1]+'-'+'tv'+'/'+'remote-models'
			voice_log_data(raw_text_data,responseurl+slug)
			return JsonResponse({
				'success': True,
				'url': responseurl+slug,
			})
	elif data.startswith('select'):
		name = data.split()
		# get_remote = Remote.objects.filter(user=user, original_name=name[1])
		if len(name) == 1:
			responseurl = 'television'
			slug = ''
		else:
			responseurl = '/television/remote/'
			slug = name[1]+'tv'+name[2]+'/'+'operate'
			voice_log_data(raw_text_data,responseurl+slug)
			return JsonResponse({
				'success': True,
				'url': responseurl+slug,
			})
	else:
		return 0
	voice_log_data(raw_text_data,str(reverse(responseurl)+slug))
	return JsonResponse({
	    'success': True,
		'url': reverse(responseurl)+slug,
	})

def voice_log_data(raw_text_data,responseurl):
	row = [raw_text_data, responseurl]
	with open(basedir + '/log/voice_log_data.csv', 'a') as csv_fle:
		writer = csv.writer(csv_fle)
		writer.writerow(row)
	csv_fle.close()