from django.urls import path

from .views import *

urlpatterns = [
    path('planned_visits/', planned_visits, name='planned_visits'),
]
