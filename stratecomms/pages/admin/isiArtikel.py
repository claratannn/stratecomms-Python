from django.shortcuts import render
from ...databaseConnect import *
from django.contrib import messages

connection = connect()
cursor = connection.cursor(dictionary=True)

def isiArtikel(request):
  cursor.execute('select * from artikel')
  artikel = cursor.fetchone()

  context = {
    'artikel' : artikel,
  }

  return render(request, 'isiArtikel.html', context)