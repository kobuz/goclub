from django.db import models
from django.db.models import Count
from django.utils import timezone
from django.utils.text import slugify


class Place(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=100)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class MeetingManager(models.Manager):
    def past(self):
        today = timezone.now().date()
        return self.get_queryset().filter(date__lt=today).order_by('-date')

    def upcoming(self):
        today = timezone.now().date()
        return self.get_queryset().filter(date__gte=today).order_by('date')

    def recent_players(self):
        recent_meetings = self.past()[:10]
        guys = Participant.objects.filter(meeting__in=recent_meetings)
        return guys.values_list('name', flat=True).annotate(
            num=Count('name')).order_by('-num')


class Meeting(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    notes = models.TextField(blank=True)
    place = models.ForeignKey(Place)
    date = models.DateField()

    objects = MeetingManager()

    def __str__(self):
        return "{0.place} {0.date}".format(self)

    class Meta:
        ordering = ('date',)

    def save(self, *args, **kwargs):
        # set slug for a meeting
        if not self.slug:
            self.slug = slugify('{} {}'.format(self.place, self.date))
        super(Meeting, self).save(*args, **kwargs)


class Participant(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    meeting = models.ForeignKey(Meeting, related_name='participants')

    def __str__(self):
        return self.name
