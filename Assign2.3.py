from bs4 import BeautifulSoup
import psycopg2
import requests


#URL = "https://www.instagram.com/python_assign/?hl=en"
URL = "https://www.instagram.com/jayychavhan/?hl=en"
req = requests.get(URL)

soup = BeautifulSoup(req.text, 'html.parser')
# print(soup.prettify())


title = soup.find("meta",  property="og:description")
strg = str(title['content'])
info = (strg.split())

psql_int = []
insta=[]

for i in info:
    i = i.strip(',@()')
    insta.append(i)

psql_int.append(insta[-1])
psql_int.append(insta[-2])
psql_int.append(insta[0])
psql_int.append(insta[2])
psql_int.append(insta[4])

print(psql_int)

connection = psycopg2.connect(user = "postgres",
                              database = "python"
                              )

mycursor = connection.cursor()

psql_form = """INSERT INTO insta (username, name, followers, following, post) VALUES (%s, %s, %s, %s, %s)"""

mycursor.execute(psql_form,psql_int)
connection.commit()

