from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', profile, name='doctor_profile'),
    path('doctors_list/', doctors, name='doctors_list'),
    path('schedule/', doctor_schedule, name='doctor_schedule'),
    path('schedule/create/', create_schedule, name='create_schedule'),
    path('schedule/delete/<int:pk>/', delete_schedule, name='delete_schedule'),
    path('schedule/update/<int:pk>/', update_schedule, name='update_schedule'),
    path('order_list/', order_list, name='doctor_order_list'),
    path('complete_order/<int:order_id>/', complete_order, name='complete_order'),
]
