from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Leftover

# Create your views here.

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def leftovers_index(request):
  leftovers = Leftover.objects.filter(user=request.user)
  return render(request, 'leftovers/index.html', { 'leftovers': leftovers})

@login_required
def leftovers_detail(request, leftover_id):
  leftover = Leftover.objects.get(id=leftover_id)
  return render(request, 'leftovers/detail.html', { 'leftover': leftover })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('leftovers_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class LeftoverCreate(LoginRequiredMixin, CreateView):
  model = Leftover
  fields = ['name', 'expiration', 'storage', 'servings']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class LeftoverUpdate(LoginRequiredMixin, UpdateView):
  model = Leftover
  fields = ['name', 'expiration', 'storage', 'servings']

class LeftoverDelete(LoginRequiredMixin, DeleteView):
  model = Leftover
  success_url = '/leftovers/'