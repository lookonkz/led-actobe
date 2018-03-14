from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Create your models here.
class Page(models.Model):
    name = models.CharField(verbose_name='название', max_length=200, blank=True)
    slug = models.SlugField('название к сылке')
    description = models.TextField(verbose_name='описание', default=None, blank=True)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        ordering = ['name']

    def __str__(self):
        return self.name


class Work(models.Model):
    name = models.CharField(verbose_name='название', max_length=200, blank=True)
    description = models.CharField(verbose_name='описание', max_length=500, default=None, blank=True)
    photo = ThumbnailerImageField(verbose_name='фото', upload_to='works/photos')

    class Meta:
        verbose_name = 'Протфолио'
        verbose_name_plural = 'Портфолии'
        ordering = ['name']

    def __str__(self):
        return self.name


@receiver(post_delete, sender=Work)
def photo_post_delete_handler(sender, **kwargs):
    work = kwargs['instance']
    storage, path = work.photo.storage, work.photo.path
    storage.delete(path)
