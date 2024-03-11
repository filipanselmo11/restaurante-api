from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRestaurantes),
    path('<str:pk>', views.getRestaurante)
]