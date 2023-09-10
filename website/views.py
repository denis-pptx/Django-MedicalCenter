from django.shortcuts import render
import requests
import datetime


def home(request):
    return render(request, 'website/home.html')


def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = '63026ab922acdc159af4d7d5c6adca54'
        # my: aed8fb007394a58f1b4ad89ee08fc49e
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return render(request, 'website/weather.html',
                          {'city': data['name'], 'weather': data['weather'][0]})
        else:
            error_message = f"Error: {response.status_code}"
            return render(request, 'website/weather.html',
                          {'city': city, 'error_message': error_message})

    return render(request, 'website/weather.html')


def get_gender(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        url = f'https://api.genderize.io/?name={name}'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return render(request, 'website/gender.html',
                          {'name': data['name'],
                           'gender': data['gender'],
                           'probability': int(data['probability'] * 100)})
        else:
            error_message = f"Error: {response.status_code}"
            return render(request, 'website/gender.html',
                          {'name': name, 'error_message': error_message})

    return render(request, 'website/gender.html')
