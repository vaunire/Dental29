from django.db import models

# Модель для хранения должностей сотрудников
class Position(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

# Модель для хранения статусов сотрудников (например, активен, уволен)
class EmployeeStatus(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус сотрудника'
        verbose_name_plural = 'Статусы сотрудников'

# Модель для хранения кабинетов
class Cabinet(models.Model):
    number = models.CharField(max_length = 10, verbose_name = 'Номер')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'

# Модель для хранения информации о сотрудниках
class Employee(models.Model):
    last_name = models.CharField(max_length = 100, verbose_name = 'Фамилия')
    first_name = models.CharField(max_length = 100, verbose_name = 'Имя')
    middle_name = models.CharField(max_length = 100, blank = True, verbose_name = 'Отчество')
    birth_date = models.DateField(verbose_name = 'Дата рождения')
    gender = models.ForeignKey('patients.Gender', on_delete = models.PROTECT, verbose_name = 'Пол')
    position = models.ForeignKey(Position, on_delete = models.PROTECT, verbose_name = 'Должность')
    cabinet = models.ForeignKey(Cabinet, on_delete = models.PROTECT, verbose_name = 'Кабинет')
    status = models.ForeignKey(EmployeeStatus, on_delete = models.PROTECT, verbose_name = 'Статус')

    def get_contacts(self):
        return self.contacts.all()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        indexes = [models.Index(fields=['last_name', 'first_name'])]
