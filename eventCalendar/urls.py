from django.conf.urls import url
from . import views

app_name = 'eventCalendar'
urlpatterns = [
    url(r'^calendar/$', views.index.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]
