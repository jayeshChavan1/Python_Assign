from bs4 import BeautifulSoup
import psycopg2
import requests
import re

URL = "https://twitter.com/Python88925757"

req = requests.get(URL)

psql_data = []
insta=[]

soup = BeautifulSoup(req.text, 'html.parser')
# print(soup.prettify())

title = soup.find(attrs={"name":"description"})

links = soup.findAll('a', {'class': 'ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor'})

for i in links:
    follwng = i.get('title')
    psql_data.append(follwng)

strg = str(title['content'])
#print(strg)

info = (strg.split())

for i in info:
    i = i.strip(',@():')
    insta.append(i)

psql_data.append(insta[4])
psql_data.append(insta[5])

result = re.findall(r'"([^"]*)"', strg)

psql_data.extend(result)

print(psql_data)


connection = psycopg2.connect(user = "postgres",
                              database = "python"
                              )

mycursor = connection.cursor()


psql_form = """INSERT INTO twitter (following, likes, name, username, tweets) VALUES (%s, %s, %s, %s, %s)"""

mycursor.execute(psql_form,psql_data)
connection.commit()
