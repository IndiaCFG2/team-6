from . import views
from django.urls import path,include


urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.signup, name = "signup"),
    path('', views.index, name="home"),
    path('profile/', views.profile, name = "profile"),
]
