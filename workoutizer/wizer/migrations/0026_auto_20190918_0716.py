# Generated by Django 2.2.1 on 2019-09-18 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wizer', '0025_auto_20190916_0943'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TraceFiles',
        ),
        migrations.RemoveField(
            model_name='traces',
            name='center_lat',
        ),
        migrations.RemoveField(
            model_name='traces',
            name='center_lon',
        ),
        migrations.RemoveField(
            model_name='traces',
            name='zoom_level',
        ),
    ]
