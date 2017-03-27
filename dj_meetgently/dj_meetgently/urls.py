"""dj_meetgently URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from chat import views

urlpatterns = [
    url(r'^$',  views.about, name='about'),
    url(r'^new_socket/admin/', admin.site.urls),
    url(r'^new_socket/new/$', views.new_room, name='new_room'),
    url(r'^new_socket/$', views.chat_room, name='chat_room'),
    #url(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
    #url(r'^new_socket/chat/$', views.chat_room, name='chat_room'),
]