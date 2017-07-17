# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 03:05
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('content', models.TextField(null=True)),
                ('views', models.IntegerField(default=0)),
                ('link', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('api_name', models.CharField(choices=[('ph', 'Porn Hub'), ('rb', 'Red Tube'), ('t8', 'Tube8'), ('yp', 'YouPorn'), ('xt', 'XTube'), ('sw', 'Sparn Wire')], max_length=255, null=True)),
                ('data_json', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(null=True, to='app.Category')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_post_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Static_Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_page', models.CharField(choices=[('dmca', 'DMCA'), ('2257', '2257')], default='dmca', max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_tag_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_tag_updated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(null=True, to='app.Tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_post_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='demo',
            name='post',
            field=models.ManyToManyField(to='app.Post'),
        ),
    ]
