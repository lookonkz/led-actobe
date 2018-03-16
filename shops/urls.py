"""shops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.utils.functional import curry
from django.views.defaults import server_error, page_not_found

handler404 = curry(page_not_found, template_name='errs/404.html')
handler500 = curry(server_error, template_name='errs/500.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stock.urls', namespace='stock')),
    path('', include('static_pages.urls', namespace='static_pages')),
    # path('cart/', include('cart.urls', namespace='cart')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


