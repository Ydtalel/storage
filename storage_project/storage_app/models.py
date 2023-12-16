from django.db import models
from model_utils.models import TimeStampedModel


class Category(TimeStampedModel):
    name_ru = models.CharField(verbose_name='Название на русском', max_length=255, unique=True)
    name_en = models.CharField(verbose_name='Название на английском', max_length=255,
                               unique=True, blank=True, null=True)
    category_code = models.SmallIntegerField(default=10, blank=True, null=True)

    def __str__(self):
        return self.name_ru

    class Meta:
        ordering = ('name_ru', 'category_code')


class Item(TimeStampedModel):
    category = models.ForeignKey(
        Category,
        verbose_name='',
        on_delete=models.CASCADE,
    )

    code = models.IntegerField(verbose_name='Код поставщика')
    internal_code = models.IntegerField(verbose_name='Код в приложении', unique=True, null=True, blank=True)

    package_length = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Длина упаковки')
    package_width = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Ширина упаковки')
    package_height = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Высота упаковки')

    name_ru = models.CharField(verbose_name='Название на русском', max_length=255)
    description_ru = models.CharField(verbose_name='Описание на русском', max_length=255, blank=True, null=True)
    description_en = models.CharField(verbose_name='Описание на английском', max_length=255, blank=True, null=True)

    amount = models.IntegerField(verbose_name='Кол-во единиц на складе')
    cost = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)

    is_active = models.BooleanField(verbose_name='Текущий ассортимент', default=True)

    additional = models.ManyToManyField('self', verbose_name='Дополнительная информация', symmetrical=False,
                                        related_name='additional_from', blank=True)

    def __str__(self):
        return self.name_ru

