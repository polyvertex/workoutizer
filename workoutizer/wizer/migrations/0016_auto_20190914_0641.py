# Generated by Django 2.2.1 on 2019-09-14 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wizer', '0015_traces'),
    ]

    operations = [
        migrations.RenameField(
            model_name='traces',
            old_name='geometry',
            new_name='coordinates',
        ),
    ]
