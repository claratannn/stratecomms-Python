from django.shortcuts import render
from .pages.pendaftaran import *

def homepage(request):
  # cursor.execute('select * from peserta')
  # data = cursor.fetchall()
  # print(data)

  # context = {
  #   'data' : data
  # }
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

def adminArtikel(request):
  return render(request, 'admin/adminArtikel.html')
