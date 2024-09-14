import mysql.connector

database=mysql.connector.connect(
  host='localhost',
  user='root',
  passwd='rammech@2294'
)

cursorObject=database.cursor()

cursorObject.execute("CREATE DATABASE dcrmwebapp")

