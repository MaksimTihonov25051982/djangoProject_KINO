from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import modelPodpiska
from captcha.fields import CaptchaField

class formRegistr(UserCreationForm):
    username = forms.CharField(label='Login',
                               help_text='')
    password1 = forms.CharField(label='Пароль',
                                help_text='',
                                widget= forms.PasswordInput(
                                attrs= {'autocomplete':'new-passwotd'}
                                ))
    password2 = forms.CharField(label='Подтверждение',
                                help_text='',
                                widget=forms.PasswordInput(
                                attrs={'autocomplete': 'new-passwotd'}
                                ))
    email = forms.EmailField(label='Почта',
                                widget=forms.TextInput(
                                attrs={'placeholder':'qwe@mail.ru'}
                             ))
    first_name = forms.CharField(label='Имя',required=False)
    last_name = forms.CharField(label='Фамилия',required=False)
    captcha = CaptchaField()

class formPodpiska(forms.Form):
    item = forms.ModelChoiceField(modelPodpiska.objects.all(),
                                  label='Выберите')

class formOtsiv(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs= {
        'name':'text','rows':5, 'cols':50}),
        label='напишите отзыв.',
        min_length= 10)
    nerobot = forms.BooleanField(error_messages={'reguired': 'Вы робот'},
                                 label='Вы  не робот')