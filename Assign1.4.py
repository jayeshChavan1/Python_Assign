import mysql.connector as mydbs

myconn = mydbs.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="test1"
)

mycursor = myconn.cursor()

# sql_create_category = "create table category(id int not null auto_increment primary key, name varchar(255) not null);"
# mycursor.execute(sql_create_category)
#
# sql_create_books = "create table books(id int not null auto_increment primary key, name varchar(255) not null);"
# mycursor.execute(sql_create_books)
#
# sql_create_book_cat = "CREATE TABLE book_cat( category_id int not null, \
#                     FOREIGN KEY fk_category(category_id) REFERENCES category(id), \
#                     books_id int not null, \
#                     FOREIGN KEY fk_books(books_id) REFERENCES books(id)\
#                     );"
# mycursor.execute(sql_create_book_cat)


# sql_cato = "INSERT INTO category (name) VALUES (%s)"
# val_cato = [('Engineering'),('Commerce')]
#
# mycursor.executemany(sql_cato, val_cato)

# sql_book = "INSERT INTO books (name) VALUES (%s)"
# val_book = [('Mechanic'),('Math'),('Electrical'),('Accounts')]
#Mechnics
# mycursor.executemany(sql_book, val_book)

# sql_book_cat = "INSERT INTO book_cat (category_id,books_id) VALUES (%s)"
# val_book_cat = [(1,1),(1,2),(1,3),(2,2),(2,4)]
#
# mycursor.executemany(sql_book_cat, val_book_cat)

sql_query = "select category.id, category.name \
             from category inner join book_cat \
             on book_cat.category_id=category.id \
             where book_cat.books_id=(select id from books where name='Math');"

mycursor.execute(sql_query)

for i in mycursor:
  print(i)

