from django.views.generic import DetailView

from .models import Meeting


class MeetingDetail(DetailView):
    model = Meeting
    template_name = 'meeting_detail.html'
