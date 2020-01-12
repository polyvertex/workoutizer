# Generated by Django 2.2.5 on 2019-09-20 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizer', '0027_auto_20190918_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='number_of_days',
            field=models.IntegerField(choices=[(365, 365), (180, 180), (90, 90), (30, 30), (10, 10), (5, 5)], default=30),
        ),
        migrations.AlterField(
            model_name='sport',
            name='color',
            field=models.CharField(choices=[('#0000FF', '#0000FF'), ('#DC143C', '#DC143C')], max_length=24, verbose_name='Color:'),
        ),
    ]
