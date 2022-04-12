from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from myapp.models import Patient
from myapp.forms import PatientForm
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy

# Create your views here.

def index(request):
    return render(request,'index.html')

def firstpage(request):

    return render(request,'myapp/page.html')

class PatientCreateView(CreateView):

    model = Patient
    fields = '__all__'
    success_url = reverse_lazy('myapp:list')

class PatientListView(ListView):

    model = Patient
    context_object_name = 'tags'

class PatientDetailView(DetailView):

    model = Patient
    context_object_name = 'tags2'




