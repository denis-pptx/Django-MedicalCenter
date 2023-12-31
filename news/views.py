from django.shortcuts import render, get_object_or_404
from .models import News

import logging
logger = logging.getLogger(__name__)


def news(request):
    logging.info('Displayed news')
    news_list = News.objects.order_by('-publish_date')
    return render(request, 'news/news.html', context={'news': news_list})


def news_details(request, pk):
    logging.info('Displayed news details')
    certain_news = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_details.html', context={'news': certain_news})
