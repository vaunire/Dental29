from django.db import models

# Модель для хранения диагнозов по МКБ-10
class Diagnosis(models.Model):
    icd10_code = models.CharField(max_length = 10, verbose_name = 'Код МКБ-10')
    name = models.CharField(max_length = 255, verbose_name = 'Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Диагноз'
        verbose_name_plural = 'Диагнозы'
        indexes = [models.Index(fields = ['icd10_code'])]

# Модель для хранения позиций зубов в зубной формуле
class ToothPosition(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Позиция зуба'
        verbose_name_plural = 'Позиции зубов'

# Модель для хранения статусов зубов
class ToothStatus(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус зуба'
        verbose_name_plural = 'Статусы зубов'

# Модель для хранения зубных формул
class ToothFormula(models.Model):
    medical_card = models.ForeignKey('patients.MedicalCard', on_delete = models.CASCADE, verbose_name = 'Медицинская карта')
    medical_card_insert = models.ForeignKey('patients.MedicalCardInsert', on_delete = models.CASCADE, null = True, blank = True, verbose_name = 'Вкладыш медицинской карты')

    def __str__(self):
        return f"Формула для {self.medical_card}"

    class Meta:
        verbose_name = 'Зубная формула'
        verbose_name_plural = 'Зубные формулы'
        indexes = [models.Index(fields = ['medical_card'])]

# Модель для хранения информации о зубах в зубной формуле
class Tooth(models.Model):
    tooth_formula = models.ForeignKey(ToothFormula, on_delete = models.CASCADE, verbose_name = 'Зубная формула')
    position = models.ForeignKey(ToothPosition, on_delete = models.PROTECT, verbose_name = 'Позиция')
    status = models.ForeignKey(ToothStatus, on_delete = models.PROTECT, verbose_name = 'Статус')

    def __str__(self):
        return f"Зуб {self.position} ({self.status})"

    class Meta:
        verbose_name = 'Зуб'
        verbose_name_plural = 'Зубы'
        indexes = [models.Index(fields = ['tooth_formula'])]

# Модель для хранения назначений пациентам
class Prescription(models.Model):
    quantity = models.PositiveIntegerField(verbose_name = 'Количество')
    prescription_date = models.DateField(verbose_name = 'Дата назначения')
    execution_count = models.PositiveIntegerField(verbose_name = 'Количество выполнений')
    comment = models.TextField(blank = True, verbose_name = 'Комментарий')
    nomenclature = models.ForeignKey('services.Nomenclature', on_delete = models.PROTECT, verbose_name = 'Номенклатура')
    medical_card = models.ForeignKey('patients.MedicalCard', on_delete = models.CASCADE, verbose_name = 'Медицинская карта')
    medical_card_insert = models.ForeignKey('patients.MedicalCardInsert', on_delete = models.CASCADE, null = True, blank = True, verbose_name = 'Вкладыш медицинской карты')

    def __str__(self):
        return f"Назначение {self.nomenclature}"

    class Meta:
        verbose_name = 'Назначение'
        verbose_name_plural = 'Назначения'
        indexes = [models.Index(fields = ['medical_card'])]