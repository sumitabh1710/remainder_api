from django.urls import path
from .views import create_remainder

urlpatterns = [
    path('create/', create_remainder, name='create_remainder'),
]
