from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Category, PromoCode
from services.models import Service
import json

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


@csrf_exempt
def check_promo_code(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        promo_code = data.get('promo_code')
        service_id = data.get('service_id')

        promo_code_obj = PromoCode.objects.filter(code=promo_code, service_id=service_id, isAvailable=True).first()

        if promo_code_obj:
            original_price = Service.objects.get(id=service_id).price
            new_price = original_price * (1 - promo_code_obj.discount / 100)

            data = {
                'valid': True,
                'discount': promo_code_obj.discount,
                'new_price': new_price
            }
        else:
            if not PromoCode.objects.filter(code=promo_code, isAvailable=True):
                data = {
                    'valid': False,
                    'message': 'Данного промокода не существует.'
                }
            else:
                data = {
                    'valid': False,
                    'message': 'Промокод не подходит под данную услугу.'
                }

        return JsonResponse(data)






