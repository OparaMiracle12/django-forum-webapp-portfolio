from django.db import models
from .forum_category import ForumCategory

class Forum(models.Model):
    name = models.CharField(max_length = 32, unique = True)
    category = models.ForeignKey(ForumCategory, on_delete = models.CASCADE)
    slug = models.SlugField(max_length = 50, unique = True)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self, *args, **kwargs):
        return reverse('forum_detail', args = [str(self.slug)])

    class Meta:
        verbose_name_plural = 'forums'
        ordering = ['name']

