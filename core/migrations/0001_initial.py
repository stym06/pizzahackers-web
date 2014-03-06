# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hacker'
        db.create_table(u'core_hacker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='hacker', unique=True, to=orm['auth.User'])),
            ('batch', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('branch', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('roll_number', self.gf('django.db.models.fields.CharField')(unique=True, max_length=12)),
            ('profile_image_url', self.gf('django.db.models.fields.CharField')(default='/static/core/img/placeholder_hacker.png', max_length=255)),
            ('thumbnail_url', self.gf('django.db.models.fields.CharField')(default='/static/core/img/placeholder_hacker.png', max_length=255)),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('interests', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('blog', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('github_id', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('facebook_id', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('twitter_id', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
        ))
        db.send_create_signal(u'core', ['Hacker'])

        # Adding model 'Proposal'
        db.create_table(u'core_proposal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('completed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('repo_url', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('proposer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='proposals', to=orm['core.Hacker'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Proposal'])

        # Adding M2M table for field upvotes on 'Proposal'
        m2m_table_name = db.shorten_name(u'core_proposal_upvotes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('proposal', models.ForeignKey(orm[u'core.proposal'], null=False)),
            ('hacker', models.ForeignKey(orm[u'core.hacker'], null=False))
        ))
        db.create_unique(m2m_table_name, ['proposal_id', 'hacker_id'])

        # Adding model 'Discussion'
        db.create_table(u'core_discussion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='Untitled Discussion', max_length=255)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('hacker', self.gf('django.db.models.fields.related.ForeignKey')(related_name='discussions', to=orm['core.Hacker'])),
        ))
        db.send_create_signal(u'core', ['Discussion'])

        # Adding model 'Comment'
        db.create_table(u'core_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comments', to=orm['core.Hacker'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('discussion', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='comments', null=True, to=orm['core.Discussion'])),
            ('proposal', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='comments', null=True, to=orm['core.Proposal'])),
        ))
        db.send_create_signal(u'core', ['Comment'])


    def backwards(self, orm):
        # Deleting model 'Hacker'
        db.delete_table(u'core_hacker')

        # Deleting model 'Proposal'
        db.delete_table(u'core_proposal')

        # Removing M2M table for field upvotes on 'Proposal'
        db.delete_table(db.shorten_name(u'core_proposal_upvotes'))

        # Deleting model 'Discussion'
        db.delete_table(u'core_discussion')

        # Deleting model 'Comment'
        db.delete_table(u'core_comment')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'discussion': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'comments'", 'null': 'True', 'to': u"orm['core.Discussion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proposal': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'comments'", 'null': 'True', 'to': u"orm['core.Proposal']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': u"orm['core.Hacker']"})
        },
        u'core.discussion': {
            'Meta': {'object_name': 'Discussion'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'hacker': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'discussions'", 'to': u"orm['core.Hacker']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Untitled Discussion'", 'max_length': '255'})
        },
        u'core.hacker': {
            'Meta': {'object_name': 'Hacker'},
            'batch': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'blog': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'branch': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'github_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'profile_image_url': ('django.db.models.fields.CharField', [], {'default': "'/static/core/img/placeholder_hacker.png'", 'max_length': '255'}),
            'roll_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'thumbnail_url': ('django.db.models.fields.CharField', [], {'default': "'/static/core/img/placeholder_hacker.png'", 'max_length': '255'}),
            'twitter_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'hacker'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'core.proposal': {
            'Meta': {'object_name': 'Proposal'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'proposer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'proposals'", 'to': u"orm['core.Hacker']"}),
            'repo_url': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'upvotes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'upvoters'", 'blank': 'True', 'to': u"orm['core.Hacker']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        }
    }

    complete_apps = ['core']