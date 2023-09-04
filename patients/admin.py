from django.contrib import admin

from services.models import Service
from .models import PatientProfile
from django import forms


# class ServiceChoiceField(forms.ModelMultipleChoiceField):
#     def label_from_instance(self, obj):
#         return f'{obj.name} ({obj.price})'
#
#
# class OrderAdminForm(forms.ModelForm):
#     services = ServiceChoiceField(queryset=Service.objects.all())
#
#     class Meta:
#         model = Order
#         fields = '__all__'
#
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     form = OrderAdminForm
#     list_display = ('__str__', 'created_at', 'updated_at')
#     list_filter = ('created_at', 'updated_at')
#
#
# class OrderInline(admin.TabularInline):
#     model = Order
#     form = OrderAdminForm
#     extra = 0
#     fields = ('services', 'created_at', 'updated_at')
#     readonly_fields = ('created_at', 'updated_at')


# @admin.register(PatientProfile)
# class PatientAdmin(admin.ModelAdmin):
#     list_display = ('__str__', 'date_of_birth', 'get_order_count')
#     inlines = [OrderInline]
#
#     def get_order_count(self, obj):
#         return obj.order_set.count()
#
#     get_order_count.short_description = 'Orders'
