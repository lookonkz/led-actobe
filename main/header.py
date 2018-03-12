from static_pages.models import Page
from django import template
register = template.Library()


@register.inclusion_tag('includes/header.html')
def menu(request):
    pages = Page.objects.all()
    return {
        "pages": pages,
    }
