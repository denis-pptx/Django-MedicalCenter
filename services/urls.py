from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
]
