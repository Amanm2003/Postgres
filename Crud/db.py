# for database
import psycopg2

def get_connection():
  connection = psycopg2.connect(
    dbname='training',
    user='saideepa',
    password='saideepa',
    host='192.168.180.91',
    port='5432'
  )
  return connection
