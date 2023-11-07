from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('promo-codes/', promo_code_list, name='promo-codes'),
    path('check-promo-code/', check_promo_code, name='check-promo-code')
]
