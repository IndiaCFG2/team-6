from . import views
from django.urls import path,include


urlpatterns = [
    path('s_login/', views.login, name="login"),
    path('', views.index, name="index"),
    path('/profile', views.profile, name="profile"),
    path('/about',views.about,name="about"),
    path('/contact', views.contact, name="contact"),
    path('/main', views.index, name="index"),
    # path('/course',views.course,name="course"),
]
