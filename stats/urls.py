from django.urls import path

from .views import *

urlpatterns = [
    path('planned_visits/', planned_visits, name='planned_visits'),
    path('cost_summary/', cost_summary, name='cost_summary'),
    path('doctor_appointments/', doctor_appointments, name='doctor_appointments'),
    path('patients/', patients, name='patients'),
    path('services_and_sales/', services_and_sales, name='services_and_sales'),
    path('category_chart/', category_chart, name='category_chart'),
    path('', statistics, name='statistics')
]
