from typing import ContextManager
from django.shortcuts import render, get_object_or_404
from django.views import View
from hospital.models import Hospital
from hospital.forms import HospitalForm, SearchForm
from asks.forms import AskForm

def hospital_list_view(request):
    if request.method == 'GET':
        hospital = Hospital.objects.all()
        return render(request, 'hospital/list_view.html', context={'hospital': hospital})
    elif request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            search_param = search_form.cleaned_data.get('search_param')
            filtered_posts = Hospital.objects.filter(title__icontains=search_param)
            return render(request, 'hospital/list_view.html', context={'hospital': filtered_posts})

def hospital_detail_view(request, id):
    hosp = get_object_or_404(Hospital, id=id)
    asks = hosp.asks.filter(active=True)
    if request.method == 'POST':
        ask_form = AskForm(request.POST)
        if ask_form.is_valid():
            new_ask = ask_form.save(commit=False)
            new_ask.hosp = hosp
            new_ask.save()
        return render(request, 
                'hospital/hospital_detail.html', 
                {'hosp':hosp,
                'asks': asks,
                'ask_form': ask_form,
                'new_ask': new_ask})
    else:
        ask_form = AskForm()
        return render(request, 
                'hospital/hospital_detail.html', 
                {'hosp':hosp,
                'asks': asks,
                'ask_form': ask_form,
                })




