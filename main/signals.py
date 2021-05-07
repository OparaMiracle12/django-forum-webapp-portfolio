from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models

@receiver(post_save, sender = models.Post)
def generate_post_image(sender, instance, created, *args, **kwargs):
    models.PostImage.objects.save()