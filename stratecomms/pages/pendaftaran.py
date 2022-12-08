from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def pendaftaran(request):
  context = {
    }

  if request.method == 'POST':
    foto = request.FILES['foto'] 
    print(foto)
    fs = FileSystemStorage(location='static/images')
    filename = fs.save(foto.name, foto)
    uploaded_file_url = fs.url(filename)

    context = {
      'foto' : foto,
      'uploaded_file_url': uploaded_file_url,
    }

  return render(request, 'pendaftaran.html', context)
