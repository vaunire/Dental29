from django.db import models

# Модель для хранения типов документов (например, согласие, договор, ИДС)
class DocumentType(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип документа'
        verbose_name_plural = 'Типы документов'

# Модель для хранения статусов документов
class DocumentStatus(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус документа'
        verbose_name_plural = 'Статусы документов'

# Модель для хранения всех видов документов
class Document(models.Model):
    issue_date = models.DateField(verbose_name = 'Дата выдачи')
    issued_by = models.CharField(max_length = 255, verbose_name = 'Кем выдан')
    patient = models.ForeignKey('patients.Patient', on_delete = models.CASCADE, null = True, blank = True, verbose_name = 'Пациент')
    employee = models.ForeignKey('employees.Employee', on_delete = models.PROTECT, null = True, blank = True, verbose_name = 'Сотрудник')
    status = models.ForeignKey(DocumentStatus, on_delete = models.PROTECT, verbose_name = 'Статус')
    document_type = models.ForeignKey(DocumentType, on_delete = models.PROTECT, verbose_name = 'Тип документа')

    def __str__(self):
        return f"{self.document_type} {self.id}"

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        indexes = [models.Index(fields = ['patient']), models.Index(fields = ['employee']), models.Index(fields = ['document_type'])]

# Модель для хранения информированных добровольных согласий на медицинское вмешательство
class InformedConsent(models.Model):
    nomenclature = models.ForeignKey('services.Nomenclature', on_delete = models.PROTECT, verbose_name = 'Номенклатура')
    patient = models.ForeignKey('patients.Patient', on_delete = models.CASCADE, verbose_name = 'Пациент')
    document = models.ForeignKey(Document, on_delete = models.CASCADE, verbose_name = 'Документ')
    employee = models.ForeignKey('employees.Employee', on_delete = models.PROTECT, verbose_name = 'Сотрудник')

    def __str__(self):
        return f"ИДС для {self.patient} ({self.nomenclature})"

    class Meta:
        verbose_name = 'ИДС на мед. вмешательство'
        verbose_name_plural = 'ИДС на мед. вмешательства'
        indexes = [models.Index(fields = ['patient'])]

# Модель для хранения договоров
class Contract(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete = models.PROTECT, verbose_name = 'Пациент')
    employee = models.ForeignKey('employees.Employee', on_delete = models.PROTECT, verbose_name = 'Сотрудник')
    document = models.ForeignKey(Document, on_delete = models.PROTECT, verbose_name = 'Документ')

    def __str__(self):
        return f"Договор {self.id} для {self.patient}"

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'
        indexes = [models.Index(fields = ['patient'])]

# Модель для хранения приложений к договорам
class ContractAppendix(models.Model):
    discount = models.DecimalField(max_digits = 5, decimal_places = 2, verbose_name = 'Скидка')
    total_cost = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = 'Общая стоимость')
    discounted_cost = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = 'Стоимость со скидкой')
    patient = models.ForeignKey('patients.Patient', on_delete = models.PROTECT, verbose_name = 'Пациент')
    employee = models.ForeignKey('employees.Employee', on_delete = models.PROTECT, verbose_name = 'Сотрудник')
    contract = models.ForeignKey(Contract, on_delete = models.CASCADE, verbose_name = 'Договор')

    def __str__(self):
        return f"Приложение к договору {self.contract}"

    class Meta:
        verbose_name = 'Приложение к договору'
        verbose_name_plural = 'Приложения к договорам'
        indexes = [models.Index(fields=['contract'])]

# Модель для хранения оплат по договорам
class Payment(models.Model):
    payment_date = models.DateField(verbose_name = 'Дата оплаты')
    amount = models.DecimalField(max_digits = 10, decimal_places=2, verbose_name = 'Сумма')
    contract = models.ForeignKey(Contract, on_delete = models.CASCADE, verbose_name = 'Договор')

    def __str__(self):
        return f"Оплата {self.amount} для {self.contract}"

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'
        indexes = [models.Index(fields=['contract'])]