

from django.shortcuts import render, redirect
from .models import *
import random

# Create your views here.
def index(reguest):
    film = modelKino.objects.all() # собрали все объекты кино
    acter = modelAkter.objects.all()
    randomFilm = random.choice(film)
    data = {'film': film, 'acter': acter, 'random': randomFilm}
    return render(reguest, 'index.html', data)

# Занятие 2
from django.views import generic # Генерирует список всех фильмов
class kinoList(generic.ListView):
    model = modelKino
    paginate_by = 3
class kinoDetal(generic.DeleteView):
    model = modelKino



class akterList(generic.ListView):
    model = modelAkter
    paginate_by = 3

class akterDetal(generic.DeleteView):
    model = modelAkter



class direktorList(generic.ListView):
    model = modelDirektor
    paginate_by = 3

class direktorDetal(generic.DeleteView):
    model = modelDirektor




                       ############# <<< РЕГИСТРАЦИЯ >>> #############
from  django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import authenticate, login
from  django.contrib.auth.models import User


def registr(reguest):
    # forma = UserCreationForm()
    # print(1)
    if reguest.POST:
        print(2)
        forma = formRegistr(reguest.POST) # форма регистрации
        if forma.is_valid():              # проверка пройдена
            print(3)
            # собираем данные
            k1 = forma.cleaned_data.get('username')
            k2 = forma.cleaned_data.get('password')
            k3 = forma.cleaned_data.get('email')
            k4 = forma.cleaned_data.get('last_name')
            k5 = forma.cleaned_data.get('first_name')

            User.objects.create_user(username=k1, password=k2)  # новая строка, пользователь
            user1 = authenticate(username=k1, password=k2)
            user =  User.objects.get(username=k1) # находим пользователя
            # заполняем про него данные
            user.email = k3
            user.last_name = k4
            user.first_name = k5
            user.save()    # сохраняем
            modelProfile.objects.create(balanse=1000, podpiska_id=1, user_id=user.id) #привяжет профиль пользователя
            login(reguest, user) # вход пользователя на сайт
            return redirect('home') # перемещаемся на главную страницу
    else:
        forma = formRegistr()
    data = {'form':forma}
    return render(reguest,'registration/registration.html', data)

def profile(reguest):
    return render(reguest,'kabinet.html')

def profileChange(reguest):
    forma = formPodpiska
    data = {'form':forma}
    if reguest.POST:
        k1 = reguest.POST.get('item')
        user = User.objects.get(id=reguest.user.id)
        user.modelprofile.podpiska_id= k1
        user.modelprofile.save()
        return  redirect('kabinet')
    return render(reguest,'kabinet.html', data)

# def otziv(reguest):
#     if reguest.POST:
#         k1 = reguest.user.username
#         k2 = reguest.POST.get('text')
#         print(k1, k2)
#         return redirect('home')

def otziv(reguest, kinoid):
    print(1)
    print(kinoid)
    if reguest.POST:     # загружается форма отзыва
        k1 = reguest.POST.get('text')
        k2 = reguest.user.id # Кто написал отзыв.
        k3 = reguest.user.username
        print(k1, k2, k3)
        film = modelKino.objects.get(id=kinoid) # находим фильм
        modelOtziv.objects.create(text=k1, user_id=k2, film_id=kinoid) # записываем отзыв в таблицу
        return redirect('onekino', film.genre, film.id) # обнавляем ту же страницу фильма
    return redirect('home')