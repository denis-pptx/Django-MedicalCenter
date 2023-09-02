from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Page


@admin.register(Page)
class PageAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'page_type', 'active')
    list_filter = ('active', 'page_type')
    actions = ['mark_as_unactive']

    def mark_as_unactive(self, request, queryset):
        queryset.update(active=False)

    mark_as_unactive.short_description = 'Mark selected pages as inactive'
