import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="VehryHordPassword",
  database='accounts'
)

mycursor = mydb.cursor()

# Unless already created -> mycursor.execute("CREATE DATABASE accounts")
# Unless already created -> mycursor.execute("CREATE TABLE creds (name VARCHAR(255), passwd VARCHAR(255), plan VARCHAR(255))")

insert_sql = "INSERT INTO creds (name, passwd, plan) VALUES (%s, %s, %s)"
acc_val = ("test", "t3st", 'basic')