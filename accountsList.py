import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="VehryHordPassword",
  database='accounts'
)

mycursor = mydb.cursor()

# Unless already created -> 
# mycursor.execute("CREATE DATABASE accounts")

# Delete table -> 
# mycursor.execute("DROP TABLE creds")

# Unless already created -> 
mycursor.execute("CREATE TABLE creds (name VARCHAR(255), passwd VARCHAR(255), plan VARCHAR(255))")



print(mycursor.rowcount, "record inserted.")


acc_val = ("test", "pass", 'basic')

mycursor.execute("INSERT INTO creds (name, passwd, plan) VALUES (%s, %s, %s)", acc_val)
mycursor.execute("SHOW TABLE creds")

mydb.commit()
