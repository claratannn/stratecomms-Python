from django.shortcuts import render
from datetime import datetime
from ..databaseConnect import *

connection = connect()
cursor = connection.cursor(dictionary=True)

def artikel(request):
  cursor.execute('select * from artikel')
  artikel = cursor.fetchall()

  context = {
    'artikel' : artikel,
  }

  return render(request, 'artikel.html', context)