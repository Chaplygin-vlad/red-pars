import psycopg2

DB_NAME = "ffcvdwpe"
DB_USER = "ffcvdwpe"
DB_PASS = "ehGq2l8TRqXPmdPRmhOr6hy5D2zwoBNt"
DB_HOST = "salt.db.elephantsql.com"
DB_PORT = "5432"


conn= psycopg2.connect(database = DB_NAME, user = DB_USER,
                           password=DB_PASS, host = DB_HOST, port=DB_PORT)

cur = conn.cursor()
cur.execute("""

CREATE TABLE Reddit
(
HEADER TEXT NOT NULL,
IMAGE TEXT NOT NULL,
NEWS_LINK TEXT NOT NULL,
ALL_TEXT TEXT NOT NULL,
COMMENTS TEXT NOT NULL
)

""")
try:
    cur.execute ("drop table reddit")
except Exception:
    print ('Такой таблицы не существует')

conn.commit()
cur.close()
conn.close()

print('test')