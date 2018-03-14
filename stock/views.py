from django.shortcuts import render, get_object_or_404, resolve_url
from .models import Product
from .forms import ContactForm
from orders.forms import OrderForm, OrderForm1
from django.http import HttpResponseRedirect
from django.urls import reverse
from static_pages.models import Work
from django.views.generic.base import TemplateView
from django.views.decorators.http import require_http_methods


def home(request):
    products = Product.objects.all()
    works = Work.objects.all()
    form = ContactForm(request.POST)
    form1 = OrderForm(request.POST)

    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            print('hello')
            form = ContactForm(request.POST)
            form.save()
            return HttpResponseRedirect("?sended=true")
        elif form1.is_valid():
            form1.save()
            return HttpResponseRedirect("?sended=true")
        else:
            print(form.errors)

    return render(request, "stock/home.html", {
        "products": products, "works": works,
        "form": form, "form1": form1,
        "sended": request.GET.get("sended", False)})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = OrderForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            print('прошло')
            form.save()
            return HttpResponseRedirect("?sended=true")

    return render(request, "stock/product__detail.html", {
        "product": product,
        "form": form,
        "sended": request.GET.get("sended", False)
    })


def contact(request):
    form = OrderForm

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("{}?sended=true")

    return render(request, "stock/contact.html", {
        "form": form,
        "sended": request.GET.get("sended", False)
    })


