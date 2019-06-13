import psycopg2
from fpdf import FPDF
import csv

connection = psycopg2.connect(user = "postgres",
                              database = "python"
                              )

mycursor = connection.cursor()

psql_select_Query = "select * from demo1"

mycursor.execute(psql_select_Query)

records = mycursor.fetchall()

with open('psql_test.csv', 'w') as f:
     writer = csv.writer(f, delimiter=',')
     writer.writerows(records)

print("Successfully Write data into File")
