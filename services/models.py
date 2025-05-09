from django.db import models

# Модель для хранения видов номенклатуры (например, услуга, материал)
class NomenclatureType(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид номенклатуры'
        verbose_name_plural = 'Виды номенклатуры'

# Модель для хранения единиц измерения
class Unit(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Название')
    short_name = models.CharField(max_length = 10, verbose_name = 'Краткое название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

# Модель для хранения номенклатуры (услуг, материалов)
class Nomenclature(models.Model):
    name = models.CharField(max_length = 255, verbose_name = 'Название')
    description = models.TextField(blank = True, verbose_name = 'Описание')
    nomenclature_type = models.ForeignKey(NomenclatureType, on_delete = models.PROTECT, verbose_name = 'Тип номенклатуры')
    unit = models.ForeignKey(Unit, on_delete = models.PROTECT, verbose_name = 'Единица измерения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Номенклатура'
        verbose_name_plural = 'Номенклатура'
        indexes = [models.Index(fields=['name'])]

# Модель для хранения прайс-листов
class PriceList(models.Model):
    start_date = models.DateField(verbose_name = 'Дата начала')
    end_date = models.DateField(null = True, blank = True, verbose_name = 'Дата окончания')
    employee = models.ForeignKey('employees.Employee', on_delete = models.PROTECT, verbose_name = 'Сотрудник')
    document = models.ForeignKey('contracts.Document', on_delete = models.PROTECT, verbose_name = 'Документ')

    def __str__(self):
        return f"Прайс-лист от {self.start_date}"

    class Meta:
        verbose_name = 'Прайс-лист'
        verbose_name_plural = 'Прайс-листы'
        indexes = [models.Index(fields = ['start_date'])]

# Модель для хранения позиций прайс-листа
class PriceListItem(models.Model):
    price = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = 'Цена')
    price_list = models.ForeignKey(PriceList, on_delete = models.CASCADE, verbose_name = 'Прайс-лист')
    nomenclature = models.ForeignKey(Nomenclature, on_delete = models.PROTECT, verbose_name = 'Номенклатура')

    def __str__(self):
        return f"{self.nomenclature} - {self.price}"

    class Meta:
        verbose_name = 'Позиция прайс-листа'
        verbose_name_plural = 'Позиции прайс-листа'
        indexes = [models.Index(fields=['price_list'])]

# Модель для хранения услуг, оказанных на приёме
class ServiceOnAppointment(models.Model):
    nomenclature = models.ForeignKey(Nomenclature, on_delete = models.PROTECT, verbose_name = 'Номенклатура')
    appointment = models.ForeignKey('appointments.Appointment', on_delete = models.CASCADE, verbose_name = 'Запись на приём')

    def __str__(self):
        return f"Услуга {self.nomenclature} для {self.appointment}"

    class Meta:
        verbose_name = 'Услуга на приём'
        verbose_name_plural = 'Услуги на приём'
        indexes = [models.Index(fields=['appointment'])]

# Модель для хранения манипуляций в рамках договора
class Manipulation(models.Model):
    quantity = models.PositiveIntegerField(verbose_name = 'Количество')
    contract_appendix = models.ForeignKey('contracts.ContractAppendix', on_delete = models.CASCADE, verbose_name = 'Приложение к договору')
    price_list_item = models.ForeignKey(PriceListItem, on_delete = models.PROTECT, verbose_name = 'Позиция прайс-листа')

    def __str__(self):
        return f"Манипуляция {self.price_list_item}"

    class Meta:
        verbose_name = 'Манипуляция'
        verbose_name_plural = 'Манипуляции'
        indexes = [models.Index(fields=['contract_appendix'])]