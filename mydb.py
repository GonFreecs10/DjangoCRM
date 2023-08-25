import psycopg2
dataBase = psycopg2.connect(
    host = 'localhost',
    user ='postgres',
    password = '1234'
)
cursorObject = dataBase.cursor()
dataBase.autocommit = True #!

cursorObject.execute("CREATE DATABASE yazin")
print("all done")