from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', "slug", "forum", "date_updated")
    search_fields = ("title",)
    autocomplete_fields = ('forum',)
    list_filter = ('date_updated',)

admin.site.register(models.Post, PostAdmin)