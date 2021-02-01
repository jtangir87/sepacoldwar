from django.contrib import admin
from .models import Category, Collection, Keyword, FileType, CatalogItem
# Register your models here.


class CatalogItemAdmin(admin.ModelAdmin):
    list_display = ("accession_number",
                    "obj_name", "file_format")
    list_filter = ["category", "collection",
                   "file_format", "keyword", "accession_date"]
    search_fields = ("obj_name", "accession_number")


admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Keyword)
admin.site.register(FileType)
admin.site.register(CatalogItem, CatalogItemAdmin)
