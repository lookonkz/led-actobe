from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from easy_thumbnails.fields import ThumbnailerImageField
from django.utils.functional import cached_property
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Product(models.Model):
    name = models.CharField(verbose_name='наименование', max_length=200, default=None, blank=True)
    description = RichTextUploadingField(verbose_name='описание', default=None, blank=True)
    price = models.TextField(blank=True, default='', verbose_name='price')
    img = ThumbnailerImageField(verbose_name='фото', upload_to='product/photos')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']

    @cached_property
    def images(self):
        return self.photo_set.all()

    def __str__(self):
        return self.name


class Photo(models.Model):
    name_photo = models.CharField(verbose_name='наименование фото', max_length=200, default=None, blank=True)
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    image = ThumbnailerImageField(verbose_name='фото', upload_to='product/photos')

    class Meta:
        verbose_name = 'фото товара'
        verbose_name_plural = 'фотографии товара'

    def image_img(self):
        if self.image:
            return '<img src="%s" width="100"/>' % self.image.url
        else:
            return '(none)'

    def __str__(self):
        return self.name_photo

    image.short_description = 'Thumb'
    image.allow_tags = True


@receiver(post_delete, sender=Photo)
def photo_post_delete_handler(sender, **kwargs):
    photo = kwargs['instance']
    storage, path = photo.image.storage, photo.image.path
    storage.delete(path)


