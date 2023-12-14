from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages


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

def home(request):
    return render(request, "home.html")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')  # ログイン後のリダイレクト先を指定
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home') 

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            login(request, authenticate(username=username, password=request.POST['password1']))
            return redirect('home')  # サインアップ後のリダイレクト先を指定
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})