from django.shortcuts import redirect, render
from Auths.models import My_User
from My_Seller.models import Add_Product
from django.contrib.auth.decorators import login_required
from .models import Cart,WishList
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.conf import settings
import random
from django.core.mail import send_mail
from blogapp.models import Blogs


def index(request):
    data = Add_Product.objects.all()
    blog = Blogs.objects.all()
    context = {
        'data' : random.choices(data, k=4),
        # 'blog' : random.choices(blog, k=3)
    }
    return render(request,"index.html",context)

@login_required(login_url='login')
def product_details(request,id):
    data = Add_Product.objects.get(id=id)
    context = {
        'details' : data,
    }
    return render(request,"product_details.html",context)

@login_required(login_url='login')
def shop(request):
    price_li = []
    li = []
    dat = Cart.objects.filter(user=request.user.id)
    for x in dat:
        price_li.append(model_to_dict(x, fields=None, exclude=None))
    for i in price_li:
        li.append(i['total_price'])
    if 'search' in request.GET:
        search = request.GET['search']
        multiple_q = Q(Q(category__icontains=search))
        data = Add_Product.objects.filter(multiple_q).order_by('price')
        p = Paginator(data, 9)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)

    elif ('start' in request.GET and 'end' in request.GET):
        start = float(request.GET['start'])
        end = float(request.GET['end'])
        data = Add_Product.objects.filter(price__range=(start, end))
        p = Paginator(data, 9)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)

    else:
        data = Add_Product.objects.all()
        p = Paginator(data, 9)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)

    context = {
        'data' : page_obj,
        'total_price' : round(sum(li), 2),
        'total_itm': len(price_li),
    }
    return render(request,"shop.html",context)



@login_required(login_url='login')
def cart(request):
    price_li = []
    li = []
    data = Cart.objects.filter(user=request.user.id)
    for x in data:
        price_li.append(model_to_dict(x, fields=None, exclude=None))
    for i in price_li:
        li.append(i['total_price'])

    total_price = sum(li)

    context = {
        'data' : data,
        'total_itm': len(price_li),
        'total_price': round(total_price, 2)
    }
    return render(request,"cart.html",context)

@login_required(login_url='login')
def wishlist(request):
    price_li = []
    li = []
    data = WishList.objects.filter(user=request.user.id)
    dat = Cart.objects.filter(user=request.user.id)

    for x in dat:
        price_li.append(model_to_dict(x, fields=None, exclude=None))
    for i in price_li:
        li.append(i['total_price'])
    # print(price_li)
    total_price = sum(li)

    context = {
        'data' : data,
        'total_itm': len(price_li),
        'total_price': round(total_price, 2)
    }
    return render(request,"wishlist.html",context)


@login_required(login_url='login')
def add_cart(request,id):
    user = request.user
    user = My_User.objects.get(pk=request.user.id)
    product = Add_Product.objects.get(id=id)
    cart = Cart.objects.create(user=user,product=product,quantity=1,total_price=product.price)
    return redirect('cart')

@login_required(login_url='login')
def add_wishlist(request,id):
    user = request.user
    user = My_User.objects.get(pk=request.user.id)
    product = Add_Product.objects.get(id=id)
    wishlist = WishList.objects.create(user=user,product=product)
    return redirect('wishlist')

@login_required(login_url='login')
def del_cart(request,id):
    cart = Cart.objects.get(pk = id)
    cart.delete()
    return redirect('cart')

@login_required(login_url='login')
def del_wishlist(request,id):
    wishlist = WishList.objects.get(pk = id)
    wishlist.delete()
    return redirect('wishlist')

@login_required(login_url='login')
def contact_us(request):
    price_li = []
    li = []
    dat = Cart.objects.filter(user=request.user.id)
    # data = WishList.objects.all()h
    for x in dat:
        price_li.append(model_to_dict(x, fields=None, exclude=None))
    for i in price_li:
        li.append(i['total_price'])

    if 'F_Name' in request.GET and 'F_Email' in request.GET and 'F_Description' in request.GET:
        f_name = request.GET['F_Name']
        f_email = request.GET['F_Email']
        f_description = request.GET['F_Description']

        subject = f'Hello {f_name}'
        message = f'Hi {f_name}, Thank you for Contacting us Your Message was {f_description}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [f_email, ]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('contact_us')
    context = {
        'total_price' : round(sum(li), 2),
        'total_itm': len(price_li),
    }
    return render(request, 'contact_us.html', context)


def test(request):
    return render(request, 'test.html')



