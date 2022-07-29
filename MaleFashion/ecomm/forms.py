from django import forms
from .models import Cart, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        field = ['quantity']
        exclude = ['product','total_price']

class Filter_Price(forms.Form):
    start_price = forms.IntegerField()
    end_price = forms.IntegerField()
