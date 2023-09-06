from django.contrib import admin
from .models import Order
from django.utils.translation import gettext_lazy as _
from datetime import date


class DateFilter(admin.SimpleListFilter):
    title = _('Date')
    parameter_name = 'date_filter'

    def lookups(self, request, model_admin):
        return (
            ('past', _('Past')),
            ('today', _('Today')),
            ('future', _('Future')),
        )

    def queryset(self, request, queryset):
        now = date.today()

        if self.value() == 'past':
            return queryset.filter(doctor_schedule__date__lt=now)
        elif self.value() == 'today':
            return queryset.filter(doctor_schedule__date=now)
        elif self.value() == 'future':
            return queryset.filter(doctor_schedule__date__gt=now)
        else:
            return queryset


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('patient', 'service', 'doctor_schedule_date', 'status')
    list_filter = ('status', 'service__subcategory__category', DateFilter)
    ordering = ('doctor_schedule__date',)

    def doctor_schedule_date(self, obj):
        return obj.doctor_schedule.date

    doctor_schedule_date.short_description = 'Date'


