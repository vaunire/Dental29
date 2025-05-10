from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from unfold.admin import ModelAdmin, TabularInline
from unfold.contrib.filters.admin import RelatedDropdownFilter, RangeDateFilter

from _config.admin import BaseAdmin
from .models import (
    Month, DayStatus, Day, Schedule, SchedulePosition, AppointmentType,
    ReminderStatus, Appointment, AppointmentCancellation
)


# Inline для позиций расписания
class SchedulePositionInline(TabularInline):
    model = SchedulePosition
    extra = 0
    fields = ['employee']
    autocomplete_fields = ['employee']


# Inline для записей на приём
class AppointmentInline(TabularInline):
    model = Appointment
    extra = 0
    fields = ['patient', 'appointment_date', 'start_time', 'duration', 'appointment_type', 'employee', 'cabinet', 'reminder_status']
    autocomplete_fields = ['patient', 'appointment_type', 'employee', 'cabinet', 'schedule', 'reminder_status']
    readonly_fields = ['appointment_date', 'start_time', 'duration']


@admin.register(Month)
class MonthAdmin(BaseAdmin):
    list_display = ['name', 'year']
    search_fields = ['name']
    list_filter = [('year', RelatedDropdownFilter)]
    # Простая регистрация для справочной модели


@admin.register(DayStatus)
class DayStatusAdmin(BaseAdmin):
    list_display = ['name']
    search_fields = ['name']
    # Простая регистрация для справочной модели


@admin.register(Day)
class DayAdmin(BaseAdmin):
    list_display = ['number', 'month', 'status']
    search_fields = ['number']
    list_filter = [
        ('month', RelatedDropdownFilter),
        ('status', RelatedDropdownFilter),
    ]
    autocomplete_fields = ['month', 'status']


@admin.register(Schedule)
class ScheduleAdmin(BaseAdmin):
    list_display = ['day', 'start_time', 'end_time']
    search_fields = ['day__number']
    list_filter = [
        ('day__month', RelatedDropdownFilter),
        ('day', RelatedDropdownFilter),
    ]
    inlines = [SchedulePositionInline, AppointmentInline]
    autocomplete_fields = ['day']


@admin.register(SchedulePosition)
class SchedulePositionAdmin(BaseAdmin):
    list_display = ['schedule', 'employee']
    search_fields = ['employee__last_name', 'employee__first_name']
    list_filter = [
        ('schedule', RelatedDropdownFilter),
        ('employee', RelatedDropdownFilter),
    ]
    autocomplete_fields = ['schedule', 'employee']


@admin.register(AppointmentType)
class AppointmentTypeAdmin(BaseAdmin):
    list_display = ['name']
    search_fields = ['name']
    # Простая регистрация для справочной модели


@admin.register(ReminderStatus)
class ReminderStatusAdmin(BaseAdmin):
    list_display = ['is_sent']
    search_fields = ['is_sent']  # Добавлено для автодополнения
    # Простая регистрация для справочной модели


@admin.register(Appointment)
class AppointmentAdmin(BaseAdmin):
    list_display = ['patient_link', 'appointment_date', 'start_time', 'duration', 'employee', 'cabinet', 'reminder_status']
    search_fields = ['patient__last_name', 'patient__first_name']
    list_filter = [
        ('appointment_date', RangeDateFilter),
        ('employee', RelatedDropdownFilter),
        ('cabinet', RelatedDropdownFilter),
        ('schedule__day__month', RelatedDropdownFilter),
        ('appointment_type', RelatedDropdownFilter),
        ('reminder_status', RelatedDropdownFilter),
    ]
    autocomplete_fields = ['patient', 'employee', 'cabinet', 'schedule', 'appointment_type', 'reminder_status']
    fieldsets = (
        ('Основная информация', {
            'fields': ('patient', 'appointment_date', 'start_time', 'duration', 'appointment_type'),
        }),
        ('Рабочая информация', {
            'fields': ('employee', 'cabinet', 'schedule', 'reminder_status'),
        }),
    )

    # Отображает ссылку на пациента
    def patient_link(self, obj):
        url = reverse('admin:patients_patient_change', args=[obj.patient.id])
        return format_html('<a href="{}">{}</a>', url, obj.patient)
    patient_link.short_description = 'Пациент'


@admin.register(AppointmentCancellation)
class AppointmentCancellationAdmin(BaseAdmin):
    list_display = ['appointment']
    search_fields = ['appointment__patient__last_name', 'appointment__patient__first_name']
    list_filter = [('appointment', RelatedDropdownFilter)]
    autocomplete_fields = ['appointment']