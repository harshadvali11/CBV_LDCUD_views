from django.shortcuts import render

# Create your views here.
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *

from django.urls import reverse_lazy

class HomeView(View):
    def get(self,request):
        return render(request,'app/home.html')


class SchoolListView(ListView):
    model=School
    context_object_name='schools'
    

class SchoolDetailView(DetailView):
    model=School
    context_object_name='school'

class SchoolCreateView(CreateView):
    model=School
    fields=['name','principal','location']


class SchoolUpdateView(UpdateView):
    model=School
    fields=['name','principal','location']


class SchoolDeleteView(DeleteView):
    model=School
    context_object_name='school'
    success_url=reverse_lazy('app:list')












