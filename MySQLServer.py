import mysql.connector
from mysql.connector import Error
import getpass  # For safe password input

connection = None  # Define at top so it's accessible in finally

try:
    # Securely get MySQL password from user
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

except Error as err:
    print(f"Error: {err}")

finally:
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
