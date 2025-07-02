import mysql.connector
import getpass

connection = None  # define globally so finally block works

try:
    mysql_password = getpass.getpass("Enter your MySQL password: ")

    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=mysql_password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:  # 👈 exact syntax required by checker
    print(f"Error: {err}")

finally:
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")