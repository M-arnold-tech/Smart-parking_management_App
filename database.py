import mysql.connector
from mysql.connector import Error

def get_connection():

  try:
    connection = mysql.connector.connect(
      host="localhost",           # Change if running on a remote server
      user="root",                # Your MYSQL username
      password="yourpassword",    # Your MYSQL password
      database="smart_spaces"
    )

    if connection.is_connected():
      return connection
    
  except Error as e:
    print(f"[ERROR] Database connection failed: {e}")
    return None
  