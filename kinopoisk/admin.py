from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(modelAkter)
admin.site.register(modelDirektor)
admin.site.register(modelGenre)
# admin.site.register(modelOtziv)


class adminPodpiska(admin.ModelAdmin):
    list_display = ('name', 'prise')     # отобразить несколько колонок
admin.site.register(modelPodpiska, adminPodpiska)


class adminKino(admin.ModelAdmin):
    list_display = ('name', 'direktor', 'year', 'podpiska')
    fieldsets = [ # при заполнении делим на части
            ('О фильме', {'fields':('name', 'info', 'year', 'genre', 'country')}),
            ('Люди', {'fields': ('acter', 'direktor')}),
            ('Для сайта', {'fields': ('poster', 'rating', 'podpiska', 'file')})
    ]
admin.site.register(modelKino, adminKino)
# admin.site.registration(modelKino)

class adminOtziv(admin.ModelAdmin):
    list_display = ('user', 'film')     # отобразить несколько колонок
admin.site.register(modelOtziv, adminOtziv)
