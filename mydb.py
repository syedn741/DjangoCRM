import mysql.connector

dataBase = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'haider1324',

    )

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE CRM_db")

print("All Done!")