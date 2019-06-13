import csv
import mysql.connector as mydbs

myconn = mydbs.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="test"
)

mycursor = myconn.cursor()

sqlform = "INSERT INTO demo (ID,Name,City) VALUES (%s, %s, %s)"

with open('demo.csv', 'r') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        print(row)
        mycursor.execute(sqlform,row)
        myconn.commit()

myconn.close()

