# Generated by Django 2.2.5 on 2019-09-25 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wizer', '0041_auto_20190925_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='duration_old',
        ),
    ]
