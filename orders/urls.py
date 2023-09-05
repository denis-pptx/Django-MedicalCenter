from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('select_doctor/<int:service_id>/', select_doctor, name='select_doctor'),
    path('select_doctor_date/', select_doctor_date, name='select_doctor_date'),
    path('create_order/', create_order, name='create_order')
]
