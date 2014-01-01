# coding=utf-8
from django.views.generic import ListView

from .models import Member


class MemberList(ListView):
    model = Member
    template_name = 'members.html'
    context_object_name = 'members'
