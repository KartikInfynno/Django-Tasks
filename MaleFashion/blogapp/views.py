
from django.shortcuts import redirect, render
from django.contrib import messages
from Auths.models import My_User
from .forms import Post_Blog
from .models import Blogs


def blog_index(request):
    data = Blogs.objects.all()

    context = {
        'data': data,
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

    blog_list = Blogs.objects.all()[::-1]

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

            messages.success(request,('Admin Request Approved'))
            return redirect('admin_approve')
            pass
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
