from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

from members.views import MemberList
from meetings.views import MeetingDetail

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^klub$', TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^spotkania$', TemplateView.as_view(template_name='meetings.html'),
        name='meetings'),
    url(r'^spotkania/(?P<slug>.*)$', MeetingDetail.as_view(), name='meeting_detail'),
    url(r'^czlonkowie$', MemberList.as_view(), name='members'),
)
