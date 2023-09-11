from django.contrib import admin
from news.models import News
from news.common import get_path_to_html


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publish_date', 'file_path')

    def file_path(self, obj):
        return get_path_to_html(obj)

    file_path.short_description = 'File path'

