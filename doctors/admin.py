from django.contrib import admin
from django.core.files.storage import default_storage
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .models import Specialization, Category, AcademicDegree, Type, DoctorProfile, DoctorSchedule
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from datetime import date, timedelta

admin.site.register(Category)
admin.site.register(AcademicDegree)
admin.site.register(Type)


@admin.register(DoctorSchedule)
class DoctorScheduleAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'date', 'start_time', 'end_time')
    list_filter = ('doctor',)


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_category',)
    list_filter = ('service_category',)


class ExperienceFilter(admin.SimpleListFilter):
    title = _('Experience')
    parameter_name = 'experience'

    def lookups(self, request, model_admin):
        years = [1, 5, 10, 20, 50]
        return [(str(number), _(f'≥ {number} year(s)')) for number in years]

    def queryset(self, request, queryset):
        if self.value():
            years = int(self.value())
            current_date = date.today()
            min_experience_date = current_date - timedelta(days=365 * years)
            return queryset.filter(experience__lte=min_experience_date)
        return queryset


class DoctorScheduleInline(admin.TabularInline):
    model = DoctorSchedule
    extra = 0


@admin.register(DoctorProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'get_specializations_display',
                    'experience', 'category', 'academic_degree', 'get_types_display')
    list_filter = ('specializations', ExperienceFilter, 'category', 'academic_degree', 'types')
    inlines = [DoctorScheduleInline]

    def get_types_display(self, obj):
        return mark_safe(',<br>'.join(str(type)
                                      for type in obj.types.all()))

    get_types_display.short_description = _('Type')

    def get_specializations_display(self, obj):
        return mark_safe(',<br>'.join(str(specialization)
                                      for specialization in obj.specializations.all()))

    get_specializations_display.short_description = _('Specialization')


@receiver(pre_delete, sender=DoctorProfile)
def delete_doctor_photo(sender, instance, **kwargs):
    if instance.photo:
        default_storage.delete(instance.photo.path)
