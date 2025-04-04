# Generated by Django 5.1.5 on 2025-01-29 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_alter_workpackage_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='workpackage',
            name='WP_ID',
            field=models.CharField(default='-', max_length=150),
        ),
        migrations.AlterField(
            model_name='badrating',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 29, 15, 47, 40, 588968), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='workpackage',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 29, 15, 47, 40, 588968), verbose_name='pub date'),
        ),
    ]
