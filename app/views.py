from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def private(request):
    return render(request, "private.html")

@login_required
def analysis(request):
    return render(request, "analysis.html")

def signUp(request):
    return render(request, "signUp.html")

