# Generated by Django 4.0.4 on 2022-05-08 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('movie_id', models.UUIDField()),
                ('date_from', models.DateField(auto_now=True)),
                ('date_to', models.DateField(auto_now=True)),
                ('rating', models.SmallIntegerField()),
                ('poster_image_link', models.CharField(max_length=500)),
                ('duration', models.SmallIntegerField()),
                ('age_restriction', models.SmallIntegerField()),
            ],
        ),
    ]
