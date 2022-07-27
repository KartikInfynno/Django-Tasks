from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import login_page

const_user = "admin"
const_pass = "admin"

l_flag = False

def login_system(request):
    global l_flag
    if l_flag == True:
        return redirect("profile")
    form = login_page()
    if request.method == "POST":
        form = login_page(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            l_flag = False
            if username == const_user and password == const_pass:
                l_flag = True
                return redirect('profile')

            else:
                l_flag = False
                error = '''<a href="http://127.0.0.1:8000/login/">Invalid Credentials Tap Here To Login Again</a>'''
                return HttpResponse(error)

    
    context = {
        "form" : form
    }

    return render(request,'login.html',context)


def profile_page(request):

    if l_flag == False:
        return HttpResponse("Please Login To See Your Profile")
    context = {
        "name" : const_user,
        "flag" : l_flag
    }
    return render(request,"profile.html", context)