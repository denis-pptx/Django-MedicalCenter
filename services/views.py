from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView
from .models import Category, PromoCode

import logging
logger = logging.getLogger(__name__)


class CategoryListView(ListView):
    model = Category


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    subcategories = category.subcategory_set.all()

    context = {
        'category': category,
        'subcategories': subcategories,
    }

    logging.info('Displayed category details')
    return render(request, 'services/category_detail.html', context)

def promo_code_list(request):
    available_promo_codes = PromoCode.objects.filter(isAvailable=True)
    unavailable_promo_codes = PromoCode.objects.filter(isAvailable=False)
    return render(request, 'services/promo-codes.html', {
        'available_promo_codes': available_promo_codes,
        'unavailable_promo_codes': unavailable_promo_codes
    })