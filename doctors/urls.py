from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('profile/', profile, name='doctor_profile'),
    path('doctors_list/', doctors, name='doctors_list'),
    path('schedule/', doctor_schedule, name='doctor_schedule'),
    path('schedule/create/', create_schedule, name='create_schedule'),
    re_path(r'^schedule/delete/(?P<pk>\d+)/$', delete_schedule, name='delete_schedule'),
    re_path(r'^schedule/update/(?P<pk>\d+)/$', update_schedule, name='update_schedule'),
    re_path(r'^order_list/$', order_list, name='doctor_order_list'),
    re_path(r'^complete_order/(?P<order_id>\d+)/$', complete_order, name='complete_order'),
]
