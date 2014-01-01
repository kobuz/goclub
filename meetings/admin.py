# coding: utf-8
from django.contrib import admin

from .models import Place, Meeting, Participant


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'address',)

admin.site.register(Place, PlaceAdmin)


class ParticipantAdmin(admin.StackedInline):
    model = Participant
    extra = 0


class MeetingAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'date',)
    list_filter = ('place',)
    readonly_fields = ('slug',)
    inlines = [ParticipantAdmin]

admin.site.register(Meeting, MeetingAdmin)
