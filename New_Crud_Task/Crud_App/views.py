from django.shortcuts import redirect, render
from .forms import Crud_Form
from .models import Crud



def create(request):
    data = Crud.objects.all()
    form = Crud_Form()
    if request.method == "POST":
        form = Crud_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form": form,
        "data": data,
    }

    return render(request,"index.html",context)

# def retrive(request,id):
#     data = Crud.objects.filter(id=id)
#     return render(request,"retrive.html",{"data":data})


def update(request, id):
    data = Crud.objects.all()
    data_f = Crud.objects.get(pk=id)
    form = Crud_Form(instance=data_f)
    if request.method == "POST":
        form = Crud_Form(request.POST, instance=data_f)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form": form,
        "data" : data,
    }

    return render(request,"index.html",context)

def delete(request, id):
    data = Crud.objects.get(pk=id)
    data.delete()
    return redirect('index')
