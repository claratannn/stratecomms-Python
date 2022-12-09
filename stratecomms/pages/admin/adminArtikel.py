from django.shortcuts import render
from datetime import datetime
from ...databaseConnect import *

connection = connect()
cursor = connection.cursor(dictionary=True)

def adminArtikel(request):
  cursor.execute('select * from artikel')
  artikel = cursor.fetchall()

  context = {
    'artikel' : artikel,
  }

  if request.method == 'POST':
    button = request.POST.get('button')
    button = button.split('-')

    print(button[0])

    if button[0] == 'delete':
      cursor.execute(f'delete from artikel where ArtikelId = {button[1]}')
      connection.commit()
    if button[0] == 'pin':
      cursor.execute(f'update artikel set pin = "yes" where ArtikelId = {button[1]}')
      connection.commit()
    if button[0] == 'unpin':
      cursor.execute(f'update artikel set pin = "no" where ArtikelId = {button[1]}')
      connection.commit()
    
    cursor.execute('select * from artikel')
    artikel = cursor.fetchall()

    context = {
      'artikel' : artikel,
    }

  return render(request, 'admin/adminArtikel.html', context)