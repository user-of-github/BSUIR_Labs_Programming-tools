# Generated by Django 4.0.4 on 2022-05-23 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marveldcmovies', '0013_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]