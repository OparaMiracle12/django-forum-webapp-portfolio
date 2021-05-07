from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from . import models

@admin.register(models.ForumCategory)
class ForumCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('name', "slug", "category")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    autocomplete_fields = ('category',)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', "slug", 'forum')
    search_fields = ("title",)
    prepopulated_fields = {"slug": ('title',)}
    autocomplete_fields = ("forum",)


@admin.register(models.PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class CommentMPTTAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
