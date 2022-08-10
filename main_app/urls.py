from django.urls import path
from . import views


urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('leftovers/', views.leftovers_index, name='leftovers_index'),
  path('leftovers/<int:leftover_id>/', views.leftovers_detail, name='leftovers_detail'),
  path('leftovers/create/', views.LeftoverCreate.as_view(), name='leftovers_create'),
  path('leftovers/<int:pk>/update/', views.LeftoverUpdate.as_view(), name='leftovers_update'),
  path('leftovers/<int:pk>/delete/', views.LeftoverDelete.as_view(), name='leftovers_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]
