# Generated by Django 5.1.5 on 2025-01-28 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workpackage',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 28, 17, 9, 37, 344766), verbose_name='pub date'),
        ),
    ]
