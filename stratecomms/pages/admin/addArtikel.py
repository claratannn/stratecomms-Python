from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from ...databaseConnect import *
from django.contrib import messages

connection = connect()
cursor = connection.cursor(dictionary=True)

def addArtikel(request):

  if request.method == 'POST':
    now = datetime.now()
    dt_string = now.strftime("%d %B %Y, %H:%M:%S")

    try:
      foto = request.FILES['fotoartikel']
      fs = FileSystemStorage(location='static/images/artikel')
      filename = fs.save(foto.name, foto)
    except:
      messages.info(request, 'MOHON UNTUK MENGISI KOLOM FOTO')
      return render(request, 'admin/addArtikel.html')
    
    judul = request.POST.get('judul')
    isi = request.POST.get('isi')

    try:
      cursor.execute(f'insert into artikel values(null, "{foto}", "{judul}", "{isi}", "no", "{dt_string}")')
      connection.commit()
    except:
      messages.info(request, 'DATA GAGAL DITAMBAHKAN')
      return render(request, 'admin/addArtikel.html')

  return render(request, 'admin/addArtikel.html')