from django.shortcuts import redirect, render
from .forms import Sort_form
from .models import Sort
from datetime import datetime, date
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q



def find_age(born):
    born = datetime.strptime(born, "%Y-%m-%d").date()
    today = date.today()
    age = today.year - born.year - \
        ((today.month, today.day) < (born.month, born.day))

    return age

def index(request):
    filter_data_list = []
    data_list = []
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(name__icontains=q) | Q(email__icontains=q))
        data = Sort.objects.filter(multiple_q)
        for x in data:

            filter_data_list.append(model_to_dict(x,fields=None,exclude=None,))
        for i in filter_data_list:
            age = find_age(str(i['dob']))
            i['age'] = age
        p = Paginator(filter_data_list, 5)
        page_number = request.GET.get('page')
        try:
            page_obj = p.get_page(page_number)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)
    else:
        data = Sort.objects.all()
        for x in data:
            data_list.append(model_to_dict(x, fields=None, exclude=None))

        for i in data_list:
            age = find_age(str(i['dob']))
            i['age'] = age

        p = Paginator(data_list,5)
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
