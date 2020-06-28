# Generated by Django 3.0.3 on 2020-06-27 20:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wizer', '0029_lap_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sport',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
