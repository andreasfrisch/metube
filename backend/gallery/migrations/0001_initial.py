# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to=b'images')),
            ],
        ),
    ]
