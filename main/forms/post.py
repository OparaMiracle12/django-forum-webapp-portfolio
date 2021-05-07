from django import forms
from .models import Post

class PostForm(model.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {'content': forms.TextArea(attrs = {'col': 80})}