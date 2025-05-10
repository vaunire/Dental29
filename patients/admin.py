from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from unfold.admin import ModelAdmin, TabularInline
from unfold.contrib.filters.admin import RelatedDropdownFilter, RangeDateFilter

from _config.admin import BaseAdmin
from .models import (
    Gender, PatientType, Patient, ContactType, ContactInfo, MedicalCard,
    MedicalCardInsert, PersonalDataConsent, HealthQuestionnaire, Intolerance, Disease
)


# Inline для редактирования контактной информации в формах Patient и Employee
class ContactInfoInline(TabularInline):
    model = ContactInfo
    extra = 1
    fields = ['contact_type', 'value']
    autocomplete_fields = ['contact_type']
    # Запрещает удаление контактов, если они критичны
    def has_delete_permission(self, request, obj=None):
        return False



@admin.register(Gender)
class GenderAdmin(BaseAdmin):
    list_display = ['name']
    search_fields = ['name']
    # Простая регистрация для справочной модели


@admin.register(PatientType)
class PatientTypeAdmin(BaseAdmin):
    list_display = ['name']
    search_fields = ['name']
    # Простая регистрация для справочной модели


@admin.register(Patient)
class PatientAdmin(BaseAdmin):
    list_display = ['full_name', 'birth_date', 'gender', 'patient_type', 'address_link']
    search_fields = ['last_name', 'first_name', 'middle_name']
    list_filter = [
        ('gender', RelatedDropdownFilter),
        ('patient_type', RelatedDropdownFilter),
        ('birth_date', RangeDateFilter),
    ]
    inlines = [ContactInfoInline,]
    autocomplete_fields = ['gender', 'patient_type', 'address']
    fieldsets = (
        ('Основная информация', {
            'fields': ('last_name', 'first_name', 'middle_name', 'birth_date', 'gender', 'patient_type'),
        }),
        ('Адрес', {
            'fields': ('address',),
        }),
    )

    # Отображает полное имя пациента
    def full_name(self, obj):
        return f"{obj.last_name} {obj.first_name} {obj.middle_name}".strip()
    full_name.short_description = 'ФИО'

    # Отображает ссылку на адрес
    def address_link(self, obj):
        url = reverse('admin:addresses_address_change', args=[obj.address.id])
        return format_html('<a href="{}">{}</a>', url, obj.address)
    address_link.short_description = 'Адрес'


@admin.register(ContactType)
class ContactTypeAdmin(BaseAdmin):
    list_display = ['name']
    search_fields = ['name']
    # Простая регистрация для справочной модели


@admin.register(ContactInfo)
class ContactInfoAdmin(BaseAdmin):
    list_display = ['value', 'contact_type', 'patient_link', 'employee_link']
    search_fields = ['value']
    list_filter = [
        ('contact_type', RelatedDropdownFilter),
        ('patient', RelatedDropdownFilter),
        ('employee', RelatedDropdownFilter),
    ]
    autocomplete_fields = ['patient', 'employee', 'contact_type']

    # Отображает ссылку на пациента
    def patient_link(self, obj):
        if obj.patient:
            url = reverse('admin:patients_patient_change', args=[obj.patient.id])
            return format_html('<a href="{}">{}</a>', url, obj.patient)
        return '-'
    patient_link.short_description = 'Пациент'

    # Отображает ссылку на сотрудника
    def employee_link(self, obj):
        if obj.employee:
            url = reverse('admin:employees_employee_change', args=[obj.employee.id])
            return format_html('<a href="{}">{}</a>', url, obj.employee)
        return '-'
    employee_link.short_description = 'Сотрудник'


@admin.register(MedicalCard)
class MedicalCardAdmin(BaseAdmin):
    list_display = ['patient_link', 'document']
    search_fields = ['patient__last_name', 'patient__first_name']
    list_filter = [('patient', RelatedDropdownFilter)]
    autocomplete_fields = ['patient', 'document']

    # Отображает ссылку на пациента
    def patient_link(self, obj):
        url = reverse('admin:patients_patient_change', args=[obj.patient.id])
        return format_html('<a href="{}">{}</a>', url, obj.patient)
    patient_link.short_description = 'Пациент'


@admin.register(MedicalCardInsert)
class MedicalCardInsertAdmin(BaseAdmin):
    list_display = ['medical_card', 'employee', 'diagnosis']
    search_fields = ['medical_card__patient__last_name', 'medical_card__patient__first_name']
    list_filter = [
        ('medical_card', RelatedDropdownFilter),
        ('employee', RelatedDropdownFilter),
        ('diagnosis', RelatedDropdownFilter),
    ]
    autocomplete_fields = ['medical_card', 'employee', 'diagnosis', 'nomenclature']


@admin.register(PersonalDataConsent)
class PersonalDataConsentAdmin(BaseAdmin):
    list_display = ['patient_link', 'consent_date', 'expiry_date']
    search_fields = ['patient__last_name', 'patient__first_name']
    list_filter = [
        ('patient', RelatedDropdownFilter),
        ('consent_date', RangeDateFilter),
    ]
    autocomplete_fields = ['patient', 'document']

    # Отображает ссылку на пациента
    def patient_link(self, obj):
        url = reverse('admin:patients_patient_change', args=[obj.patient.id])
        return format_html('<a href="{}">{}</a>', url, obj.patient)
    patient_link.short_description = 'Пациент'


@admin.register(HealthQuestionnaire)
class HealthQuestionnaireAdmin(BaseAdmin):
    list_display = ['patient_link', 'employee']
    search_fields = ['patient__last_name', 'patient__first_name']
    list_filter = [
        ('patient', RelatedDropdownFilter),
        ('employee', RelatedDropdownFilter),
    ]
    autocomplete_fields = ['patient', 'employee', 'document']

    # Отображает ссылку на пациента
    def patient_link(self, obj):
        url = reverse('admin:patients_patient_change', args=[obj.patient.id])
        return format_html('<a href="{}">{}</a>', url, obj.patient)
    patient_link.short_description = 'Пациент'


@admin.register(Intolerance)
class IntoleranceAdmin(BaseAdmin):
    list_display = ['medical_card', 'nomenclature']
    search_fields = ['medical_card__patient__last_name', 'medical_card__patient__first_name']
    list_filter = [
        ('medical_card', RelatedDropdownFilter),
        ('nomenclature', RelatedDropdownFilter),
    ]
    autocomplete_fields = ['medical_card', 'nomenclature']


@admin.register(Disease)
class DiseaseAdmin(BaseAdmin):
    list_display = ['medical_card', 'diagnosis']
    search_fields = ['medical_card__patient__last_name', 'medical_card__patient__first_name']
    list_filter = [
        ('medical_card', RelatedDropdownFilter),
        ('diagnosis', RelatedDropdownFilter),
    ]
    autocomplete_fields = ['medical_card', 'diagnosis', 'medical_card_insert']