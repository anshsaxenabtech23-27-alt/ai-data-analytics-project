import mysql.connector

# MySQL connection setup
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="anshsxna22@AN",  
    database="ecommerce"
)

print("Database connected successfully!")

