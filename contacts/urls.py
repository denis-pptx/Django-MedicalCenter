from django.urls import path
from .views import *

urlpatterns = [
    path('medical_centers/', medical_centers, name='medical_centers'),
]
