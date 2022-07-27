from unittest.util import _MAX_LENGTH
from django import forms


CHOICES = (
    ("Technical Issue", "Technical Issue"),
    ("Product_Issue", "Product_Issue"),
    ("Manufacturing_Issue", "Manufacturing_Issue"),
)


class Contact_Us(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class" : "form-control","placeholder" : "Enter Username"}))
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={"class" : "form-control","placeholder" : "Enter Email"}))
    contact_no = forms.IntegerField(widget=forms.TextInput(attrs={"class" : "form-control","placeholder" : "Enter Contact No"}))
    issue = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={"class" : "form-select form-select-lg mb-3"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class" : "form-control","placeholder" : "Description","style": "height:100px;width:auto"}))
