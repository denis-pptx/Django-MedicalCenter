from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name="website/home.html"), name='home'),
    path('weather/', get_weather, name='weather'),
    path('gender/', get_gender, name='gender'),
]
