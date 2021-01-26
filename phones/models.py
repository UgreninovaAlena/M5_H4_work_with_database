from django.db import models

class Phone(models.Model):

    name = models.TextField(default=None, verbose_name='Модель')
    price = models.IntegerField(default=None, verbose_name='Цена')
    image = models.TextField(null = True, verbose_name='Изображение')
    release_date = models.DateField(default=None, verbose_name='Дата выпуска')
    lte_exists = models.BooleanField(default=None, verbose_name='В наличии')
    slug = models.TextField(default=None)
    # comp = models.ForeignKey('Company', on_delete=models.CASCADE())


