from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('leftovers/', views.leftovers_index, name='leftovers_index'),
  path('leftovers/create/', views.LeftoverCreate.as_view(), name='leftovers_create'),
]
