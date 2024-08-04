from django import forms
from .models import Profile


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['textField', 'phone', 'image']