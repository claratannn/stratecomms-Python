from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from ..databaseConnect import *
from django.contrib import messages

connection = connect()
cursor = connection.cursor(dictionary=True)

def pendaftaran(request):
  context = {
  }

  cursor.execute('select * from peserta')
  data = cursor.fetchall()
  print(data)

  if request.method == 'POST':
      
    name = request.POST.get('nama')
    if name == '':
      messages.info(request, 'MOHON UNTUK MENGISI KOLOM NAMA')
      return render(request, 'pendaftaran.html', context)
    
    wa = request.POST.get('wa')
    if wa == '':
      messages.info(request, 'MOHON UNTUK MENGISI KOLOM NOMOR WHATSAPP')
      context = {
        'name' : name,
      }
      return render(request, 'pendaftaran.html', context)
    
    try:
      foto = request.FILES['foto']
      fs = FileSystemStorage(location='static/images/pasFoto')
      filename = fs.save(foto.name, foto)
      foto = fs.url(filename)
    except:
      messages.info(request, 'MOHON UNTUK MENGISI KOLOM FOTO')
      context = {
        'name' : name,
        'wa' : wa,
      }
      return render(request, 'pendaftaran.html', context)
    
    try:
      cv = request.FILES['cv'] 
      fs = FileSystemStorage(location='static/images/cv')
      filename = fs.save(cv.name, cv)
      cv = fs.url(filename)
    except:
      messages.info(request, 'MOHON UNTUK MENGISI KOLOM CV')
      context = {
        'name' : name,
        'wa' : wa,
      }
      return render(request, 'pendaftaran.html', context)
    
    try:
      ijazah = request.FILES['ijazah'] 
      fs = FileSystemStorage(location='static/images/ijazahTerakhir')
      filename = fs.save(ijazah.name, ijazah)
      ijazah = fs.url(filename)
    except:
      messages.info(request, 'MOHON UNTUK MENGISI KOLOM IJAZAH TERAKHIR')
      context = {
        'name' : name,
        'wa' : wa,
      }
      return render(request, 'pendaftaran.html', context)
    
    try:
      ktp = request.FILES['ktp'] 
      fs = FileSystemStorage(location='static/images/ktp')
      filename = fs.save(ktp.name, ktp)
      ktp = fs.url(filename)
    except:
      messages.info(request, 'MOHON UNTUK MENGISI KOLOM KTP')
      context = {
        'name' : name,
        'wa' : wa,
      }
      return render(request, 'pendaftaran.html', context)
    
    try:
      cursor.execute(f'insert into peserta values(null, "{name}", "{wa}", "{foto}", "{cv}", "{ijazah}", "{ktp}")')
      connection.commit()
    except:
      messages.info(request, 'DATA GAGAL UNTUK DI TAMBAHKAN')
      return render(request, 'pendaftaran.html', context)

    context = {
    }

  return render(request, 'pendaftaran.html', context)
