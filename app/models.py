from django.db import models
from django.utils import timezone

class Analysis(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    datetime = models.DateTimeField(default= timezone.now)
    vocal_path = models.FileField(upload_to='vocal/')
    no_vocal_path = models.FileField(upload_to='no_vocal/')
    bass_path = models.FileField(upload_to='bass/')
    drum_path = models.FileField(upload_to='drum/')
    other_path = models.FileField(upload_to='other/')
    youtube_url = models.CharField(max_length=255)
    music_path = models.FileField(upload_to='music/')
    music_key = models.CharField(max_length=2)
    music_title = models.CharField(max_length=255)
    vocal_range = models.CharField(max_length=7)

