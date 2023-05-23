import mysql.connector

connection= mysql.connector.connect(host="localhost",username="root",password="mysql123")
cursor=connection.cursor()
cursor.execute("show databases")
data = cursor.fetchall()
print(data)
connection.close()