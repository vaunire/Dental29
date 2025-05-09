from django.db import models
from django.core.exceptions import ValidationError
import calendar

# Модель для хранения месяцев для расписания
class Month(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Название')
    year = models.PositiveIntegerField(verbose_name = 'Год')

    def __str__(self):
        return f"{self.name} {self.year}"

    class Meta:
        verbose_name = 'Месяц'
        verbose_name_plural = 'Месяцы'
        unique_together = [['name', 'year']]
        indexes = [models.Index(fields = ['name', 'year'])]

# Модель для хранения статусов дней (рабочий, выходной)
class DayStatus(models.Model):
    name = models.CharField(max_length = 1, choices = [('Р', 'Рабочий'), ('В', 'Выходной')], verbose_name = 'Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус дня'
        verbose_name_plural = 'Статусы дней'

# Модель для хранения дней в месяце
class Day(models.Model):
    number = models.PositiveIntegerField(verbose_name = 'Число')
    month = models.ForeignKey(Month, on_delete = models.PROTECT, verbose_name = 'Месяц')
    status = models.ForeignKey(DayStatus, on_delete = models.PROTECT, verbose_name = 'Статус')

    def clean(self):
        month_map = {'Январь': 1, 'Февраль': 2, 'Март': 3, 'Апрель': 4, 'Май': 5, 'Июнь': 6, 'Июль': 7, 'Август': 8, 'Сентябрь': 9, 'Октябрь': 10, 'Ноябрь': 11, 'Декабрь': 12}
        if self.month.name not in month_map:
            raise ValidationError('Недопустимое название месяца.')
        month_number = month_map[self.month.name]
        max_days = calendar.monthrange(self.month.year, month_number)[1]
        if not 1 <= self.number <= max_days:
            raise ValidationError(f'Число дня должно быть от 1 до {max_days} для {self.month}.')

    def __str__(self):
        return f"{self.number} {self.month}"

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'
        # Гарантирует уникальность комбинации названия месяца и года (например, только один "Январь 2025")
        unique_together = [['number', 'month']]
        indexes = [models.Index(fields=['month', 'number'])]

# Модель для хранения расписания на день
class Schedule(models.Model):
    start_time = models.TimeField(verbose_name = 'Время начала')
    end_time = models.TimeField(verbose_name = 'Время окончания')
    break_start = models.TimeField(null = True, blank=True, verbose_name = 'Начало перерыва')
    break_end = models.TimeField(null = True, blank=True, verbose_name = 'Окончание перерыва')
    day = models.ForeignKey(Day, on_delete = models.PROTECT, verbose_name = 'День')

    def __str__(self):
        return f"Расписание на {self.day}"

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
        indexes = [models.Index(fields = ['day'])]

# Модель для хранения связи расписания с сотрудником
class SchedulePosition(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete = models.CASCADE, verbose_name = 'Расписание')
    employee = models.ForeignKey('employees.Employee', on_delete = models.PROTECT, verbose_name = 'Сотрудник')

    def __str__(self):
        return f"Позиция для {self.schedule}"

    class Meta:
        verbose_name = 'Позиция расписания'
        verbose_name_plural = 'Позиции расписания'
        indexes = [models.Index(fields = ['employee'])]

# Модель для хранения видов приёмов
class AppointmentType(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид приёма'
        verbose_name_plural = 'Виды приёмов'

# Модель для хранения статусов напоминаний о приёмах
class ReminderStatus(models.Model):
    is_sent = models.BooleanField(default = False, verbose_name = 'Отправлено')

    def __str__(self):
        return 'Отправлено' if self.is_sent else 'Не отправлено'

    class Meta:
        verbose_name = 'Статус напоминания'
        verbose_name_plural = 'Статусы напоминаний'

# Модель для хранения записей на приём
class Appointment(models.Model):
    appointment_date = models.DateField(verbose_name = 'Дата приёма')
    start_time = models.TimeField(verbose_name = 'Время начала')
    duration = models.DurationField(verbose_name = 'Продолжительность')
    appointment_type = models.ForeignKey(AppointmentType, on_delete = models.PROTECT, verbose_name = 'Тип приёма')
    patient = models.ForeignKey('patients.Patient', on_delete = models.PROTECT, verbose_name = 'Пациент')
    employee = models.ForeignKey('employees.Employee', on_delete = models.PROTECT, verbose_name = 'Сотрудник')
    cabinet = models.ForeignKey('employees.Cabinet', on_delete = models.PROTECT, verbose_name = 'Кабинет')
    schedule = models.ForeignKey(Schedule, on_delete = models.PROTECT, verbose_name = 'Расписание')
    reminder_status = models.ForeignKey(ReminderStatus, on_delete = models.PROTECT, verbose_name = 'Статус напоминания')

    def clean(self):
        if not (self.schedule.start_time <= self.start_time < self.schedule.end_time):
            raise ValidationError('Время приёма должно быть в рамках расписания.')
        if self.schedule.break_start and self.schedule.break_end:
            if self.schedule.break_start <= self.start_time < self.schedule.break_end:
                raise ValidationError('Время приёма попадает на перерыв.')

    def __str__(self):
        return f"Приём {self.patient} на {self.appointment_date}"

    class Meta:
        verbose_name = 'Запись на приём'
        verbose_name_plural = 'Записи на приём'
        indexes = [
            models.Index(fields = ['appointment_date']),
            models.Index(fields = ['employee']),
            models.Index(fields = ['cabinet']),
            models.Index(fields = ['schedule']),
        ]

# Модель для хранения отмен записей на приём
class AppointmentCancellation(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete = models.CASCADE, verbose_name = 'Запись на приём')

    def __str__(self):
        return f"Отмена записи {self.appointment}"

    class Meta:
        verbose_name = 'Отмена записи на приём'
        verbose_name_plural = 'Отмены записей на приём'