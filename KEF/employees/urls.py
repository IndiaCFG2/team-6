from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('register/', views.signup, name = "signup"),
    path('courses/', views.course, name = "course"),
    path('teachers/', views.tcher, name = "tcher"),
]
