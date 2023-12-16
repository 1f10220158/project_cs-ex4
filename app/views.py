from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import *

from app.assist_analysis.pitch_finder import find_pitch
from app.assist_analysis.key_finder import Tonal_Fragment
import librosa
from yt_dlp import YoutubeDL
import demucs.separate
import re

#@login_required
def private(request):
    return render(request, "private.html")

#@login_required
def analysis(request):
    if request.method == "GET":
        return render(request, "analysis.html")
    
    elif request.method == "POST":
        sound_file = request.FILES.get("soundfile")
        url = request.POST.get("url")
        vocal = request.POST.get("vocal")
        separate = request.POST.get("separate")

        #ファイルを入力した場合
        if sound_file:

            analysis = Analysis(
                music_path = sound_file,
            )
            analysis.save()

            audio_name = sound_file.name
            audio_name_without_extension = re.sub('.\s+', '', audio_name)
            title = audio_name_without_extension
            audio_path = "media/music/{}".format(audio_name)
        
        #youtube-urlを入力した場合
        else:

            #urlから音声をダウンロード
            opts = {
                'outtmpl': 'media/music/%(id)s.mp3',
                'format': 'bestaudio'
            }

            with YoutubeDL(opts) as ydl:
                res = ydl.extract_info(url)

            title = res["title"]
            audio_name_without_extension = res["id"]
            audio_path = "media/music/{}.mp3".format(res["id"])
        
        #音声ファイル読み込み
        y, sr = librosa.load(audio_path)

        #bpm推定
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr) 

        #キー推定
        y_harmonic, y_percussive = librosa.effects.hpss(y)
        key_obj = Tonal_Fragment(y_harmonic, sr, tend=22)
        key = max(key_obj.key_dict, key=key_obj.key_dict.get)
        if key_obj.altkey is not None:
            key = "{} also possible {}".format(key, key_obj.altkey)

        vocal_options = [
                audio_path,
                "-n", "htdemucs",
                "-o", "media",
                "--mp3",
                ]

        #ボーカルがある場合
        if vocal == "1":

            #ボーカルがあって楽器別に分ない場合
            if separate == "0":
                vocal_options += ["--two-stems", "vocals"]

            #音声分離
            #demucs.separate.main(vocal_options)
            separated_path = "media/htdemucs/{}/{}"

            #ボーカルの音域推定
            vocal_audio_path = separated_path.format(audio_name_without_extension, "vocals.mp3")
            vocal_range = find_pitch(vocal_audio_path, vocal_audio_path)


        #ボーカルがなく楽器別に分ける場合
        else:

            #音声分離
            #demucs.separate.main(vocal_options)
            separated_path = "media/htdemucs/{}/{}"

        if url:
            analysis = Analysis()
            analysis.music_path = audio_path
            analysis.youtube_url = url

        if vocal == "1":
            analysis.vocal_path = vocal_audio_path
            analysis.vocal_range = vocal_range

            if separate == "0":
                analysis.no_vocal_path = separated_path.format(audio_name_without_extension, "no_vocals.mp3")
            else:
                analysis.bass_path = separated_path.format(audio_name_without_extension, "bass.mp3")
                analysis.drum_path = separated_path.format(audio_name_without_extension, "drum.mp3")
                analysis.other_path = separated_path.format(audio_name_without_extension, "other.mp3")

        else:
            if separate == "0":
                analysis.no_vocal_path = separated_path.format(audio_name_without_extension, "no_vocals.mp3")
            else:
                analysis.bass_path = separated_path.format(audio_name_without_extension, "bass.mp3")
                analysis.drum_path = separated_path.format(audio_name_without_extension, "drum.mp3")
                analysis.other_path = separated_path.format(audio_name_without_extension, "other.mp3")

        analysis.music_key = key
        analysis.music_title = title
        analysis.save()

        """
        モデルに保存されるデータ

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
        """
        context = {"vocal_range": {
            "vocal_path": analysis.vocal_path,
            "bass_path": analysis.bass_path,
            "vocal_range": vocal_range
        }}

    return render(request, "analysis.html", context)

def signUp(request):
    return render(request, "signUp.html")

def home(request):
    return render(request, "home.html")

