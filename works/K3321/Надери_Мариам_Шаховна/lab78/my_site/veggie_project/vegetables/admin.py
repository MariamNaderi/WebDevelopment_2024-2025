from django.contrib import admin
from .models import Vegetable  # Импортируем модель

# Регистрируем модель для отображения в админке
admin.site.register(Vegetable)