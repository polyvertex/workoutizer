# Generated by Django 2.2.1 on 2019-09-14 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wizer', '0016_auto_20190914_0641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='traces',
            old_name='coordinates',
            new_name='geometry',
        ),
    ]
