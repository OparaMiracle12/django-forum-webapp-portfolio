from django import forms
from .models import PostImage

class PostForm(model.ModelForm):
    class Meta:
        model = Post
        fields = ['image']