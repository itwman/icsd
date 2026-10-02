from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Book, BookCategory

admin.site.register(BookCategory, ModelAdmin)


@admin.register(Book)
class BookAdmin(ModelAdmin):
    list_display = ("title", "authors", "category", "download_count", "is_published")
    search_fields = ("title", "authors")
