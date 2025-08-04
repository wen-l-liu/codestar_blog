from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Form for creating and editing comments on blog posts."""
    class Meta:
        model = Comment
        fields = ('body',)
