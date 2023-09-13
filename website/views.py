from django.shortcuts import render
import requests
from news.models import News
from patients.models import Feedback

import logging
logger = logging.getLogger(__name__)


def feedback_list(request):
    logger.info("A list of reviews is displayed")
    feedbacks = Feedback.objects.all().order_by('-date')
    return render(request, 'website/feedback-list.html', {'feedbacks': feedbacks})


def home(request):
    logger.info("The main page is opened")
    last_news = News.objects.all().order_by('-publish_date').first()
    return render(request, 'website/home.html', context={'last_news': last_news})


def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = '63026ab922acdc159af4d7d5c6adca54'
        # my: aed8fb007394a58f1b4ad89ee08fc49e
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        response = requests.get(url)

        if response.status_code == 200:
            logger.info("Weather API: code 200")
            data = response.json()
            return render(request, 'website/weather.html',
                          {'city': data['name'], 'weather': data['weather'][0]})
        else:
            logger.warning(f"Weather API: {response.status_code}")
            error_message = f"Error: {response.status_code}"
            return render(request, 'website/weather.html',
                          {'city': city, 'error_message': error_message})

    return render(request, 'website/weather.html')


def get_gender(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        url = f'https://api.genderize.io/?name={name}'

        response = requests.get(url)
        data = response.json()

        if not data['probability']:
            logger.warning(f"Gender API: data['probability'] is null")
            response.status_code = 400

        if response.status_code == 200:
            logger.info("Gender API: code 200")
            return render(request, 'website/gender.html',
                          {'name': data['name'],
                           'gender': data['gender'],
                           'probability': int(data['probability'] * 100)})
        else:
            logger.warning(f"Gender API: code {response.status_code}")
            error_message = f"Error: {response.status_code}"
            return render(request, 'website/gender.html',
                          {'name': name, 'error_message': error_message})

    return render(request, 'website/gender.html')
