from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('predictions/', views.predictions),
    path('customer/', views.customer),
]