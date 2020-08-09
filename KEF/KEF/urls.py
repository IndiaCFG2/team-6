"""KEF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('', views.workshops, name = "workshops"),
    path('about/', views.about, name = "about"),
    path('contact/', views.contact, name = "contact"),
    path('schools/', include('schools.urls')),
    path('employees/',include('employees.urls')),
    path('employees/login/', auth_views.LoginView.as_view(template_name = 'employees/login.html'), name = 'login'),
    path('employees/logout/', auth_views.LogoutView.as_view(template_name = 'employees/logout.html'), name = 'logout'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
