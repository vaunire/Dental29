from django.db import models
from django.core.exceptions import ValidationError

# Модель для хранения полов пациентов и сотрудников
class Gender(models.Model):
    name = models.CharField(max_length = 1, choices = [('М', 'Мужской'), ('Ж', 'Женский')], verbose_name = 'Пол')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Полы'

# Модель для хранения типов пациентов (например, взрослый, ребёнок)
class PatientType(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Название')
    service_conditions = models.TextField(blank = True, verbose_name = 'Условия обслуживания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид пациента'
        verbose_name_plural = 'Виды пациентов'

# Модель для хранения информации о пациентах
class Patient(models.Model):
    last_name = models.CharField(max_length = 100, verbose_name='Фамилия')
    first_name = models.CharField(max_length = 100, verbose_name='Имя')
    middle_name = models.CharField(max_length = 100, blank = True, verbose_name = 'Отчество')
    birth_date = models.DateField(verbose_name = 'Дата рождения')
    gender = models.ForeignKey(Gender, on_delete = models.PROTECT, verbose_name='Пол')
    patient_type = models.ForeignKey(PatientType, on_delete = models.PROTECT, verbose_name='Тип пациента')
    address = models.ForeignKey('addresses.Address', on_delete = models.PROTECT, verbose_name = 'Адрес')

    def get_contacts(self):
        return self.contacts.all()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        # Индекс для ускорения поиска пациентов по фамилии и имени
        indexes = [models.Index(fields = ['last_name', 'first_name'])]

# Модель для хранения видов контактной информации (например, телефон, email)
class ContactType(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид контактной информации'
        verbose_name_plural = 'Виды контактной информации'

# Модель для хранения контактной информации пациентов и сотрудников
class ContactInfo(models.Model):
    value = models.CharField(max_length = 255, verbose_name = 'Значение')
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE, null = True, blank = True, related_name = 'contacts', verbose_name = 'Пациент')
    employee = models.ForeignKey('employees.Employee', on_delete = models.CASCADE, null = True, blank = True, related_name = 'contacts', verbose_name = 'Сотрудник')
    contact_type = models.ForeignKey(ContactType, on_delete = models.PROTECT, verbose_name = 'Тип контакта')

    def clean(self):
        if self.patient and self.employee:
            raise ValidationError('Контактная информация может быть связана только с пациентом или сотрудником.')
        if not self.patient and not self.employee:
            raise ValidationError('Контактная информация должна быть связана с пациентом или сотрудником.')

    def __str__(self):
        return f"{self.contact_type.name}: {self.value}"

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'
        # Индексы для ускорения поиска контактов по пациенту или сотруднику
        indexes = [models.Index(fields = ['patient']), models.Index(fields = ['employee'])]

# Модель для хранения медицинских карт пациентов
class MedicalCard(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE, verbose_name = 'Пациент')
    document = models.ForeignKey('contracts.Document', on_delete = models.CASCADE, verbose_name = 'Документ')
    mucosa_condition = models.TextField(blank = True, verbose_name = 'Состояние слизистой полости рта')
    complaints = models.TextField(blank = True, verbose_name = 'Жалобы')
    disease_history = models.TextField(blank = True, verbose_name = 'История болезней')
    examination_data = models.TextField(blank = True, verbose_name = 'Данные осмотра')

    def __str__(self):
        return f"Медкарта {self.patient}"

    class Meta:
        verbose_name = 'Медицинская карта'
        verbose_name_plural = 'Медицинские карты'
        # Индекс для ускорения поиска медкарт по пациенту
        indexes = [models.Index(fields = ['patient'])]

# Модель для хранения вкладышей к медицинским картам
class MedicalCardInsert(models.Model):
    medical_card = models.ForeignKey(MedicalCard, on_delete = models.CASCADE, verbose_name = 'Медицинская карта')
    employee = models.ForeignKey('employees.Employee', on_delete = models.PROTECT, verbose_name = 'Сотрудник')
    visit_complaints = models.TextField(blank = True, verbose_name = 'Жалобы на визите')
    dental_history = models.TextField(blank = True, verbose_name = 'Стоматологический анамнез')
    allergic_history = models.TextField(blank = True, verbose_name = 'Аллергологический анамнез')
    visit_examination = models.TextField(blank = True, verbose_name = 'Данные осмотра на визите')
    diagnosis = models.ForeignKey('dental.Diagnosis', on_delete = models.PROTECT, verbose_name = 'Диагноз')
    nomenclature = models.ForeignKey('services.Nomenclature', on_delete = models.PROTECT, verbose_name = 'Номенклатура')

    def __str__(self):
        return f"Вкладыш для {self.medical_card}"

    class Meta:
        verbose_name = 'Вкладыш к медицинской карте'
        verbose_name_plural = 'Вкладыши к медицинским картам'
        # Индекс для ускорения поиска вкладышей по медкарте
        indexes = [models.Index(fields = ['medical_card'])]

# Модель для хранения согласий на обработку персональных данных
class PersonalDataConsent(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE, verbose_name = 'Пациент')
    document = models.ForeignKey('contracts.Document', on_delete = models.CASCADE, verbose_name = 'Документ')
    consent_date = models.DateField(verbose_name = 'Дата согласия')
    expiry_date = models.DateField(null = True, blank = True, verbose_name = 'Дата истечения')

    def __str__(self):
        return f"Согласие для {self.patient}"

    class Meta:
        verbose_name = 'Согласие на обработку данных'
        verbose_name_plural = 'Согласия на обработку данных'
        indexes = [models.Index(fields = ['patient'])]

# Модель для хранения анкет здоровья пациентов
class HealthQuestionnaire(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE, verbose_name = 'Пациент')
    employee = models.ForeignKey('employees.Employee', on_delete = models.PROTECT, verbose_name = 'Сотрудник')
    document = models.ForeignKey('contracts.Document', on_delete = models.CASCADE, verbose_name = 'Документ')

    def __str__(self):
        return f"Анкета здоровья для {self.patient}"

    class Meta:
        verbose_name = 'Анкета здоровья'
        verbose_name_plural = 'Анкеты здоровья'
        indexes = [models.Index(fields = ['patient'])]

# Модель для хранения информации о непереносимости лекарств
class Intolerance(models.Model):
    nomenclature = models.ForeignKey('services.Nomenclature', on_delete=models.PROTECT, verbose_name='Номенклатура')
    medical_card = models.ForeignKey(MedicalCard, on_delete=models.CASCADE, verbose_name='Медицинская карта')

    def __str__(self):
        return f"Непереносимость для {self.medical_card}"

    class Meta:
        verbose_name = 'Непереносимое лекарство'
        verbose_name_plural = 'Непереносимые лекарства'
        indexes = [models.Index(fields=['medical_card'])]

# Модель для хранения заболеваний пациентов
class Disease(models.Model):
    diagnosis = models.ForeignKey('dental.Diagnosis', on_delete = models.PROTECT, verbose_name = 'Диагноз')
    medical_card = models.ForeignKey(MedicalCard, on_delete = models.CASCADE, verbose_name = 'Медицинская карта')
    medical_card_insert = models.ForeignKey(MedicalCardInsert, on_delete = models.CASCADE, null = True, blank = True, verbose_name = 'Вкладыш медицинской карты')

    def __str__(self):
        return f"Заболевание для {self.medical_card}"

    class Meta:
        verbose_name = 'Заболевание'
        verbose_name_plural = 'Заболевания'
        indexes = [models.Index(fields = ['medical_card'])]