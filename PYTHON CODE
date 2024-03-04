import mysql.connector


db_name = "newproject"
db_user = "root"
db_password = "student"
db_host = "localhost"

# Connection
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
def insert_book(name, author, classification, branch, shelf):
  try:
    sql = "INSERT INTO books (name, author, classification, branch, shelf) VALUES ( %s, %s, %s, %s, %s)"
    cursor.execute(sql,(name, author, classification, branch, shelf))
    connection.commit()
    print("Book added successfully!")

  except mysql.connector.Error as err:
    print("Error inserting book:", err)
    






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
        results1 = cursor.fetchall()

        if results1:
            print("Search results:")
            for row in results1:
                print(f"bookid: {row[0]} | Name: {row[1]} | Author: {row[2]} | Classification: {row[3]} | Branch: {row[4]} | Shelf: {row[5]}")
        else:
            print("No books found with that name.")

    except mysql.connector.Error as err:
        print("Error searching for book:", err)
  
    except:
        print("err")
        
        
        
        
        
        
print("WELCOME TO THE LIBRARY MANAGEMENT SYSTEM")


        

addbook= input("enter y/n if you want to add new book : ")

if addbook== "y":
    name= input("enter name : ")
    author=input("enter name of auhor : ")
    classification=input("enter the classification : ")
    branch=input("enter the branch : ")
    shelf=input("enter the shelf : ")
    insert_book(name,author,classification,branch,shelf)
    
else :
    print("no new book added")



        
searchtype= input("enter if you want to find book by name/author : ")
 
if searchtype == "name":
    searchname = input("enter name of the book : ")
    print(searchname)
    search_by_name(searchname)


elif searchtype=="author":
    searchname1=input("enter name of the author : ")
    print(searchname1)
    search_by_author(searchname1)
    
else:
    print("error type name or author name to search")
    
    



# Close the connection
connection.close()
 
