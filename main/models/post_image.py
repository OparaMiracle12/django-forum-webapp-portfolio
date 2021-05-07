from django.db import models
from .post import Post
from PIL import Image

class PostImage(models.Model):
    image = models.ImageField(default = 'default.jpeg', upload_to = "posts")
    post = models.ForeignKey(Post, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.post.title} image"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        dimensions = (300, 300)
        image = Image.open(self.image.path)
        image.thumbnail(dimensions)
        image.save(self.image.path)
