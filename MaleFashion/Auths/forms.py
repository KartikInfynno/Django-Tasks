from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from .models import My_User

class Create_User(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'type':'password','placeholder' : 'Enter Password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'type':'password','placeholder' : 'Confirm Password'}),
    )

    class Meta:
        model = My_User
        fields = ('username','first_name','last_name','email','user_type')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg','placeholder' : 'Enter Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg','placeholder' : 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg','placeholder' : 'Enter Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg','placeholder' : 'Enter Email Address'}),
            'user_type': forms.Select(attrs={'class': 'form-control form-control-lg','placeholder' : 'Select Account Type'}),
        }

class Update_User(UserChangeForm):
    class Meta:
        Model = My_User
        fields = ('email','password')

class Login_User(AuthenticationForm):
    pass
