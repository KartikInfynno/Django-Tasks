from tkinter import W
from django import forms
from .models import Blogs


class Post_Blog(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'b_image', 'descriptions']
        exclude = ['user','is_approved']

        widgets = {
            'title' : forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control form-control-lg', 'placeholder': 'Enter Title'}),
            'b_image' : forms.widgets.ClearableFileInput(attrs={'class': 'form-control form-control-lg','type': 'file'}),
            # 'descriptions' : forms.widgets.ClearableFileInput(attrs={'class': 'form-control form-control-lg m-5','type': 'file'}),
        }
