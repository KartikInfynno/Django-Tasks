from .models import Sort
from django import forms
from datetime import date


class Sort_form(forms.ModelForm):
    class Meta:
        model = Sort
        fields = ['name', 'email', 'dob']
        widgets = {
            'dob': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date',
                       'max': date.today()
                       }),
            'name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter Name',
                       'type': 'text'}),
            'email': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Enter Email',
                       'type': 'email'})}
