import mysql.connector

try:
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

except mysql.connector.Error as e:
    print(f"Error: {e}")
finally:
    if mycursor:
        print("Cursor is closed.")
    mycursor.close()

    if mydb:
        print("MySQL connection is closed.")
    mydb.close()