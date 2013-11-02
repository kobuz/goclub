# coding: utf-8
from django.db import models
from django.db.models import Count
from django.utils import timezone


class Place(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class MeetingManager(models.Manager):
    def past(self):
        today = timezone.now().date()
        return self.get_query_set().filter(date__lt=today).order_by('-date')

    def upcoming(self):
        today = timezone.now().date()
        return self.get_query_set().filter(date__gte=today).order_by('date')


class Meeting(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    place = models.ForeignKey(Place)
    date = models.DateField()

    objects = MeetingManager()

    def __unicode__(self):
        return "{0.name} / {0.place} / {0.date}".format(self)

    class Meta:
        ordering = ('date',)


class ParticipanManager(models.Manager):
    def coming_often_recently(self):
        recent_meetings = Meeting.objects.past()[:10]
        guys = self.get_query_set().filter(meeting__in=recent_meetings)
        return guys.values_list('name', flat=True).annotate(
            num=Count('name')).order_by('-num')


class Participant(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    meeting = models.ForeignKey(Meeting, related_name='participants')

    objects = ParticipanManager()

    def __unicode__(self):
        return self.name
