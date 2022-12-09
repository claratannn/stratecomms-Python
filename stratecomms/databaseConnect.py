import mysql.connector
from mysql.connector import Error
import csv
from random import randint

def connect():
  try:
      connection = mysql.connector.connect(
          host= "127.0.0.1",
          port= '3306',
          user= "root",
<<<<<<< HEAD
          password= "admin123",
=======
          password= "PkmOba_2022",
>>>>>>> 52bf5e3a49e1dd8a3652ea846432ddbd24817250
          database= "stratecomms",
          auth_plugin='mysql_native_password')
      if connection.is_connected():
        return connection

  except Error as e:
      print("Error while connecting to MySQL", e)

def selectAll(tableName, cursor):
  cursor.execute(f"SELECT * FROM {tableName}")
  result = cursor.fetchall()
  return result

def insertToTable(tableName, value, connection, cursor):
  # value = 'null, ' + value
  print(value)
  cursor.execute(f"INSERT INTO {tableName} VALUES ({value})")
  connection.commit()