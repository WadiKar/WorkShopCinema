# Generated by Django 3.2.16 on 2022-11-22 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movielist', '0002_auto_20221122_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
    ]
