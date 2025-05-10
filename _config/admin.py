from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.utils.html import format_html

from unfold.admin import ModelAdmin, TabularInline
from unfold.contrib.filters.admin import RelatedDropdownFilter, RangeDateFilter
from unfold.contrib.forms.widgets import WysiwygWidget


class BaseAdmin(ModelAdmin):
    list_filter_submit = True
    formfield_overrides = {
        models.TextField: {"widget": WysiwygWidget},
    }