from django.shortcuts import render, redirect
from .forms import CartForm, ProductForm,Filter_Price
from .models import Cart, Product, WishList
# import math
from django.forms.models import model_to_dict
from django.contrib import messages
from django.db.models import Q


def index(request):
    data = Product.objects.all()
    total_itm = Cart.objects.all()
    price_li = []
    li = []
    for x in total_itm:
        price_li.append(model_to_dict(x, fields=None, exclude=None))
    for i in price_li:
        li.append(i['total_price'])

    total_price = sum(li)

    context = {
        'data': data,
        'total_itm': len(price_li),
        'total_price': round(total_price, 2)
    }

    return render(request, 'index.html', context)


def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            prod_img = form.cleaned_data.get('image')
            form = form.save(commit=False)
            form.image = prod_img
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'ecomm/create_product.html', context)


def cart(request):
    coupen_code = 'LUCKY2022'
    price_li = []
    li = []
    data = Cart.objects.all()
    message = ''
    for x in data:
        price_li.append(model_to_dict(x, fields=None, exclude=None))
    for i in price_li:
        li.append(i['total_price'])

    # if 'code' in request.GET:
    #     code = request.GET['code']
    #     if code == coupen_code:
    #         def p(x): return x/100
    #         p10 = p(10)
    #         total = sum(li) - (sum(li)*p10)
    #         # print(total)
    #         message = "congratulations you got 10% off"

    #     else:
    #         message = "Invalid CoupenCode"
    #         total = sum(li)

    # else:
    total = sum(li)

    context = {
        'data': data,
        'total_price': round(total, 2),
        'total_itm': len(price_li),
        'message': message

    }

    return render(request, 'cart.html', context)


def del_item_cart(request, id):
    data = Cart.objects.filter(id=id)
    data.delete()
    return redirect('cart')


def add_to_cart(request, id):
    prod = Product.objects.get(id=id)
    form = CartForm()
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            qty = form.cleaned_data.get('quantity')
            total = qty * prod.price
            form = form.save(commit=False)
            form.product = prod
            form.total_price = total
            form.save()
            return redirect('cart')

    context = {
        'form': form,
    }

    return render(request, 'ecomm/add_to_cart.html', context)


def wishlist(request):
    price_li = []
    li = []
    dat = Cart.objects.all()
    data = WishList.objects.all()
    for x in dat:
        price_li.append(model_to_dict(x, fields=None, exclude=None))
    for i in price_li:
        li.append(i['total_price'])

    context = {
        'data' : data,
        'total_price' : round(sum(li), 2),
        'total_itm': len(price_li),
    }
    return render(request, 'wishlist.html', context)


def add_wishlist(request,id):
    prod = Product.objects.get(id=id)
    # data = WishList.objects.get(product= prod)
    add = WishList.objects.create(product= prod)
    return redirect('wishlist')

def del_wishlist(request,id):
    data = WishList.objects.filter(id=id)
    data.delete()
    return redirect('wishlist')

def shop(request):
    price_li = []
    li = []
    dat = Cart.objects.all()
    # data = WishList.objects.all()
    for x in dat:
        price_li.append(model_to_dict(x, fields=None, exclude=None))
    for i in price_li:
        li.append(i['total_price'])
    if 'search' in request.GET:
        search = request.GET['search']
        multiple_q = Q(Q(category__icontains=search))
        data = Product.objects.filter(multiple_q).order_by('price')

    elif ('start' in request.GET and 'end' in request.GET):
        start = float(request.GET['start'])
        end = float(request.GET['end'])
        data = Product.objects.filter(price__range=(start, end))

    else:
        data = Product.objects.all()



    context = {
        'data': data,
        'total_price' : round(sum(li), 2),
        'total_itm': len(price_li),
    }
    return render(request, 'shop.html',context)
