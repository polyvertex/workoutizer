# Generated by Django 2.2.5 on 2019-09-24 20:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizer', '0037_activity_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='time',
        ),
        migrations.AddField(
            model_name='activity',
            name='dur2',
            field=models.DurationField(default=datetime.timedelta(seconds=1800), verbose_name='dur2:'),
            preserve_default=False,
        ),
    ]
