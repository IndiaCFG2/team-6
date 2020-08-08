from . import views
from django.urls import path,include


urlpatterns = [
    path('s_login/', views.login, name="login"),
    path('', views.index, name="index"),
    path('/profile', views.profile, name="profile"),
   
    path('/main', views.index, name="index"),
    # path('/course',views.course,name="course"),
]
