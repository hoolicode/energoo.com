from django.shortcuts import render
from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'shop/home.j2'


class ProductListView(generic.TemplateView):
    template_name = 'shop/product-list.j2'


class ProductDetailView(generic.TemplateView):
    template_name = 'shop/product-detail.j2'


class CartView(generic.TemplateView):
    template_name = 'shop/cart.j2'


class FAQView(generic.TemplateView):
    template_name = 'shop/faq.j2'


class ContactView(generic.TemplateView):
    template_name = 'shop/contact.j2'