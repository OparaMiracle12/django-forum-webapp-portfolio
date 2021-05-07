from django.contrib import admin
from . import models

class ForumCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(models.ForumCategory, ForumCategoryAdmin)
