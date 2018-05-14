# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-14 00:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center', models.CharField(max_length=150)),
                ('center_search_status', models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], max_length=10)),
                ('facility', models.CharField(max_length=200)),
                ('status', models.CharField(default='Inactive', max_length=50)),
                ('facility_url', models.URLField(blank=True, null=True)),
                ('url_link', models.URLField(blank=True, null=True)),
                ('occupied', models.DateTimeField(blank=True, null=True)),
                ('record_date', models.DateTimeField(null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=150)),
                ('phone', models.CharField(blank=True, max_length=25)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('zipcode', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'facility',
                'verbose_name_plural': 'facilities',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Point', 'Point')], default='Point', max_length=10)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
            options={
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
            },
        ),
        migrations.AddField(
            model_name='facility',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facilities.Location'),
        ),
        migrations.AlterUniqueTogether(
            name='facility',
            unique_together=set([('center', 'facility')]),
        ),
    ]