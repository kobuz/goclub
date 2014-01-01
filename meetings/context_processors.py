# coding=utf-8
from .models import Meeting


def upcoming_meetings(request):
    return {
        'upcoming_meetings': Meeting.objects.upcoming()
    }
