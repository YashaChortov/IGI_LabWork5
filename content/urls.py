from django.urls import path
from . import views

app_name = 'content'

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news_view, name='news_list'),
    path('vacancies/', views.vacancies_list, name='vacancies_list'),
    path('reviews/', views.reviews_list, name='reviews_list'),
]
