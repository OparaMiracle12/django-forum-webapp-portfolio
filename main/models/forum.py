from django.db import models
from .forum_category import ForumCategory

class Forum(models.Model):
    name = models.CharField(max_length = 32, unique = True)
    category = models.ForeignKey(ForumCategory, on_delete = models.CASCADE)
    slug = models.SlugField(max_length = 50, unique = True, blank=True, null=True)
    

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        super(Forum, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'forums'
        ordering = ['name']

