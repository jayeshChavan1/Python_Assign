from bs4 import BeautifulSoup
import mysql.connector as mydbs
import requests

#URL = "https://www.instagram.com/python_assign/?hl=en"
URL = "https://www.instagram.com/jayychavhan/?hl=en"
req = requests.get(URL)

soup = BeautifulSoup(req.text, 'html.parser')
# print(soup.prettify())


title = soup.find("meta",  property="og:description")
strg = str(title['content'])
info = (strg.split())

sql_int = []
insta=[]

for i in info:
    i = i.strip(',@()')
    insta.append(i)

sql_int.append(insta[-1])
sql_int.append(insta[-2])
sql_int.append(insta[0])
sql_int.append(insta[2])
sql_int.append(insta[4])

print(sql_int)

myconn = mydbs.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="instagram"
)

mycursor = myconn.cursor()

sql_form = """INSERT INTO insta (username, name, followers, following, posts) VALUES (%s, %s, %s, %s, %s)"""

mycursor.execute(sql_form,sql_int)
myconn.commit()



