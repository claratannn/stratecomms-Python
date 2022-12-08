"""stratecomms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('jadwalSertifikasi/', views.jadwalSertifikasi, name='jadwalSertifikasi'),
    path('artikel/', views.artikel, name='artikel'),
    path('isiArtikel/', views.isiArtikel, name='isiArtikel'),
    path('pendaftaran/', views.pendaftaran, name='pendaftaran'),
    path('pendaftaranBerhasil/', views.pendaftaranBerhasil, name='pendaftaranBerhasil'),
    path('adminLogin/', views.adminLogin, name='adminLogin'),
    path('adminHome/', views.adminHome, name='adminHome'),
    path('adminArtikel/', views.adminArtikel, name='adminArtikel'),
    path('adminJadwal/', views.adminJadwal, name='adminJadwal'),
    path('adminPortofolio/', views.adminPortofolio, name='adminPortofolio'),
    path('portofolio/', views.portofolio, name='portofolio'),
    path('isiPortofolio/', views.isiPortofolio, name='isiPortofolio'),
    path('addArtikel/', views.addArtikel, name='addArtikel'),
    path('editArtikel/', views.editArtikel, name='editArtikel'),
]
