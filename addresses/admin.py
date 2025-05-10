from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import RelatedDropdownFilter

from _config.admin import BaseAdmin
from .models import Country, Region, SettlementType, Settlement, Street, Address


@admin.register(Country)
class CountryAdmin(BaseAdmin):
    list_display = ['name']
    search_fields = ['name']
    # Простая регистрация для справочной модели


@admin.register(Region)
class RegionAdmin(BaseAdmin):
    list_display = ['name', 'country']
    search_fields = ['name']
    list_filter = [('country', RelatedDropdownFilter)]
    autocomplete_fields = ['country']


@admin.register(SettlementType)
class SettlementTypeAdmin(BaseAdmin):
    list_display = ['name']
    search_fields = ['name']
    # Простая регистрация для справочной модели


@admin.register(Settlement)
class SettlementAdmin(BaseAdmin):
    list_display = ['name', 'region', 'settlement_type']
    search_fields = ['name']
    list_filter = [
        ('region', RelatedDropdownFilter),
        ('settlement_type', RelatedDropdownFilter),
    ]
    autocomplete_fields = ['region', 'settlement_type']


@admin.register(Street)
class StreetAdmin(BaseAdmin):
    list_display = ['name', 'settlement']
    search_fields = ['name']
    list_filter = [('settlement', RelatedDropdownFilter)]
    autocomplete_fields = ['settlement']


@admin.register(Address)
class AddressAdmin(BaseAdmin):
    list_display = ['street', 'house_number', 'postal_code']
    search_fields = ['street__name', 'house_number', 'postal_code']
    list_filter = [('street', RelatedDropdownFilter)]
    autocomplete_fields = ['street']