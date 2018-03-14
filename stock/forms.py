from django import forms
from orders.models import ConatacForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = ConatacForm
        fields = ['name', 'telephone']
