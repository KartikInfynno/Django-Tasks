from django import forms
from .models import Crud

class Crud_Form(forms.ModelForm):
    class Meta:
        model = Crud
        fields = ('first_name', "last_name", 'contact_no', 'age', 'gender')
        widgets = {
            'first_name' : forms.TextInput(attrs={"class" : "form-control","placeholder" : "Enter First Name"}),
            'last_name' : forms.TextInput(attrs={"class" : "form-control","placeholder" : "Enter Last Name"}),
            'contact_no' : forms.TextInput(attrs={"class" : "form-control","placeholder" : "Enter Contact No"}),
            'age' : forms.TextInput(attrs={"class" : "form-control","placeholder" : "Enter Age"}),
            'gender' : forms.Select(attrs={"class" : "form-select form-select-lg mb-3"}),
        }
