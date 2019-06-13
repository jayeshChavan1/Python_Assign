import psycopg2
import csv

connection = psycopg2.connect(user = "postgres",
                              database = "python"
                              )

mycursor = connection.cursor()

psqlform = "INSERT INTO demo1 (ID,Name,City) VALUES (%s, %s, %s)"

with open('demo.csv', 'r') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        print(row)
        mycursor.execute(psqlform,row)
        #connection.commit()

connection.close()

