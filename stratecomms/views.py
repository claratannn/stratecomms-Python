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

def portofolio(request):
  return render(request, 'portofolio.html')

def isiPortofolio(request):
  return render(request, 'isiPortofolio.html')

pendaftaran

def pendaftaranBerhasil(request):
  return render(request, 'pendaftaranBerhasil.html')

<<<<<<< HEAD
def adminLogin(request):
  return render(request, 'adminLogin.html')

def adminHome(request):
  return render(request, 'adminHome.html')
=======
def adminArtikel(request):
  return render(request, 'admin/adminArtikel.html')
>>>>>>> b1c1f814263f5dd73c0e62540b23643d60ba0030
