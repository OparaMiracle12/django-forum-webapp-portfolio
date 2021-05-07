from django.db import models
from django.utils.text import slugify

class ForumCategory(models.Model):
    name = models.CharField(max_length = 32)
    description = models.TextField(max_length = 200)
    slug = models.SlugField(max_length = 40, unique = True, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self, *args, **kwargs):
        return reverse('forum_category', kwargs = {'pk': self.pk,'category': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        super(ForumCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'forum categories'
        ordering = ['name']
