from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import RelatedDropdownFilter, RangeDateFilter

from _config.admin import BaseAdmin
from patients.admin import ContactInfoInline
from .models import Position, EmployeeStatus, Cabinet, Employee


@admin.register(Position)
class PositionAdmin(BaseAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(EmployeeStatus)
class EmployeeStatusAdmin(BaseAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Cabinet)
class CabinetAdmin(BaseAdmin):
    list_display = ['number']
    search_fields = ['number']

@admin.register(Employee)
class EmployeeAdmin(BaseAdmin):
    list_display = ['full_name', 'birth_date', 'position', 'cabinet', 'status']
    search_fields = ['last_name', 'first_name', 'middle_name']
    list_filter = [
        ('position', RelatedDropdownFilter),
        ('cabinet', RelatedDropdownFilter),
        ('status', RelatedDropdownFilter),
        ('birth_date', RangeDateFilter),
    ]
    inlines = [ContactInfoInline]
    autocomplete_fields = ['gender', 'position', 'cabinet', 'status']
    fieldsets = (
        ('Основная информация', {
            'fields': ('last_name', 'first_name', 'middle_name', 'birth_date', 'gender'),
        }),
        ('Рабочая информация', {
            'fields': ('position', 'cabinet', 'status'),
        }),
    )

    # Отображает полное имя сотрудника
    def full_name(self, obj):
        return f"{obj.last_name} {obj.first_name} {obj.middle_name}".strip()
    full_name.short_description = 'ФИО'