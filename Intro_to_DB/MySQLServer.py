
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""  # replace if you have a password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
