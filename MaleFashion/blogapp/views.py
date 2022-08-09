import random
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from Auths.models import My_User
from .forms import Post_Blog
from .models import Blogs,Comments,Fav_Blogs, IP_Model
import json
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms.models import model_to_dict

def blog_index(request):
    if 'search' in request.GET:
        search = request.GET['search']
        # multiple_q = Q(Q(category__icontains=search))
        if search == 'not_approved':
            data = Blogs.objects.filter(is_approved=False)
        elif search == 'approved':
            data = Blogs.objects.filter(is_approved=True)
        else:
            data = Blogs.objects.filter(title__icontains=search,is_approved=True)
        p = Paginator(data,9)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
    else:
        data = Blogs.objects.all()
        p = Paginator(data,9)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
    li = []
    fav_blog = Fav_Blogs.objects.filter(user = request.user.id)
    for i in fav_blog:
        if i.blog in page_obj:
            li.append(i.blog)

    context = {
        'data': page_obj,
        'fav_blog': li
    }
    return render(request, 'blogapp/blog-index.html', context)


def my_blogs(request):
    # user =
    data = Blogs.objects.filter(user = request.user.id)

    context = {
        'data': data,
    }
    return render(request, 'blogapp/my-blogs.html', context)

def blog_create(request):
    form = Post_Blog
    user = request.user
    if request.method == 'POST':
        form = Post_Blog(request.POST,request.FILES)
        user = request.user
        user = My_User.objects.get(pk = request.user.id)

        if form.is_valid():
            img = form.cleaned_data.get('b_image')
            form = form.save(commit=False)
            form.b_image = img
            form.user = user
            form.save()
            return redirect('blog')

    context = {
        'form': form,
    }
    return render(request, 'blogapp/blog-create.html',context)

'''
    View of Admin Approval
    When u render the template it'll show checked if it is apprved by the id of the checkbox id
    Check blogapp/admin-approval.html file for the template
'''

def admin_approval(request):
    # get all Blog List

    blog_list = Blogs.objects.all().order_by('-pub_date')

    # Check if the user is superuser or not
    if request.user.is_superuser:

        if request.method == 'POST':

            # Make Al is_approved Fields Uchecked on the server side
            #  but on the template side it is still checked
            blog_list.update(is_approved=False)

            # now it'll get the id of the checkbox
            # which is already checked by server side when this template was rendered
            # it'lll get id by name that we've put on the templated on input tag
            # we used name as boxes here
            id_list = request.POST.getlist('boxes')

            # id_list will get the list of the checkbox whichh is checked
            print(id_list)

            # Now we itrate id_list and filter that id in blogs and make them approved again
            # Because we make all the Blogs not_approved First

            for i in id_list:

                # This Queryset Which will filter the Blogs Tabke By Id And
                #if the id matches it'll make them approved

                Blogs.objects.filter(id=i).update(is_approved=True)
            messages.success(request, "Blog Request Approved")
            return redirect('admin_approve')
        else:
            context = {
                'blog_list': blog_list,
            }
            return render(request, 'blogapp/admin-approval.html',context)
        context = {
            'blog_list': blog_list,
        }
        return render(request, 'blogapp/admin-approval.html',context)
    else:
        messages.success(request,('You are not authorized to view this page'))
    return render(request, 'blogapp/admin-approval.html')


def blog_details(request,id):
    get_blog = Blogs.objects.get(id=id)
    if 'name' in request.GET and 'comment' in request.GET:
        name = request.GET['name']
        comment = request.GET['comment']
        if len(name) > 0 and len(comment) > 0:
            Comments.objects.create(user=request.user, blog=get_blog , name=name, comment=comment)
            messages.success(request, 'Commented Successfully Your Comment will be under moderation.')
        else:
            messages.error(request, 'Comment Invalid')
        return redirect(request.META['HTTP_REFERER'])

    if request.user == get_blog.user:
        comment = Comments.objects.filter(blog=get_blog)
        if request.method == 'POST':

            approve_id = request.POST.get('boxes')

            if approve_id is None:
                Comments.objects.filter(id=approve_id).update(is_approved=False)

            else:
                Comments.objects.filter(id=approve_id).update(is_approved=True)
            messages.success(request, 'Comments Status updated successfully')
    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return f'{ip}'
    ip = get_ip(request)
    user = My_User.objects.get(id=request.user.id)
    u = IP_Model(ip=ip,user=user,blog=get_blog)
    multiple_q = Q(Q(ip__icontains=ip,user=user,blog=get_blog))
    result = IP_Model.objects.filter(multiple_q)
    if len(result) >= 1:
        print('user exist')
    else:
        u.save()
        count = IP_Model.objects.filter(blog=get_blog).count()
        get_blog.count = count
        get_blog.save()
    usr_blog1 = Blogs.objects.filter(user=get_blog.user).values()
    usr_blog2 = Blogs.objects.filter(user=get_blog.user).values()
    comment = Comments.objects.filter(blog=get_blog)
    context = {
        'blog_list': get_blog,
        'comment':  comment,
        'total_comments': len(comment),
        'blog1': random.choice(usr_blog1),
        'blog2': random.choice(usr_blog2),
    }
    return render(request, 'blogapp/blog-details.html',context)

def blog_delete(request,id):
    data = Blogs.objects.get(id=id).delete()
    # data.delete()
    return redirect('my_blog')


def add_fav_blog(request,id):
    user = My_User.objects.get(id=request.user.id)
    blog = Blogs.objects.get(id=id)
    Fav_Blogs.objects.create(user=user,blog=blog)
    messages.success(request,"Successfully Added To Fav Blog")
    return redirect('fav_blog')

def fav_blogs(request):
    fav_blogs = Fav_Blogs.objects.filter(user=request.user.id)
    context = {
        'data': fav_blogs,
    }
    return render(request, 'blogapp/fav-blogs.html',context)

def rem_fav_blog(request,id):
    blog = Fav_Blogs.objects.get(pk=id)
    # fav_blogs.get(id=id)
    blog.delete()
    messages.success(request,'Removed from Favourite Blog')
    return redirect('fav_blog')
