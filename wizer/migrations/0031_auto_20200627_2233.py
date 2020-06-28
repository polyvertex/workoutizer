# Generated by Django 3.0.3 on 2020-06-27 20:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wizer', '0030_auto_20200627_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sport',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='sport',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='sport',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 27, 20, 33, 11, 140694, tzinfo=utc), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sport',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 27, 20, 33, 21, 361756, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
