from django.contrib import admin
from .models import Banner, RotationInterval


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')


@admin.register(RotationInterval)
class RotationIntervalAdmin(admin.ModelAdmin):
    list_display = ('interval',)
