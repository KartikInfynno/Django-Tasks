from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import Contact_Us

name = ""
email = ""
contact_no = 0
issue = ""
description = ""
data_li = []
count_li = [ i for i in range(len(data_li))]


def home(request):
    return HttpResponse("Working")

def contact_us(request):
    form = Contact_Us()
    if request.method == "POST":
        form = Contact_Us(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            global name
            name = cd.get("name")
            global email
            email = cd.get("email")
            global contact_no
            contact_no = cd.get("contact_no")
            global issue
            issue = cd.get("issue")
            global description
            description = cd.get("description")
            data = {"name" : name, "email" : email, "contact_no" : contact_no, "issue" : issue, "description" : description}
            filter_data = list(filter(lambda items: items["email"] == data["email"], data_li))
            global flag
            flag = True
            for i in filter_data:
                for k,v in i.items():
                    if k == 'email':
                        if v == v:
                            flag = False
                            break
                        else:
                            flag = True
                            continue

            if flag:
                data_li.append(data)

            form = Contact_Us()

    # print(type(form))
    context = {
        "form" : form,
        "data" : data_li,
        "count" : count_li
    }
    return render(request, "temp.html", context)
