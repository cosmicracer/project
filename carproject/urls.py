"""
URL configuration for carproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from cars import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.firstpage, name="firstpage"),
    path('carrestore',views.carrestore, name="carrestore"),
    path('carpaint',views.carpaint, name="carpaint"),
    path('carsale1',views.carsale1, name="carsale1"),
    path('carsale2',views.carsale2, name="carsale2"),
    path('carsale3',views.carsale3, name="carsale3"),
    path('carsale4',views.carsale4, name="carsale4"),
    path('carsale5',views.carsale5, name="carsale5"),
    path('carsale6',views.carsale6, name="carsale6"),
    path('addData',views.addData, name="addData"),
    path('add',views.add, name="add"),
    path('sale',views.sale, name="sale"),
]
