# Generated by Django 2.2.5 on 2019-09-25 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizer', '0042_remove_activity_duration_old'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(default='unknown', max_length=50, verbose_name='Activity Name:'),
        ),
    ]
