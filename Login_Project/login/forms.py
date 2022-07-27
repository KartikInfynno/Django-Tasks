from tkinter import Widget
from django import forms

class login_page(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
    # error_messages = {
    #     'name': {
    #         'max_length': _("This writer's name is too long."),
    #     },
    # }
