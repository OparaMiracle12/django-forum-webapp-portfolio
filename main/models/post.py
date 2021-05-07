from django.core.validators import MinValueValidator
from django.db import models
from .forum import Forum
import uuid

class Post(models.Model):
    title = models.CharField(max_length = 100, unique=True)
    slug = models.SlugField(max_length = 50, blank=True, null=True)
    content = models.TextField(max_length = 200)
    forum = models.ForeignKey(Forum, on_delete = models.CASCADE)
    date_updated = models.DateTimeField(auto_now = True)
    likes = models.PositiveSmallIntegerField(default=0, validators = [MinValueValidator(0)])
    dislikes = models.PositiveSmallIntegerField(default=0, validators = [MinValueValidator(0)])
    
    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('post_detail', kwargs = {'pk': self.id, 'post': self.slug})

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(f"{uuid.uuid4()}-{self.title}")  

        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date_updated']
        verbose_name_plural = "posts"

    