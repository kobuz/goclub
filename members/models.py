# coding: utf-8
from django.db import models


class Member(models.Model):
    RANKS = [('{0}d'.format(dan), )*2 for dan in range(7, 0, -1)] + \
            [('{0}k'.format(kyu), )*2 for kyu in range(1, 21)]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    rank = models.CharField(max_length=3, blank=True, choices=RANKS)
    gor = models.IntegerField(null=True, blank=True)
    egd_id = models.CharField(max_length=8, blank=True)
    kgs_nickname = models.CharField(max_length=10, blank=True)

    def __unicode__(self):
        return u"{0.first_name} {0.last_name}".format(self)

    class Meta:
        ordering = ('gor', 'last_name',)
