from django.shortcuts import render
from .pages.pendaftaran import *
from .pages.artikel import *
from .pages.admin.login import *
from .pages.admin.isiArtikel import *
from .pages.admin.adminArtikel import *
from .pages.admin.addArtikel import *
from datetime import datetime

connection = connect()
cursor = connection.cursor(dictionary= True)

def homepage(request):
  # now = datetime.now()
  # dt_string = now.strftime("%d %B %Y, %H:%M:%S")
  # print("date and time =", dt_string)	  
  # print(dt_string)

  # cursor.execute(f'insert into artikel values(null, "artikel.png", "REFLEKSI STRATECOMMS TAHUN 2021: KEMENTERIAN PEDULI SERTIFIKASI PROFESI DARI BNSP", "Perkembangan sertifikasi profesi Public Relations (PR) dari Badan Nasional Sertifikasi Profesi (BNSP) sudah disadari oleh banyak kalangan masyarakat. Hal ini terlihat dari para peserta dengan berlatar belakang pekerjaan yang beragam. Namun mereka tidak hanya mengetahui dan mencari sertifikasi profesinya saja, beberapa diantaranya mengejar untuk mendapatkan gelar profesinya yaitu C.PR (Certified Public Relations) untuk mendukung karir. Untuk memperoleh gelar ini, peserta harus mengikuti uji kompetensi PR dari Lembaga Sertifikasi Profesi Public Relations Indonesia (LSP PRI) untuk tiga skema dalam dua tahapan uji kompetensi. LSP PRI adalah lembaga yang memperoleh ijin dari BNSP, untuk menyelenggarakan Uji Sertifikasi Profesi PR. Pada Bulan Desember 2021, Pimpinan STRATECOMMS, Dr Muhammad Adi Pribadi, C.PR menyerahkan sertifikat profesi PR untuk skema C.PR kepada Bapak Siko D.S.W, S.ST., C.PR. Penyerahan sertifikat ini adalah untuk yang kedua kalinya oleh Pimpinan STRATECOMMS karena beliau harus mengikuti uji kompetensi PR dari LSP PRI - BNSP, sebanyak dua kali untuk tiga skema dalam memperoleh gelar C.PR. Bapak Siko yang bekerja di Kementerian Keuangan Republik Indonesia sangat peduli dengan gelar profesi ini untuk menunjang karirnya. Hal ini menunjukkan bahwa lembaganya sangat memperhatikan pegawainya untuk memperoleh sertifikat profesi dari BNSP. STRATECOMMS bekerjasama dengan LSP PRI akan mengadakan uji kompetensi PR berikutnya pada sabtu 22 Januari 2022. Sedangkan, workshop persiapan uji kompetensi PR akan dilaksanakan pada sabtu 15 Januari 2022. Silahkan menghubungi STRATECOMMS di nomer telpon 081390601398 untuk informasi lebih lanjut. Hal ini menjadi kebahagiaan tersendiri bagi STRATECOMMS yang selalu mendampingi para asesinya untuk maju bersama dalam meraih harapan terbaiknya. Salam sehat dan sukses untuk kita semua dalam mengarungi waktu di tahun 2022.", "yes", "{dt_string}")')
  # connection.commit()

  return render(request, 'homepage.html')

def jadwalSertifikasi(request):
  cursor.execute('select * from jadwal')
  jadwalSertifikasi = cursor.fetchone()
  syarat = jadwalSertifikasi['deskripsi3'].split('-')

  context = {
    'jadwalSertifikasi' : jadwalSertifikasi,
    'syarat' : syarat,
  }

  if request.method == "POST":
    # try:
    #   fotoPoster = request.FILES['fotoPoster']
    #   fs = FileSystemStorage(location='static/images/jadwal')
    #   fs.save(fotoPoster.name, fotoPoster)
    # except:
    #   messages.info(request, 'MOHON UNTUK MENGISI KOLOM FOTO')
    #   return render(request, 'admin/editJadwal.html')
      
    # updateTitle = request.POST.get('updateTitle')
    # updateJudul1 = request.POST.get('updateJudul1')
    # updateDeskripsi1 = request.POST.get('updateDeskripsi1')
    # updateJudul2 = request.POST.get('updateJudul2')
    # updateDeskripsi2 = request.POST.get('updateDeskripsi2')
    # updateJudul3 = request.POST.get('updateJudul3')
    # updateDeskripsi3 = request.POST.get('updateDeskripsi3')
    # button = request.POST.get('button')

    # button = button.split('-')
    # if button[0] == 'UpdateAdminPorto':
    #   cursor.execute(f'update portofolio set fotoPoster = "{fotoPoster}",updateTitle = "{updateTitle}", updateJudul1 = "{updateJudul1}", updateJudul2 = "{updateJudul2}", updateJudul3 = "{updateJudul3}", updateDeskripsi1 = "{updateDeskripsi1}", updateDeskripsi2 = "{updateDeskripsi2}", updateDeskripsi3 = "{updateDeskripsi3}" where PortofolioID = "{PortofolioId}"')

    cursor.execute('select * from jadwal')
    jadwalSertifikasi = cursor.fetchone()

    context = {
      'jadwalSertifikasi' : jadwalSertifikasi,
      'syarat' : syarat,
    }

  return render(request,'jadwalSertifikasi.html', context)

artikel

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

adminArtikel

addArtikel

def editArtikel(request):
  return render(request, 'admin/editArtikel.html')

def editJadwal(request):
  cursor.execute('select * from jadwal where JadwalId=1')
  jadwalSertifikasi = cursor.fetchone()
  syarat = jadwalSertifikasi['deskripsi3'].split('-')

  context = {
    'jadwalSertifikasi' : jadwalSertifikasi,
    'syarat' : syarat,
  }

  if request.method == "POST":
    try:
      fotoPoster = request.FILES['fotoPoster']
      fs = FileSystemStorage(location='static/images/jadwal')
      fs.save(fotoPoster.name, fotoPoster)
    except:
      messages.info(request, 'MOHON UNTUK MENGISI KOLOM FOTO')
      return render(request, 'admin/editJadwal.html')
      
    updateTitle = request.POST.get('updateTitle')
    if updateTitle == '':
      messages.info(request, 'MOHON UNTUK MENGISI KOLOM JUDUL UTAMA')
      return render(request, 'admin/editJadwal.html')

    updateJudul1 = request.POST.get('updateJudul1')
    if updateTitle == '':
      messages.info(request, 'MOHON UNTUK MENGISI KOLOM JUDUL 1')
      return render(request, 'admin/editJadwal.html')

    updateDeskripsi1 = request.POST.get('updateDeskripsi1')
    if updateDeskripsi1 == '':
      messages.info(request, 'MOHON UNTUK MENGISI KOLOM DESKRIPSI 1')
      return render(request, 'admin/editJadwal.html')
    

    updateJudul2 = request.POST.get('updateJudul2')
    if updateJudul2 == '':
      updateJudul2 = 'none'
    
    updateDeskripsi2 = request.POST.get('updateDeskripsi2')
    if updateDeskripsi2 == '':
      updateDeskripsi2 = 'none'

    updateJudul3 = request.POST.get('updateJudul3')
    if updateJudul3 == '':
      updateJudul3 = 'none'

    updateDeskripsi3 = request.POST.get('updateDeskripsi3')
    if updateDeskripsi3 == '':
      updateDeskripsi3 = 'none'

    cursor.execute(f'update jadwal set gambar = "{fotoPoster}",judul = "{updateTitle}", judul1 = "{updateJudul1}", judul2 = "{updateJudul2}", judul3 = "{updateJudul3}", deskripsi1 = "{updateDeskripsi1}", deskripsi2 = "{updateDeskripsi2}", deskripsi3 = "{updateDeskripsi3}" where JadwalId = 1')
    connection.commit()

    cursor.execute('select * from jadwal')
    jadwalSertifikasi = cursor.fetchone()
    syarat = jadwalSertifikasi['deskripsi3'].split('-')

    context = {
      'jadwalSertifikasi' : jadwalSertifikasi,
      'syarat' : syarat,
    }

  return render(request, 'admin/editJadwal.html', context)


def adminJadwal(request):
  cursor.execute('select * from jadwal')
  jadwalSertifikasi = cursor.fetchone()
  syarat = jadwalSertifikasi['deskripsi3'].split('-')

  context = {
    'jadwalSertifikasi' : jadwalSertifikasi,
    'syarat' : syarat,
  }

  if request.method == "POST":
    # try:
    #   fotoPoster = request.FILES['fotoPoster']
    #   fs = FileSystemStorage(location='static/images/jadwal')
    #   fs.save(fotoPoster.name, fotoPoster)
    # except:
    #   messages.info(request, 'MOHON UNTUK MENGISI KOLOM FOTO')
    #   return render(request, 'admin/editJadwal.html')
      
    # updateTitle = request.POST.get('updateTitle')
    # updateJudul1 = request.POST.get('updateJudul1')
    # updateDeskripsi1 = request.POST.get('updateDeskripsi1')
    # updateJudul2 = request.POST.get('updateJudul2')
    # updateDeskripsi2 = request.POST.get('updateDeskripsi2')
    # updateJudul3 = request.POST.get('updateJudul3')
    # updateDeskripsi3 = request.POST.get('updateDeskripsi3')
    # button = request.POST.get('button')

    # button = button.split('-')
    # if button[0] == 'UpdateAdminPorto':
    #   cursor.execute(f'update portofolio set fotoPoster = "{fotoPoster}",updateTitle = "{updateTitle}", updateJudul1 = "{updateJudul1}", updateJudul2 = "{updateJudul2}", updateJudul3 = "{updateJudul3}", updateDeskripsi1 = "{updateDeskripsi1}", updateDeskripsi2 = "{updateDeskripsi2}", updateDeskripsi3 = "{updateDeskripsi3}" where PortofolioID = "{PortofolioId}"')

    cursor.execute('select * from jadwal')
    jadwalSertifikasi = cursor.fetchone()
    syarat = jadwalSertifikasi['deskripsi3'].split('-')


    context = {
      'jadwalSertifikasi' : jadwalSertifikasi,
      'syarat' : syarat,
    }

  return render(request, 'admin/adminJadwal.html', context)

def adminPortofolio(request):
  return render(request, 'admin/adminPortofolio.html')

def addPortofolio(request):
  return render(request, 'admin/addPortofolio.html')

def editPortofolio(request):
  return render(request, 'admin/editPortofolio.html')

def addJadwal(request):
  return render(request, 'admin/addJadwal.html')