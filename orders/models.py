from django.db import models
from stock.models import Product


# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE)
    name = models.CharField("имя", max_length=50)
    phone = models.CharField("телефон", max_length=50)
    date = models.DateTimeField("дата", auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['date']

    def __str__(self):
        return self.name
