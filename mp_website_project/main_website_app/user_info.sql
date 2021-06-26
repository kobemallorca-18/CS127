import mysql.connector

mydb = mysql.connector.connect(
  email="email",
  password="yourusername",
  firstname="yourpassword",
  lastname="mydatabase",
  phonenumber="myphonenumber"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE user_info (name VARCHAR(255), address VARCHAR(255))")