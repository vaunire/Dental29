from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from unfold.admin import ModelAdmin, TabularInline
from unfold.contrib.filters.admin import RelatedDropdownFilter, RangeDateFilter

from _config.admin import BaseAdmin
from .models import Diagnosis, ToothPosition, ToothStatus, ToothFormula, Tooth, Prescription


# Inline для зубов в зубной формуле
class ToothInline(TabularInline):
    model = Tooth
    extra = 0
    fields = ['position', 'status']
    autocomplete_fields = ['position', 'status']


@admin.register(Diagnosis)
class DiagnosisAdmin(BaseAdmin):
    list_display = ['icd10_code', 'name']
    search_fields = ['icd10_code', 'name']
    list_filter = [('icd10_code', RelatedDropdownFilter)]
    # Простая регистрация для справочной модели


@admin.register(ToothPosition)
class ToothPositionAdmin(BaseAdmin):
    list_display = ['name']
    search_fields = ['name']
    # Простая регистрация для справочной модели


@admin.register(ToothStatus)
class ToothStatusAdmin(BaseAdmin):
    list_display = ['name']
    search_fields = ['name']
    # Простая регистрация для справочной модели


@admin.register(ToothFormula)
class ToothFormulaAdmin(BaseAdmin):
    list_display = ['medical_card']
    search_fields = ['medical_card__patient__last_name', 'medical_card__patient__first_name']
    list_filter = [('medical_card', RelatedDropdownFilter)]
    inlines = [ToothInline]
    autocomplete_fields = ['medical_card', 'medical_card_insert']


@admin.register(Tooth)
class ToothAdmin(BaseAdmin):
    list_display = ['tooth_formula', 'position', 'status']
    search_fields = ['tooth_formula__medical_card__patient__last_name']
    list_filter = [
        ('tooth_formula', RelatedDropdownFilter),
        ('position', RelatedDropdownFilter),
        ('status', RelatedDropdownFilter),
    ]
    autocomplete_fields = ['tooth_formula', 'position', 'status']


@admin.register(Prescription)
class PrescriptionAdmin(BaseAdmin):
    list_display = ['medical_card', 'nomenclature', 'prescription_date', 'quantity']
    search_fields = ['medical_card__patient__last_name', 'medical_card__patient__first_name']
    list_filter = [
        ('medical_card', RelatedDropdownFilter),
        ('nomenclature', RelatedDropdownFilter),
        ('prescription_date', RangeDateFilter),
    ]
    autocomplete_fields = ['nomenclature', 'medical_card', 'medical_card_insert']