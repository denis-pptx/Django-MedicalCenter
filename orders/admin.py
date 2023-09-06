from django.contrib import admin
from django.db.models import Sum

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
    list_display = ('patient', 'service', 'service_price', 'doctor_schedule_date', 'doctor_name', 'status')
    list_filter = ('status', 'service__subcategory__category', DateFilter)
    search_fields = ('patient__user__first_name', 'patient__user__last_name')
    ordering = ('doctor_schedule__date',)

    def doctor_schedule_date(self, obj):
        return obj.doctor_schedule.date

    def doctor_name(self, obj):
        return obj.doctor_schedule.doctor.user.get_full_name()

    def service_price(self, obj):
        return obj.service.price

    doctor_schedule_date.short_description = 'Date'
    doctor_name.short_description = 'Doctor Name'
    service_price.short_description = 'Price'








