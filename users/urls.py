from django.urls import path
from . import views
from .views import login_view

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', login_view, name='login'),
]
