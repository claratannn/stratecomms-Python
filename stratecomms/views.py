from django.shortcuts import render

def home(request):
  return render(request, 'base.html')

def homepage(request):
  return render(request, 'homepage.html')