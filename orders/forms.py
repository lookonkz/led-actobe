from django import forms
from .models import Order
from stock.models import Product


class OrderForm(forms.ModelForm):
    house = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Order
        fields = ["product", "name", "phone"]
