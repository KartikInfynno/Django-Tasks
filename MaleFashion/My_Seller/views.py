from django.shortcuts import render,redirect
from .models import Add_Product
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from Auths.models import My_User

def add_product(request):
    form = ProductForm
    user = request.user
    # print(user)

    if request.method == 'POST':
         form = ProductForm(request.POST,request.FILES)
         user = request.user
         user = My_User.objects.get(pk=request.user.id)

         if form.is_valid():
             img = form.cleaned_data.get('image')
             img2 = form.cleaned_data.get('image2')
             img3 = form.cleaned_data.get('image3')

             form = form.save(commit=False)
             form.image = img
             form.user= user
             form.save()
             return redirect('index')

    return render(request, 'seller/add_product.html', { 'form' : form })
