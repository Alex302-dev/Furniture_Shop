from django.shortcuts import render

def home(request):
    return render(request, 'furniture_shop/base.html')
