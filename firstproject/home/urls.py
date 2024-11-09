from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Service_details/', views.Service_details, name='Service_details'),
]
