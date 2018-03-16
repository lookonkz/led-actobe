from django.urls import path
from .views import PageDetail

app_name = 'static_pages'
urlpatterns = [
    path('page/<slug:slug>', PageDetail.as_view(), name='page'),

]
