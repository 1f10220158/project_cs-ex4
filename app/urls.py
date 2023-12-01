from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('private/', views.private, name="private"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('analysis/', views.analysis, name="analysis"),
    path('signUp/', views.signUp, name="signUp"),
]