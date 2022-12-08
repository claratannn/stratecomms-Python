from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def pendaftaran(request):
  context = {
    }

  if request.method == 'POST':
    foto = request.FILES['foto'] 
    fs = FileSystemStorage(location='static/images/pasFoto')
    filename = fs.save(foto.name, foto)
    foto = fs.url(filename)

    cv = request.FILES['cv'] 
    fs = FileSystemStorage(location='static/images/cv')
    filename = fs.save(cv.name, cv)
    cv = fs.url(filename)

    ijazah = request.FILES['ijazah'] 
    fs = FileSystemStorage(location='static/images/ijazahTerakhir')
    filename = fs.save(foto.name, foto)
    ijazah = fs.url(filename)

    ktp = request.FILES['ktp'] 
    fs = FileSystemStorage(location='static/images/ktp')
    filename = fs.save(foto.name, foto)
    ktp = fs.url(filename)

    context = {
      # 'foto' : foto,
      # 'uploaded_file_url': uploaded_file_url,
    }

  return render(request, 'pendaftaran.html', context)
