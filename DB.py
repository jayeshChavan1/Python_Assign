import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="test")

mycursor = mydb.cursor()

mycursor.execute("select * from customers")

for i in mycursor:
    print(i)
