from django import forms
from .models import Crud

class Crud_Form_Create(forms.ModelForm):
    class Meta:
        model = Crud
        fields = "__all__"

