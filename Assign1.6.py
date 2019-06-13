import mysql.connector as mydbs
import twitter
from fpdf import FPDF

api = twitter.Api(consumer_key='uUxFGMySjOQs2LC4rwtBGOJ31', consumer_secret='Qwf6H8P2gFuaXPEaS9IUD2jjakCjZh00YGYdRnWtXqX8ESOFrr',
                  access_token_key='1136618829591719938-3KAm74SP7gjaaYZrlNFjYhlZ3HhMHu', access_token_secret='qHhhHkLkyYAk1RaIQzHHDPvjyZsLCdBshypEg3BQxZu69')

user = "@Python88925757"

user_info_list = []
usr = api.GetUser(screen_name=user)
user_info = usr.AsDict()

user_info_list.append(user_info["name"])
user_info_list.append(user_info['screen_name'])
user_info_list.append(user_info['followers_count'])
user_info_list.append(user_info['friends_count'])

tweets = api.GetUserTimeline(screen_name=user)
for s in tweets:
    user_info_list.append(s.text)

myconn = mydbs.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="twitter"
)

mycursor = myconn.cursor()

sql_form = """INSERT INTO twitter (name, username, followers, following, tweets) VALUES (%s, %s, %s, %s, %s)"""

mycursor.execute(sql_form,user_info_list)

#myconn.commit()

sql_select_Query = "select * from twitter"
mycursor.execute(sql_select_Query)

records = mycursor.fetchone()

class PDF(FPDF):

    def header(self):

        self.set_font('Arial','B',22)
        self.cell(0, 15, 'Twitter Database', ln=1, align="C")
        self.ln(5)

    def simple_pdf(spacing=1):

        pdf.set_font("Arial", size=10)
        col_width = pdf.w / 5.5
        row_height = pdf.font_size + 5
        head = ["Name","Username","Followers","Following","Tweets"]
        for item in head:
            pdf.cell(col_width, row_height, txt=item, border=1, align="C" )
        pdf.ln(row_height)

        for item in records:
            pdf.cell(col_width, row_height, txt=item, border=1 ,align="C")
        pdf.ln(row_height)

        pdf.output('twitter_mysql_pdf.pdf')

pdf = PDF()
pdf.add_page()
pdf.simple_pdf()
