from django.contrib import admin
from . import models

class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post',)
    autocomplete_fields = ('post')    

admin.site.register(models.PostImage)