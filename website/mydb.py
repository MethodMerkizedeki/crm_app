import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a databse
cursorObject.execute('CREATE DATABASE elderco')

print('all done')