from django.shortcuts import render
from .pages.pendaftaran import *

def home(request):
  return render(request, 'base.html')

def homepage(request):
  return render(request, 'homepage.html')

def jadwalSertifikasi(request):
  return render(request,'jadwalSertifikasi.html')

def artikel(request):
  return render(request, 'artikel.html')

def isiArtikel(request):
  return render(request, 'isiArtikel.html')

pendaftaran

def pendaftaranBerhasil(request):
  return render(request, 'pendaftaranBerhasil.html')
