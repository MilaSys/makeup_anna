from django.urls import path

from . import views

app_name = 'feedback'

urlpatterns = [
    path('', views.gallery, name='feed'),
    path('customer', views.customer, name='customer'),
]