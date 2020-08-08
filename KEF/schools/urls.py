from . import views
from django.urls import path,include

urlpatterns = [
    path('s_login/', views.login, name="login"),
    path('', views.index, name="index"),
]
