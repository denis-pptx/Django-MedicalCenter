from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name="website/home.html"), name='home'),
    path('about/', TemplateView.as_view(template_name="website/about.html"), name='about'),
    path('faq/', TemplateView.as_view(template_name="website/faq.html"), name='faq'),
    path('private-policy/', TemplateView.as_view(template_name="website/private-policy.html"), name='private-policy'),
    path('weather/', get_weather, name='weather'),
    path('gender/', get_gender, name='gender'),
]
