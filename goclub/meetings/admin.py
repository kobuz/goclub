from django.contrib import admin

from .models import Place, Meeting, Participant


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'address',)


class ParticipantInline(admin.StackedInline):
    model = Participant
    extra = 0


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('name', 'place', 'date',)
    list_filter = ('place',)
    readonly_fields = ('slug',)
    inlines = [ParticipantInline]
