from django.views.generic import ListView

from .models import Member


class MemberList(ListView):
    model = Member
    template_name = 'member_list.html'
    context_object_name = 'members'
