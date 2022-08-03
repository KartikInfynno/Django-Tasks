from django.shortcuts import redirect, render

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
