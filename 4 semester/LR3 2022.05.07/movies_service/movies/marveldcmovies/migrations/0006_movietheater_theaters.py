# Generated by Django 4.0.4 on 2022-05-16 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marveldcmovies', '0005_movietheater_visits_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='movietheater',
            name='theaters',
            field=models.ManyToManyField(to='marveldcmovies.movie'),
        ),
    ]
