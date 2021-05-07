from django import forms
from .models import Comment
from mptt import TreeNodeChoiceField

class CommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset = Comment.objects.all())

    class Meta:
        model = Comment
        fields = ['content', 'image', 'comments', 'parent']
        widgets = {'content': forms.TextArea(attrs = {'col': 80})}