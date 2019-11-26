from django.conf.urls import include, url
from . import views

app_name = 'clock'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'alarm/$', views.alarm, name='alarm'),
]