from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('product-list/', views.ProductListView.as_view(), name='product-list'),
    path('product/', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('faq/', views.FAQView.as_view(), name='faq'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
