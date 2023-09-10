from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('weather/', get_weather, name='weather'),
    path('gender/', get_gender, name='gender'),
]
