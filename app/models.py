from django.db import models
from django.utils import timezone

class Analysis(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    datetime = models.DateTimeField(default= timezone.now)
    vocal_path = models.CharField(max_length=255)
    no_vocal_path = models.CharField(max_length=255)
    bass_path = models.CharField(max_length=255)
    drum_path = models.CharField(max_length=255)
    other_path = models.CharField(max_length=255)
    youtube_url = models.CharField(max_length=255)
    music_path = models.FileField(upload_to='music/')
    music_key = models.CharField(max_length=20)
    music_title = models.CharField(max_length=255)
    vocal_range = models.CharField(max_length=10)
