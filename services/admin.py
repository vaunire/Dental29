from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from unfold.admin import ModelAdmin, TabularInline
from unfold.contrib.filters.admin import RelatedDropdownFilter, RangeDateFilter

from _config.admin import BaseAdmin
from .models import (
    NomenclatureType, Unit, Nomenclature, PriceList, PriceListItem,
    ServiceOnAppointment, Manipulation
)


# Inline для позиций прайс-листа
class PriceListItemInline(TabularInline):
    model = PriceListItem
    extra = 0
    fields = ['nomenclature', 'price']
    autocomplete_fields = ['nomenclature']


@admin.register(NomenclatureType)
class NomenclatureTypeAdmin(BaseAdmin):
    list_display = ['name']
    search_fields = ['name']
    # Простая регистрация для справочной модели


@admin.register(Unit)
class UnitAdmin(BaseAdmin):
    list_display = ['name', 'short_name']
    search_fields = ['name']
    # Простая регистрация для справочной модели


@admin.register(Nomenclature)
class NomenclatureAdmin(BaseAdmin):
    list_display = ['name', 'nomenclature_type', 'unit']
    search_fields = ['name']
    list_filter = [
        ('nomenclature_type', RelatedDropdownFilter),
        ('unit', RelatedDropdownFilter),
    ]
    autocomplete_fields = ['nomenclature_type', 'unit']


@admin.register(PriceList)
class PriceListAdmin(BaseAdmin):
    list_display = ['start_date', 'end_date', 'employee']
    search_fields = ['employee__last_name', 'employee__first_name']
    list_filter = [
        ('start_date', RangeDateFilter),
        ('employee', RelatedDropdownFilter),
    ]
    inlines = [PriceListItemInline]
    autocomplete_fields = ['employee', 'document']


@admin.register(PriceListItem)
class PriceListItemAdmin(BaseAdmin):
    list_display = ['price_list', 'nomenclature', 'price']
    search_fields = ['nomenclature__name']
    list_filter = [
        ('price_list', RelatedDropdownFilter),
        ('nomenclature', RelatedDropdownFilter),
    ]
    autocomplete_fields = ['price_list', 'nomenclature']


@admin.register(ServiceOnAppointment)
class ServiceOnAppointmentAdmin(BaseAdmin):
    list_display = ['nomenclature', 'appointment']
    search_fields = ['nomenclature__name', 'appointment__patient__last_name']
    list_filter = [
        ('nomenclature', RelatedDropdownFilter),
        ('appointment', RelatedDropdownFilter),
    ]
    autocomplete_fields = ['nomenclature', 'appointment']


@admin.register(Manipulation)
class ManipulationAdmin(BaseAdmin):
    list_display = ['contract_appendix', 'price_list_item', 'quantity']
    search_fields = ['contract_appendix__contract__patient__last_name']
    list_filter = [
        ('contract_appendix', RelatedDropdownFilter),
        ('price_list_item', RelatedDropdownFilter),
    ]
    autocomplete_fields = ['contract_appendix', 'price_list_item']