from gettext import find
from django.shortcuts import redirect, render
from .forms import Sort_form
from .models import Sort
from datetime import datetime, date
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def find_age(born):
    born = datetime.strptime(born, "%Y-%m-%d").date()
    today = date.today()
    age = today.year - born.year - \
        ((today.month, today.day) < (born.month, born.day))

    return age


def index(request):
    data1 = Sort.objects.all()
    data = []
    for x in data1:
        data.append(model_to_dict(x, fields=None, exclude=None))
    for i in data:
        age = find_age(str(i['dob']))
        i['age'] = age
    p = Paginator(data, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {
        'data': page_obj
    }
    return render(request, 'index.html', context)


def add_data(request):
    form = Sort_form()
    if request.method == 'POST':
        form = Sort_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'create.html', {'form': form})


def update_data(request, id):
    data = Sort.objects.get(pk=id)
    form = Sort_form(instance=data)
    if request.method == 'POST':
        form = Sort_form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'create.html', {'form': form})


def delete_data(request, id):
    data = Sort.objects.get(pk=id)
    data.delete()
    return redirect('index')
