from django.shortcuts import render, get_object_or_404, resolve_url
from .models import Product
from orders.forms import OrderForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from static_pages.models import Work
from django.views.generic.base import TemplateView


def home(request):
    products = Product.objects.all()
    works = Work.objects.all()
    form = OrderForm(request.POST or None,)

    return render(request, "stock/home.html", {"products": products, "works": works, "form": form,
                                               "sended": request.GET.get("sended", False)})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    form = OrderForm(request.POST or None, initial={
        "product": product
    })

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("{}?sended=true".format(reverse("product", kwargs={"product_id": product_id})))

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

