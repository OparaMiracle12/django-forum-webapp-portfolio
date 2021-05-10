from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from . import models

# Inlines classes inheriting from TabularInline class
class inForum(admin.TabularInline):
    model = models.Forum
    extra = 1

class inPost(admin.TabularInline):
    model = models.Post
    extra = 1

class inComment(admin.TabularInline):
    model = models.Comment
    extra = 1

class inPostImage(admin.TabularInline):
    model = models.PostImage
    extra = 1

#  Registering models to admins site
@admin.register(models.ForumCategory)
class ForumCategoryAdmin(admin.ModelAdmin):
    inlines = [inForum]
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Forum)
class ForumAdmin(admin.ModelAdmin):
    inlines = [inPost]
    list_display = ('name', "slug", "category")
    list_filter = ('category',)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
   

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [inPostImage, inComment]
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
