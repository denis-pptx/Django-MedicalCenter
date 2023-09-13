from django.urls import path, re_path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', home, name='home'),
    re_path(r'^about/$', TemplateView.as_view(template_name="website/about.html"), name='about'),
    re_path(r'^faq/$', TemplateView.as_view(template_name="website/faq.html"), name='faq'),
    path('private-policy/', TemplateView.as_view(template_name="website/private-policy.html"), name='private-policy'),
    re_path(r'^promo-codes/$', TemplateView.as_view(template_name="website/promo-codes.html"), name='promo-codes'),
    path('vacancies/', TemplateView.as_view(template_name="website/vacancies.html"), name='vacancies'),
    path('feedback-list', feedback_list, name='feedback-list'),
    path('weather/', get_weather, name='weather'),
    path('gender/', get_gender, name='gender'),
]


