"""homemaker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
from accounts.views import landing_page, home, team

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', landing_page, name='landing-page'),
    url(r'^home/$', home, name='home'),
    url(r'^team/$', team, name='team'),
    url(r'^audiosystem/', include('audiosystem.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^mobile/', include('mobile.urls')),
    url(r'^television/', include('television.urls')),
    url(r'^calculator/', include('calculator.urls')),
    url(r'^weather/', include('weather.urls')),
    url(r'^news/', include('newsapp.urls')),
    url(r'^clock/', include('clock.urls')),
    url(r'^music/', include('music.urls')),
    url(r'^playlist/', include('playlist.urls')),
    url(r'^eventCalendar/', include('eventCalendar.urls')),
    url(r'^room/', include('room.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)