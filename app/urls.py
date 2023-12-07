from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('private/', views.private, name="private"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('analysis/', views.analysis, name="analysis"),
    path('signup/', views.signup, name="signUp"),
     path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]