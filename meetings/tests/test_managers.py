# coding=utf-8
import datetime

from django.test import TestCase
from django.utils import timezone
from model_mommy import mommy

from ..models import Meeting, Participant


class MeetingTest(TestCase):
    def setUp(self):
        today = timezone.now().today()
        mommy.make(Meeting, date=today - datetime.timedelta(days=7))
        mommy.make(Meeting, date=today + datetime.timedelta(days=2))
        mommy.make(Meeting, date=today + datetime.timedelta(days=10))

    def test_all_events(self):
        self.assertEqual(Meeting.objects.count(), 3)

    def test_past_events(self):
        self.assertEqual(Meeting.objects.past().count(), 1)

    def test_future_events(self):
        self.assertEqual(Meeting.objects.upcoming().count(), 2)


class ParticipantTest(TestCase):
    def setUp(self):
        today = timezone.now().today()
        meeting1 = mommy.make(Meeting, date=today - datetime.timedelta(days=4))
        meeting2 = mommy.make(Meeting, date=today - datetime.timedelta(days=10))
        meeting3 = mommy.make(Meeting, date=today - datetime.timedelta(days=12))
        for nick in ['ptak', 'wilk']:
            mommy.make(Participant, name=nick, meeting=meeting1)
        for nick in ['wilk', 'koza']:
            mommy.make(Participant, name=nick, meeting=meeting2)
        for nick in ['wilk', 'ptak', 'drzewo']:
            mommy.make(Participant, name=nick, meeting=meeting3)

    def test_coming_often_recently(self):
        names = Meeting.objects.recent_players()
        self.assertEqual(len(names), 4)
        self.assertEqual(list(names), ['wilk', 'ptak', 'drzewo', 'koza'])
