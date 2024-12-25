from django.contrib import admin
from . models import Song, Watchlater, History

# Модели Базы Данных

admin.site.register(Song)
admin.site.register(Watchlater)
admin.site.register(History)