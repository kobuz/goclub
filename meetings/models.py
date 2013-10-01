# coding: utf-8
from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Meeting(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    place = models.ForeignKey(Place)
    date = models.DateField()

    def __unicode__(self):
        return "{0.name} / {0.place} / {0.date}".format(self)

    class Meta:
        ordering = ('date',)


class Participant(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    meeting = models.ForeignKey(Meeting, related_name='participants')

    def __unicode__(self):
        return self.name
