from django.urls import path
from .views import home, product_detail, contact

app_name = 'stock'
urlpatterns = [
    path('', home, name='home'),
    path('produc/<int:product_id>', product_detail, name='prodict_detail'),
    path('contact/', contact, name='contact'),
]
