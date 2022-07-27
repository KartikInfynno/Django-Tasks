from django.shortcuts import redirect, render
from .models import Crud
from .forms import Crud_Form_Create


def index(request):
    data = Crud.objects.all()

    return render(request, "index.html",{ "data" : data })

def create(request):
    form = Crud_Form_Create()
    if request.method == "POST":
        form = Crud_Form_Create(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "form": form,
    }
    return render(request,"create.html", context=context)

def retrive(request,id):
    data = Crud.objects.filter(id=id)

    return render(request,"details.html", {"data": data})

def update(request, id):
    data = Crud.objects.get(id=id)
    # print(type(data))
    form = Crud_Form_Create(instance=data)
    if request.method == "POST":
        form = Crud_Form_Create(request.POST,instance=data)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "form": form,
    }
    return render(request,"create.html", context=context)

def delete(request,id):
    data = Crud.objects.get(id=id)
    data.delete()
    return redirect("index")
