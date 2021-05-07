from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from .post import Post

class Comment(MPTTModel):
    content = models.TextField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to = "comments", blank = True, null = True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    parent = TreeForeignKey('self', on_delete = models.CASCADE, null = True, blank = True, related_name = "children")

    def __str__(self):
        return self.content

    class MPTTMeta:
        verbose_name_plural = "comments"
        order_insertion_by = ['-date_added']