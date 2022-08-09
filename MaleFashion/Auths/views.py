from django.shortcuts import render,redirect
from .forms import Create_User,Login_User
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate,login as login_user, logout
from django.contrib.auth.decorators import login_required


def user_register(request):
    form = Create_User()
    if request.method == "POST":
        form = Create_User(request.POST)

        if form.is_valid():
            to_mail = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            subject = "Welcome To MaleFashion!"
            message = f"{username} You have been successfully registered"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [to_mail], fail_silently=False)
            print(form)
            form.save()
            form.save()
            messages.success(request, "Successfully registered. Please Login to Continue...")
            return redirect("login")

    context = {
        'form': form,
    }

    return render(request,"Auths/register.html",context)


def user_login(request):
    form = Login_User()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login_user(request, user)
            # if user.user_type == "Seller Account":
            messages.success(request, "Logged in Successfully")
            return redirect('index')

        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    context = {
        "form" : form,
    }

    return render(request,"Auths/login.html",context)

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("index")
