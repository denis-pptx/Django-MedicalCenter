from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('doctors_list/', doctors, name='doctors_list'),
]
