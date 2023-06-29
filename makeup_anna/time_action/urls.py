from django.urls import path

from .views import action

app_name = 'action'

urlpatterns = [
    path('', action, name='time'),
]
