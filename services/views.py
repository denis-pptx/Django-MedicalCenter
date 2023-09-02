from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView
from .models import Category


class CategoryListView(ListView):
    model = Category


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    subcategories = category.subcategory_set.all()

    context = {
        'category': category,
        'subcategories': subcategories,
    }
    return render(request, 'services/category_detail.html', context)
