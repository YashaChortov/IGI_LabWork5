from django.shortcuts import render
from .models import Product, Order, Client, Contact, FAQ


def product_list(request):
    products = Product.objects.all()
    return render(request, 'main/product_list.html', {'products': products})

def order_list(request):
    orders = Order.objects.select_related('client', 'product').all()
    return render(request, 'main/order_list.html', {'orders': orders})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'main/client_list.html', {'clients': clients})

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'main/contact_list.html', {'contacts': contacts})

def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'main/faq_list.html', {'faqs': faqs})
