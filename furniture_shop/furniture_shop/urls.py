from django.contrib import admin
from django.urls import path, include
from furniture_shop.guest_frontend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
