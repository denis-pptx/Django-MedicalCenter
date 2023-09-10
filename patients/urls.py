from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', profile, name='patient_profile'),
    path('register/', register, name='register'),
    path('order_list/', order_list, name='patient_order_list'),
    path('cancel_order/<int:order_id>/', cancel_order, name='cancel_order'),
]
