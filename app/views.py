from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *
from django.urls import reverse_lazy


class School_list(ListView):        ## listView is Static Url Suffix
    model = School
    context_object_name = 'allSO' 

class School_detail(DetailView):    ## DetailView is Dynamic Url Suffix
    model = School
    context_object_name = 'SDO'     #^ SDO --> school details object


class School_create(CreateView):    ## CreateView is Static Url Suffix
    model = School
    fields = '__all__'


class School_update(UpdateView):    ## UpdateView is Dynamic Url Suffix
    model = School
    fields = '__all__'


class School_delete(DeleteView):    ## DeleteView is Dynamic Url Suffix
    model = School
    context_object_name = 'dso'
    success_url=reverse_lazy('School_list')  ## after deleting reverse_lazy is taking the control to SchoolList

