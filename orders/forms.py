from django import forms
from .models import Order
from stock.models import Product


class OrderForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Order
        fields = ["product", "name", "phone"]


class OrderForm1(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Order
        fields = ["product", "name", "phone"]
