# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Member'
        db.create_table(u'members_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('rank', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('gor', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('egd_id', self.gf('django.db.models.fields.CharField')(max_length=8, blank=True)),
            ('kgs_nickname', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
        ))
        db.send_create_signal(u'members', ['Member'])


    def backwards(self, orm):
        # Deleting model 'Member'
        db.delete_table(u'members_member')


    models = {
        u'members.member': {
            'Meta': {'ordering': "('gor', 'last_name')", 'object_name': 'Member'},
            'egd_id': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'gor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kgs_nickname': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rank': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'})
        }
    }

    complete_apps = ['members']