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
          password= "PkmOba_2022",
          database= "stratecomms",
          auth_plugin='mysql_native_password'
          )
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