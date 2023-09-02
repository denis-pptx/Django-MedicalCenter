from django.contrib import admin
from .models import Service, SubCategory, Category
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage


class SubCategoryInline(admin.StackedInline):
    model = SubCategory
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_subcategories_count')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SubCategoryInline]

    def get_subcategories_count(self, obj):
        return obj.subcategory_set.count()

    get_subcategories_count.short_description = 'Subcategories Count'


@receiver(pre_delete, sender=Category)
def delete_category_image(sender, instance, **kwargs):
    if instance.image:
        default_storage.delete(instance.image.path)


class ServiceInline(admin.StackedInline):
    model = Service
    extra = 0


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'get_services_count')
    list_filter = ('category',)
    search_fields = ('name',)
    inlines = [ServiceInline]

    def get_services_count(self, obj):
        return obj.service_set.count()

    get_services_count.short_description = 'services count'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_category', 'subcategory', 'price')
    list_filter = ('subcategory__category', 'subcategory')

    def get_category(self, obj):
        return obj.subcategory.category

    get_category.short_description = 'Category'
