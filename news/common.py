import os


def get_path_to_html(news):
    publish_date = news.publish_date
    return os.path.join(
        'news',
        'news_archive',
        str(publish_date.year),
        str(publish_date.month).zfill(2),
        str(publish_date.day).zfill(2),
        f'{news.pk}.html'
    )


html_template = \
    '''
{% extends 'base.html' %}
{% load static %}

{% block title %}КДС | {{ news.title }}{% endblock %}

{% block styles %}
    <link rel="stylesheet" href="{% static 'news/css/news_details.css' %}">
{% endblock %}

{% block content %}
    <h1>{{ news.title }}</h1>
    <hr>
    <div class="image-paragraph-container">
        {% if news.image %}
            <img src="{{ news.image.url }}">
        {% endif %}
        <div class="paragraph-container">
            <p>{{ news.summary }}</p>
        </div>
    </div>
{% endblock %}
'''
