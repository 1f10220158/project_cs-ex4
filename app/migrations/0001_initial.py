# Generated by Django 4.2.8 on 2023-12-16 07:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('vocal_path', models.FileField(upload_to='vocal/')),
                ('no_vocal_path', models.FileField(upload_to='no_vocal/')),
                ('bass_path', models.FileField(upload_to='bass/')),
                ('drum_path', models.FileField(upload_to='drum/')),
                ('other_path', models.FileField(upload_to='other/')),
                ('youtube_url', models.CharField(max_length=255)),
                ('music_path', models.FileField(upload_to='music/')),
                ('music_key', models.CharField(max_length=2)),
                ('music_title', models.CharField(max_length=255)),
                ('vocal_range', models.CharField(max_length=7)),
            ],
        ),
    ]