"""goclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib.flatpages import views as flat_views

from members.views import MemberList
from meetings.views import MeetingDetail

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', flat_views.flatpage, {'url': '/'}, name='home'),
    url(r'^klub/$', flat_views.flatpage, {'url': '/klub/'},
        name='about'),
    url(r'^spotkania/$', flat_views.flatpage, {'url': '/spotkania/'},
        name='meetings'),
    url(r'^spotkania/(?P<slug>.*)/$', MeetingDetail.as_view(),
        name='meeting_detail'),
    url(r'^czlonkowie/$', MemberList.as_view(), name='members'),
    url(r'^kontakt/$', flat_views.flatpage, {'url': '/kontakt/'},
        name='contact'),
]
