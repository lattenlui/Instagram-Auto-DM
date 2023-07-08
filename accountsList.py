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
# mycursor.execute("CREATE TABLE creds (name VARCHAR(255), passwd VARCHAR(255), plan VARCHAR(255))")


print(mycursor.rowcount, "record inserted.")


def already_exists(name):
  #exists = mycursor.execute('Select count(*) from creds where name = ')
  mycursor.execute(
    "SELECT name, COUNT(*) FROM creds WHERE name = %s GROUP BY Name",
    (name,)
  )

  results = mycursor.fetchall()

  row_count = mycursor.rowcount
  print ("number of affected rows: {}".format(row_count))
  if row_count == 0:
      return false
  else:
      return true

def add_account2sql(username, passwd, plan):
    acc_val = (str(username), str(passwd), str(plan))

    mycursor.execute(f"INSERT INTO creds (name, passwd, plan) VALUES {acc_val}")

    # print SQL table
    
    result = mycursor.fetchall()
      
    # loop through the rows
    for row in result:
        print(row)
        print("\n")


    mydb.commit()


def createAccount(username, passwd, plan):

  already_exists = already_exists(username)

  if already_exists:
    return "Error: Account with this username already exists!"

  elif not already_exists: 
    add_account2sql(username, passwd, plan='basic')
    return "Account created successfully!"

  else:
    return "Some Error while creating account. Please report."



