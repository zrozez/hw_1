from django.shortcuts import render, get_object_or_404
from hospital.models import Hospital
from hospital.forms import HospitalForm, SearchForm
from asks.forms import AskForm

def hospital_list_view(request):
    if request.method == 'GET':
        hospitals = Hospital.objects.all()
        return render(request, 'hospital/list_view.html', context={'hospitals': hospitals})
    elif request.method == 'HOSPITAL':
        search_form = SearchForm(request.HOSPITAL)
        if search_form.is_valid():
            search_param = search_form.cleaned_data.get('search_param')
            filtered_posts = Hospital.objects.filter(title__icontains=search_param)
            return render(request, 'hospital/list_view.html', context={'hospitals': filtered_posts})

def hospital_detail_view(request, id):
    hospital = get_object_or_404(Hospital, id=id)
    asks = hospital.asks.filter(active=True)
    if request.method == 'POST':
        ask_form = AskForm(request.POST)
        if ask_form.is_valid():
            new_ask = ask_form.save(commit=False)
            new_ask.hospital = hospital
            new_ask.save()
            return render(request, 
                'hospital/hospital_detail.html', 
                {'hospital':hospital,
                'asks': asks,
                'ask_form': ask_form,
                'new_ask': new_ask})
    else:
        ask_form = AskForm()
        return render(request, 
                'hospital/hospital_detail.html', 
                {'hospital':hospital,
                'asks': asks,
                'ask_form': ask_form})




