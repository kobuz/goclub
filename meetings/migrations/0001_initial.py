# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table(u'meetings_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'meetings', ['Place'])

        # Adding model 'Meeting'
        db.create_table(u'meetings_meeting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['meetings.Place'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'meetings', ['Meeting'])

        # Adding model 'Participant'
        db.create_table(u'meetings_participant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('meeting', self.gf('django.db.models.fields.related.ForeignKey')(related_name='participants', to=orm['meetings.Meeting'])),
        ))
        db.send_create_signal(u'meetings', ['Participant'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table(u'meetings_place')

        # Deleting model 'Meeting'
        db.delete_table(u'meetings_meeting')

        # Deleting model 'Participant'
        db.delete_table(u'meetings_participant')


    models = {
        u'meetings.meeting': {
            'Meta': {'ordering': "('date',)", 'object_name': 'Meeting'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['meetings.Place']"})
        },
        u'meetings.participant': {
            'Meta': {'object_name': 'Participant'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meeting': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'participants'", 'to': u"orm['meetings.Meeting']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'meetings.place': {
            'Meta': {'object_name': 'Place'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['meetings']