# Generated by Django 2.0.2 on 2018-05-31 22:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180601_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komentarz',
            name='data_utworzenia',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 31, 22, 7, 35, 960954, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='data_utworzenia',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 31, 22, 7, 35, 960954, tzinfo=utc)),
        ),
    ]
