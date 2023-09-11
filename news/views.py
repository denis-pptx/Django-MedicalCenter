from django.shortcuts import render, get_object_or_404
from .models import News
from news.common import get_path_to_html


def news(request):
    return render(request, 'news/news.html', context={'news': News.objects.all()})


def news_details(request, pk):
    certain_news = get_object_or_404(News, pk=pk)
    return render(request, get_path_to_html(certain_news), context={'news': news})
