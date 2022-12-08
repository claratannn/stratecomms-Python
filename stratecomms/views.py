from django.shortcuts import render
from .pages.pendaftaran import *
from .pages.admin.login import *
from .pages.admin.isiArtikel import *
from datetime import datetime

def homepage(request):
  # now = datetime.now()
  # dt_string = now.strftime("%d %B %Y, %H:%M:%S")
  # print("date and time =", dt_string)	  
  # print(dt_string)

  # cursor.execute(f'insert into artikel values(null, "artikel.png", "REFLEKSI STRATECOMMS TAHUN 2021: KEMENTERIAN PEDULI SERTIFIKASI PROFESI DARI BNSP", "Perkembangan sertifikasi profesi Public Relations (PR) dari Badan Nasional Sertifikasi Profesi (BNSP) sudah disadari oleh banyak kalangan masyarakat. Hal ini terlihat dari para peserta dengan berlatar belakang pekerjaan yang beragam. Namun mereka tidak hanya mengetahui dan mencari sertifikasi profesinya saja, beberapa diantaranya mengejar untuk mendapatkan gelar profesinya yaitu C.PR (Certified Public Relations) untuk mendukung karir. Untuk memperoleh gelar ini, peserta harus mengikuti uji kompetensi PR dari Lembaga Sertifikasi Profesi Public Relations Indonesia (LSP PRI) untuk tiga skema dalam dua tahapan uji kompetensi. LSP PRI adalah lembaga yang memperoleh ijin dari BNSP, untuk menyelenggarakan Uji Sertifikasi Profesi PR. Pada Bulan Desember 2021, Pimpinan STRATECOMMS, Dr Muhammad Adi Pribadi, C.PR menyerahkan sertifikat profesi PR untuk skema C.PR kepada Bapak Siko D.S.W, S.ST., C.PR. Penyerahan sertifikat ini adalah untuk yang kedua kalinya oleh Pimpinan STRATECOMMS karena beliau harus mengikuti uji kompetensi PR dari LSP PRI - BNSP, sebanyak dua kali untuk tiga skema dalam memperoleh gelar C.PR. Bapak Siko yang bekerja di Kementerian Keuangan Republik Indonesia sangat peduli dengan gelar profesi ini untuk menunjang karirnya. Hal ini menunjukkan bahwa lembaganya sangat memperhatikan pegawainya untuk memperoleh sertifikat profesi dari BNSP. STRATECOMMS bekerjasama dengan LSP PRI akan mengadakan uji kompetensi PR berikutnya pada sabtu 22 Januari 2022. Sedangkan, workshop persiapan uji kompetensi PR akan dilaksanakan pada sabtu 15 Januari 2022. Silahkan menghubungi STRATECOMMS di nomer telpon 081390601398 untuk informasi lebih lanjut. Hal ini menjadi kebahagiaan tersendiri bagi STRATECOMMS yang selalu mendampingi para asesinya untuk maju bersama dalam meraih harapan terbaiknya. Salam sehat dan sukses untuk kita semua dalam mengarungi waktu di tahun 2022.", "yes", "{dt_string}")')
  # connection.commit()

  return render(request, 'homepage.html')

def jadwalSertifikasi(request):
  return render(request,'jadwalSertifikasi.html')

def artikel(request):
  return render(request, 'artikel.html')

isiArtikel

def portofolio(request):
  return render(request, 'portofolio.html')

def isiPortofolio(request):
  return render(request, 'isiPortofolio.html')

def pendaftaran(request):
  return render(request, 'pendaftaran.html')

def pendaftaranBerhasil(request):
  return render(request, 'pendaftaranBerhasil.html')

adminLogin

def adminHome(request):
  return render(request, 'admin/adminHome.html')

def adminArtikel(request):
  return render(request, 'admin/adminArtikel.html')

def addArtikel(request):
  return render(request, 'admin/addArtikel.html')

def editArtikel(request):
  return render(request, 'admin/editArtikel.html')

def editJadwal(request):
  return render(request, 'admin/editJadwal.html')

def adminJadwal(request):
  return render(request, 'admin/adminJadwal.html')

def adminPortofolio(request):
  return render(request, 'admin/adminPortofolio.html')

def addPortofolio(request):
  return render(request, 'admin/addPortofolio.html')

def editPortofolio(request):
  return render(request, 'admin/editPortofolio.html')
