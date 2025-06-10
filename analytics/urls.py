from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('sales/', views.sales_report, name='sales_report'),
    path('product-popularity/', views.product_popularity, name='product_popularity'),
    path('client-stats/', views.client_statistics, name='client_statistics'),
]
