from django.shortcuts import render

from .models import Leftover

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def leftovers_index(request):
  leftovers = Leftover.objects.all()
  return render(request, 'leftovers/index.html', { 'leftovers': leftovers})