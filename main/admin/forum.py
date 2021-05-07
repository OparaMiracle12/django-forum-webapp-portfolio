from django.contrib import admin
from . import models

class ForumAdmin(admin.ModelAdmin):
    list_display = ('name', "slug", "category")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    autocomplete_fields = ('category',)

admin.site.register(models.Forum, ForumAdmin)