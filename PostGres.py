import psycopg2

DB_NAME = "ffcvdwpe"
DB_USER = "ffcvdwpe"
DB_PASS = "ehGq2l8TRqXPmdPRmhOr6hy5D2zwoBNt"
DB_HOST = "salt.db.elephantsql.com"
DB_PORT = "5432"


try:
    conn= psycopg2.connect(database = DB_NAME, user = DB_USER,
                           password=DB_PASS, host = DB_HOST, port=DB_PORT)

    print ("Успешно")

except:
    print ("херово")