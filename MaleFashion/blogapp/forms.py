from django import forms
from .models import Blogs


class Post_Blog(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = '__all__'
        exclude = ['user','is_approved']
