
from asistenciaAPP import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('home/', views.home )
]
