from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', TemplateView.as_view(template_name="website/about.html"), name='about'),
    path('faq/', TemplateView.as_view(template_name="website/faq.html"), name='faq'),
    path('private-policy/', TemplateView.as_view(template_name="website/private-policy.html"), name='private-policy'),
    path('promo-codes/', TemplateView.as_view(template_name="website/promo-codes.html"), name='promo-codes'),
    path('feedback-list', feedback_list, name='feedback-list'),
    path('weather/', get_weather, name='weather'),
    path('gender/', get_gender, name='gender'),
]


