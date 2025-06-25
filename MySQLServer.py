import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="oluwaseyiae",
    database="alx_book_store"
)

mycursor = mydb.cursor()

sql = "CREATE DATABASE IF NOT EXISTS alx_book_store"
mycursor.execute(sql)
print("Database 'alx_book_store' created successfully!")



mycursor.close()
mydb.close()

