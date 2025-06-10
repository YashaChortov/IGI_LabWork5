from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'main'

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('orders/', views.order_list, name='order_list'),
    path('clients/', views.client_list, name='client_list'),
    path('faq/', views.faq_list, name='faq_list'),
    path('contacts/', views.contact_list, name='contact_list'),
]
