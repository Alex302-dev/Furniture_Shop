from django.shortcuts import render

def index(request):
    return render(request, 'guest_frontend/index.html')