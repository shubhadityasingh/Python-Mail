import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    database='information',
    user='root',
    password=''
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM information.user")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)