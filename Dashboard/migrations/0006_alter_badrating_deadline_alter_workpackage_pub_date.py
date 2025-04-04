# Generated by Django 5.1.5 on 2025-01-29 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0005_alter_badrating_deadline_alter_workpackage_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badrating',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 29, 15, 56, 4, 475023), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='workpackage',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2025, 1, 29, 15, 56, 4, 474026), verbose_name='pub date'),
        ),
    ]
