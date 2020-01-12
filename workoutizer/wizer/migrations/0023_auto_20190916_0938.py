# Generated by Django 2.2.1 on 2019-09-16 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizer', '0022_auto_20190916_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='gpx_checker_interval',
            field=models.IntegerField(verbose_name='GPX File Checker Time Interval:'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='path_to_trace_dir',
            field=models.CharField(max_length=120, verbose_name='Path to GPX Files Directory:'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='trace_opacity',
            field=models.FloatField(default=0.7, max_length=20, verbose_name='Opacity of Trace:'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='trace_width',
            field=models.FloatField(default=3.0, max_length=20, verbose_name='Width of Trace:'),
        ),
    ]
