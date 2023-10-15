from django.urls import path
from .views import *

urlpatterns = [
    path('', news, name='news'),
    path('details/<int:pk>/', news_details, name='news_details'),
]
