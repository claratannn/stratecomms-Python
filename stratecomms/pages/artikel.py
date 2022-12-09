from django.shortcuts import render, redirect
from datetime import datetime
from ..databaseConnect import *

connection = connect()
cursor = connection.cursor(dictionary=True)

def artikel(request):
  cursor.execute('select * from artikel')
  artikel = cursor.fetchall()

  cursor.execute('select * from artikel where pin = "yes"')
  topArtikel = cursor.fetchall()

  context = {
    'artikel' : artikel,
    'topArtikel' : topArtikel,
  }

  if request.method == 'POST':
    button = request.POST.get('button')
    print(button)
    if button != '' or button != None:
      return redirect('isiArtikel', pk=button)  

  return render(request, 'artikel.html', context)