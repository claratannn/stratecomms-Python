from django.shortcuts import render, redirect
from ...databaseConnect import *
from django.contrib import messages

connection = connect()
cursor = connection.cursor(dictionary=True)

def adminLogin(request):
  # print('here')

  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')

    print(email)
    try:
      cursor.execute(f'select Password from admin where Email = "{email}"')
      adminpass = cursor.fetchone()
    except:
       messages.info(request, 'ACCOUNT NOT FOUND')
       return render(request, 'admin/adminLogin.html')
    
    if adminpass['Password'] == password:
      return redirect('/adminHome')
    else:
      messages.info(request, 'WRONG PASSWORD')

  return render(request, 'admin/adminLogin.html')