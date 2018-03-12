from django.urls import path
from .views import home, product_detail, contact

app_name = 'stock'
urlpatterns = [
    path('', home, name='home'),
    path('produc/<int:pk>', product_detail, name='prodict'),
    path('contact/', contact, name='contact'),
]