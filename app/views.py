from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import soundfile

#@login_required
def private(request):
    return render(request, "private.html")

#@login_required
def analysis(request):
    if request.method == "GET":
        return render(request, "analysis.html")
    
    elif request.method == "POST":
        file = request.FILES
        url = request.POST.get("url")
        vocal = request.POST.get("vocal")
        separate = request.POST.get("separate")
        soundfile.write(file='test.wav', data=file ,samplerate=14400)

    return render(request, "analysis.html")

def signUp(request):
    return render(request, "signUp.html")

def home(request):
    return render(request, "home.html")

