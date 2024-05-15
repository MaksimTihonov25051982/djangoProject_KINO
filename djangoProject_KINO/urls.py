"""
URL configuration for djangoProject_KINO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from kinopoisk import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='home'),

    path('kino/',views.kinoList.as_view(), name='allkino'),
    path('kino/otzuv/<int:kinoid>/', views.otziv, name='otziv'),
    path('kino/<str:genre>/<slug:pk>/', views.kinoDetal.as_view(), name='onekino'),

    path('akter/',views.akterList.as_view(), name='allakters'),
    path('akter/<slug:pk>/', views.akterDetal.as_view(), name='oneakter'),

    path('direktor/',views.direktorList.as_view(), name='alldirektor'),
    path('direktor/<slug:pk>/', views.direktorDetal.as_view(), name='onedirektor'),


    path('auth/', include('django.contrib.auth.urls')),
                        # Регистрация
    path('auth/registration',views.registr, name= 'registr'),
    path('accounts/login/', views.index),

    path('auth/profile/', views.profile, name='kabinet'),
    path('auth/profile/change', views.profileChange, name='kabinetChange'),

    path('captcha/', include('captcha.urls')),

]

'''
    сброс пароля
    reset-password
    reset-done
    change-password
    change-done
    home   
'''
