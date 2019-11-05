import psycopg2


def write_pstgres(data):
    DB_NAME = "ffcvdwpe"
    DB_USER = "ffcvdwpe"
    DB_PASS = "ehGq2l8TRqXPmdPRmhOr6hy5D2zwoBNt"
    DB_HOST = "salt.db.elephantsql.com"
    DB_PORT = "5432"

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER,
                            password=DB_PASS, host=DB_HOST, port=DB_PORT)

    cursor = conn.cursor()

    _SQL = "insert into reddit (header, image, news_link, all_text,comments) values (%s,%s,%s,%s,%s)"

    cursor.execute(_SQL, (data['header'],
                          data['image'],
                          data['news_link'],
                          data['all_text'],
                          data['comments']))

    conn.commit()
    cursor.close()
    conn.close()


def drop_sql():
    DB_NAME = "ffcvdwpe"
    DB_USER = "ffcvdwpe"
    DB_PASS = "ehGq2l8TRqXPmdPRmhOr6hy5D2zwoBNt"
    DB_HOST = "salt.db.elephantsql.com"
    DB_PORT = "5432"

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER,
                            password=DB_PASS, host=DB_HOST, port=DB_PORT)

    cur = conn.cursor()
    try:
        cur.execute("drop table reddit")
    except Exception:
        print()

    conn.commit()
    cur.close()
    conn.close()


def create_sql():
    DB_NAME = "ffcvdwpe"
    DB_USER = "ffcvdwpe"
    DB_PASS = "ehGq2l8TRqXPmdPRmhOr6hy5D2zwoBNt"
    DB_HOST = "salt.db.elephantsql.com"
    DB_PORT = "5432"

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER,
                            password=DB_PASS, host=DB_HOST, port=DB_PORT)

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE Reddit
        (
        HEADER TEXT NOT NULL,
        IMAGE TEXT NOT NULL,
        NEWS_LINK TEXT NOT NULL,
        ALL_TEXT TEXT NOT NULL,
        COMMENTS TEXT NOT NULL
        )

        """)

    conn.commit()
    cursor.close()
    conn.close()
