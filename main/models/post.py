from django.db import models
from .forum import Forum
import uuid

class Post(models.Model):
    title = models.CharField(max_length = 32),
    slug = models.SlugField(max_length = 200, blank=True, null=True),
    content = models.TextField(max_length = 200)
    forum = models.ForeignKey(Forum, on_delete = models.CASCADE)
    date_updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('forum_detail', kwargs = {'pk': self.id, 'post': self.slug})

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(f"{uuid.uuid4()}-{self.title}")  

        super(Post, self,).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "posts"
        ordering = ['-date_updated']

    