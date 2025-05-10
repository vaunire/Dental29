from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from unfold.admin import ModelAdmin, TabularInline
from unfold.contrib.filters.admin import RelatedDropdownFilter, RangeDateFilter

from _config.admin import BaseAdmin
from .models import (
    DocumentType, DocumentStatus, Document, InformedConsent, Contract,
    ContractAppendix, Payment
)


# Inline для приложений к договору
class ContractAppendixInline(TabularInline):
    model = ContractAppendix
    extra = 0
    fields = ['discount', 'total_cost', 'discounted_cost', 'patient', 'employee']
    autocomplete_fields = ['patient', 'employee']


@admin.register(DocumentType)
class DocumentTypeAdmin(BaseAdmin):
    list_display = ['name']
    search_fields = ['name']
    # Простая регистрация для справочной модели


@admin.register(DocumentStatus)
class DocumentStatusAdmin(BaseAdmin):
    list_display = ['name']
    search_fields = ['name']
    # Простая регистрация для справочной модели


@admin.register(Document)
class DocumentAdmin(BaseAdmin):
    list_display = ['document_type', 'issue_date', 'patient_link', 'employee']
    search_fields = ['patient__last_name', 'patient__first_name', 'employee__last_name']
    list_filter = [
        ('document_type', RelatedDropdownFilter),
        ('status', RelatedDropdownFilter),
        ('patient', RelatedDropdownFilter),
        ('employee', RelatedDropdownFilter),
        ('issue_date', RangeDateFilter),
    ]
    autocomplete_fields = ['patient', 'employee', 'status', 'document_type']

    # Отображает ссылку на пациента
    def patient_link(self, obj):
        if obj.patient:
            url = reverse('admin:patients_patient_change', args=[obj.patient.id])
            return format_html('<a href="{}">{}</a>', url, obj.patient)
        return '-'
    patient_link.short_description = 'Пациент'


@admin.register(InformedConsent)
class InformedConsentAdmin(BaseAdmin):
    list_display = ['patient_link', 'nomenclature', 'employee']
    search_fields = ['patient__last_name', 'patient__first_name']
    list_filter = [
        ('patient', RelatedDropdownFilter),
        ('nomenclature', RelatedDropdownFilter),
        ('employee', RelatedDropdownFilter),
    ]
    autocomplete_fields = ['nomenclature', 'patient', 'document', 'employee']

    # Отображает ссылку на пациента
    def patient_link(self, obj):
        url = reverse('admin:patients_patient_change', args=[obj.patient.id])
        return format_html('<a href="{}">{}</a>', url, obj.patient)
    patient_link.short_description = 'Пациент'


@admin.register(Contract)
class ContractAdmin(BaseAdmin):
    list_display = ['patient_link', 'employee', 'document']
    search_fields = ['patient__last_name', 'patient__first_name']
    list_filter = [
        ('patient', RelatedDropdownFilter),
        ('employee', RelatedDropdownFilter),
    ]
    inlines = [ContractAppendixInline]
    autocomplete_fields = ['patient', 'employee', 'document']

    # Отображает ссылку на пациента
    def patient_link(self, obj):
        url = reverse('admin:patients_patient_change', args=[obj.patient.id])
        return format_html('<a href="{}">{}</a>', url, obj.patient)
    patient_link.short_description = 'Пациент'


@admin.register(ContractAppendix)
class ContractAppendixAdmin(BaseAdmin):
    list_display = ['contract', 'patient', 'total_cost', 'discounted_cost']
    search_fields = ['patient__last_name', 'patient__first_name']
    list_filter = [
        ('contract', RelatedDropdownFilter),
        ('patient', RelatedDropdownFilter),
        ('employee', RelatedDropdownFilter),
    ]
    autocomplete_fields = ['patient', 'employee', 'contract']


@admin.register(Payment)
class PaymentAdmin(BaseAdmin):
    list_display = ['contract', 'payment_date', 'amount']
    search_fields = ['contract__patient__last_name', 'contract__patient__first_name']
    list_filter = [
        ('contract', RelatedDropdownFilter),
        ('payment_date', RangeDateFilter),
    ]
    autocomplete_fields = ['contract']