from django.urls import path
from .views import PageDetail
from django.views.generic.base import TemplateView

app_name = 'static_pages'
urlpatterns = [
    path('page/<slug:slug>', PageDetail.as_view(), name='page'),
    path('politic/', TemplateView.as_view(template_name='static_pages/politic.html'), name='politic'),

]
