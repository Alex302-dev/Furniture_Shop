from django.urls import path
from . import views

app_name = 'guest_frontend'

urlpatterns = [
    path('', views.index, name='index'),
]