from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')
def dashboard(request):
    return render(request, 'pages/dashboard.html')
def prac(request):
    return render(request, 'pages/prac.html')
