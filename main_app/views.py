from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Leftover

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def leftovers_index(request):
  leftovers = Leftover.objects.all()
  return render(request, 'leftovers/index.html', { 'leftovers': leftovers})

def leftovers_detail(request, leftover_id):
  leftover = Leftover.objects.get(id=leftover_id)
  return render(request, 'leftovers/detail.html', { 'leftover': leftover })

class LeftoverCreate(CreateView):
  model = Leftover
  fields = '__all__'
  success_url = '/leftovers/'

class LeftoverUpdate(UpdateView):
  model = Leftover
  field = ['name', 'expiration', 'storage', 'servings']

class LeftoverDelete(DeleteView):
  model = Leftover
  success_url = '/leftovers/'