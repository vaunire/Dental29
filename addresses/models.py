from django.db import models

# Модель для хранения стран
class Country(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

# Модель для хранения регионов
class Region(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Название')
    country = models.ForeignKey(Country, on_delete = models.PROTECT, verbose_name = 'Страна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
        indexes = [models.Index(fields = ['country'])]

# Модель для хранения типов населённых пунктов
class SettlementType(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид населённого пункта'
        verbose_name_plural = 'Виды населённых пунктов'

# Модель для хранения населённых пунктов
class Settlement(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Название')
    region = models.ForeignKey(Region, on_delete = models.PROTECT, verbose_name = 'Регион')
    settlement_type = models.ForeignKey(SettlementType, on_delete = models.PROTECT, verbose_name = 'Тип населённого пункта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Населённый пункт'
        verbose_name_plural = 'Населённые пункты'
        indexes = [models.Index(fields = ['region'])]

# Модель для хранения улиц
class Street(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Название')
    settlement = models.ForeignKey(Settlement, on_delete = models.PROTECT, verbose_name = 'Населённый пункт')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'
        indexes = [models.Index(fields = ['settlement'])]

# Модель для хранения адресов
class Address(models.Model):
    postal_code = models.CharField(max_length = 10, blank = True, verbose_name = 'Почтовый индекс')
    house_number = models.CharField(max_length = 10, verbose_name = 'Номер дома')
    building = models.CharField(max_length = 10, blank = True, verbose_name = 'Корпус')
    structure = models.CharField(max_length = 10, blank = True, verbose_name = 'Строение')
    apartment = models.CharField(max_length = 10, blank = True, verbose_name = 'Квартира')
    street = models.ForeignKey(Street, on_delete = models.PROTECT, verbose_name = 'Улица')

    def __str__(self):
        return f"{self.street}, д.{self.house_number}"

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        indexes = [models.Index(fields = ['street'])]