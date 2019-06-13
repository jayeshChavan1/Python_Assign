import mysql.connector as mydbs
import csv

myconn = mydbs.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="test1"
)

mycursor = myconn.cursor()

sql_select_Query = "select * from demo1"
mycursor.execute(sql_select_Query)

records = mycursor.fetchall()

with open('test.csv', 'w') as f:
     writer = csv.writer(f, delimiter=',')
     writer.writerows(records)

print("Successfully Write data into File")
