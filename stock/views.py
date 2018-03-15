from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ContactForm
from orders.forms import OrderForm
from django.http import HttpResponseRedirect
from static_pages.models import Work
import telebot


def home(request):
    products = Product.objects.all()
    works = Work.objects.all()
    form = ContactForm(request.POST)
    form1 = OrderForm(request.POST)

    if request.method == "POST":
        bot = telebot.TeleBot('465058783:AAEJz6kcmZaVx0QPJrt7YGj-3wNXtBzOiXM')
        chat_id = '-223188240'

        if form.is_valid():
            text = 'Заявка на консультацию' '\n' + 'имя: ' + request.POST.get('name') + '\n' + 'телфон: ' + request.POST.get('telephone') + ''
            form.save()
            return HttpResponseRedirect("?sended=true", bot.send_message(chat_id, text))
        elif form1.is_valid():
            product = get_object_or_404(Product, pk=request.POST.get('product'))
            text = 'Заявка на товар' '\n' + 'имя: ' + request.POST.get('name') + '\n' + 'телфон: ' \
                   + request.POST.get('phone') + '\n' + 'товар: ' + product.name
            form1.save()
            return HttpResponseRedirect("?sended=true", bot.send_message(chat_id, text))
        else:
            print(form.errors)

    return render(request, "stock/home.html", {
        "products": products, "works": works,
        "form": form, "form1": form1,
        "sended": request.GET.get("sended", False)})


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = OrderForm(request.POST)
    bot = telebot.TeleBot('465058783:AAEJz6kcmZaVx0QPJrt7YGj-3wNXtBzOiXM')
    chat_id = '-223188240'

    if request.method == "POST":
        if form.is_valid():
            text = 'Заявка на товар' '\n' + 'имя: ' + request.POST.get('name') + '\n' + 'телфон: ' \
                   + request.POST.get('phone') + '\n' + 'товар: ' + product.name
            form.save()
            return HttpResponseRedirect("?sended=true", bot.send_message(chat_id, text))

    return render(request, "stock/product__detail.html", {
        "product": product,
        "form": form,
        "sended": request.GET.get("sended", False)
    })


def contact(request):
    form = ContactForm(request.POST)
    bot = telebot.TeleBot('465058783:AAEJz6kcmZaVx0QPJrt7YGj-3wNXtBzOiXM')
    chat_id = '-223188240'

    if request.method == "POST":
        if form.is_valid():
            text = 'Заявка на консультацию' '\n' + 'имя: ' + request.POST.get(
                'name') + '\n' + 'телфон: ' + request.POST.get('telephone') + ''
            form.save()
            return HttpResponseRedirect("?sended=true", bot.send_message(chat_id, text))

    return render(request, "stock/contact.html", {
        "form": form,
        "sended": request.GET.get("sended", False)
    })


