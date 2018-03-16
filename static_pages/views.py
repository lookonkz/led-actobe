from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Page
# Create your views here.


class PageDetail(DetailView):
    model = Page
    template_name = 'static_pages/page_detail.html'

