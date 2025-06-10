from django.contrib.sites import requests
from django.shortcuts import render
import random
from django.utils.dateparse import parse_datetime

from .models import News, Vacancy, Review
import requests
from requests.exceptions import RequestException

def home(request):
    return render(request, 'content/home.html')

def news_list(request):
    news = News.objects.order_by('-published_at')
    return render(request, 'content/news_list.html', {'news_list': news})

def vacancies_list(request):
    vacancies = Vacancy.objects.order_by('-published_at')
    return render(request, 'content/vacancies_list.html', {'vacancies': vacancies})

def reviews_list(request):
    reviews = Review.objects.filter(approved=True).order_by('-created_at')
    return render(request, 'content/reviews_list.html', {'reviews': reviews})

def news_list(request):
    news = News.objects.all()

    # Получаем случайный факт о кошках
    cat_fact = None
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        if response.status_code == 200:
            cat_fact = response.json().get("fact")
    except requests.RequestException:
        cat_fact = "Не удалось получить факт о кошке."

    return render(request, 'content/news_list.html', {
        'news': news,
        'cat_fact': cat_fact
    })


def fetch_news(request):
    api_key = "9658ea7e12b944618b3f5569269cb600"
    url = f"https://newsapi.org/v2/everything?q=cryptocurrency&apiKey={api_key}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        count = 0
        for article in data.get('articles', []):
            if count >= 5:
                break

            News.objects.get_or_create(
                title=article.get('title'),
                defaults={
                    'description': article.get('description', '')[:1000],
                    'url': article.get('url'),
                    'published_at': parse_datetime(article.get('publishedAt')),
                    'image_url': article.get('urlToImage')
                }
            )
            count += 1

        news_list = News.objects.all().order_by('-published_at')
        return render(request, 'content/news_list.html', {'news_list': news_list})

    except RequestException as e:
        return render(request, 'content/news_list.html', {'news_list': [], 'error': str(e)})


import requests
from django.shortcuts import render

def news_view(request):
    news_list: list = []
    news_list_new: list = []
    error = None
    cat_fact = None

    # Получаем факт о кошках
    try:
        cat_response = requests.get('https://catfact.ninja/fact')
        if cat_response.status_code == 200:
            cat_fact = cat_response.json().get('fact')
    except requests.RequestException:
        cat_fact = 'Не удалось загрузить факт о кошках'

    # Загружаем новости
    try:
        response = requests.get(
            'https://newsapi.org/v2/everything',
            params={
                'q': 'cryptocurrency',
                'apiKey': '9658ea7e12b944618b3f5569269cb600',
                'pageSize': 50
            }
        )
        if response.status_code == 200:
            data = response.json()
            news_list = data.get('articles', [])
            if len(news_list) > 5:
                news_list_new = random.sample(news_list, 5)
        else:
            error = 'Ошибка загрузки новостей'
    except requests.RequestException:
        error = 'Ошибка соединения с API новостей'

    return render(request, 'content/news_list.html', {
        'news_list': news_list_new,
        'error': error,
        'cat_fact': cat_fact
    })
