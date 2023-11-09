from django.urls import path, re_path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', home, name='home'),
    re_path(r'^about/$', TemplateView.as_view(template_name="website/about.html"), name='about'),
    re_path(r'^faq/$', TemplateView.as_view(template_name="website/faq.html"), name='faq'),
    path('private-policy/', TemplateView.as_view(template_name="website/private-policy.html"), name='private-policy'),
    path('vacancies/', TemplateView.as_view(template_name="website/vacancies.html"), name='vacancies'),
    path('task/', TemplateView.as_view(template_name="website/task.html"), name='task'),
    path('classes/', TemplateView.as_view(template_name="website/classes.html"), name='classes'),
    path('feedback-list', feedback_list, name='feedback-list'),
    path('weather/', get_weather, name='weather'),
    path('gender/', get_gender, name='gender'),
    path('table/', TemplateView.as_view(template_name="website/magic-table.html"), name='magic-table'),
]


