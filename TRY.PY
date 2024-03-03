import mysql.connector

# Database connection details
db_name = "newproject"
db_user = "root"
db_password = "student"
db_host = "localhost"

# Connect to the database
try:
  connection = mysql.connector.connect(
      host=db_host,
      user=db_user,
      password=db_password,
      database=db_name
  )
  cursor = connection.cursor()
  print("connection established")


except mysql.connector.Error as err:
  print("Error connecting to database:", err)
  exit()

# Function to insert a new book
def insert_book(bookid,name, author, classification, branch, shelf):
  try:
    sql = "INSERT INTO books (bookid,name, author, classification, branch, shelf) VALUES (%d, %s, %s, %s, %s, %d)"
    cursor.execute(sql,(bookid ,name, author, classification, branch, shelf))
    connection.commit()
    print("Book added successfully!")

  except mysql.connector.Error as err:
    print("Error inserting book:", err)
    
insert_book(7,"pranshu","pranshu","science","cs",22)

def insert_book( name, author, classification, branch, shelf):
    try:
        sql = "INSERT INTO books (name, author, classification, branch, shelf) VALUES ( %s, %s, %s, %s, %d)"
        cursor.execute(sql, ( name, author, classification, branch, shelf))
        connection.commit()
        print("Book added successfully!")

    except mysql.connector.Error as err:
        print("Error inserting book:", err)

# Calling the function with all arguments
insert_book("pranshu", "pranshu", "science", "cs", 22)

'''
# Function to search books by name
def search_by_name(name):
  try:
    sql = "SELECT * FROM books WHERE name LIKE %s"
    cursor.execute(sql, ("%{}%".format(name),))
    results = cursor.fetchall()

    if results:
      print("Search results:")
      for row in results:
        print(f"bookid: {row[0]} | Name: {row[1]} | Author: {row[2]} | Classification: {row[3]} | Branch: {row[4]} | Shelf: {row[5]}")
    else:
      print("No books found with that name.")

  except mysql.connector.Error as err:
    print("Error searching for book:", err)

# Function to search books by author
def search_by_author(author):
    try:
        sql = "SELECT * FROM books WHERE author LIKE %s"  # Modified for author search
        cursor.execute(sql, ("%{}%".format(author),))
  # Implement similar logic as search_by_name, replacing 'name' with 'author' in the query and displaying results

    except:
        print("err")

'''
# Close the connection
connection.close()
 
