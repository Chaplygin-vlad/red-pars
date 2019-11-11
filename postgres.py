import psycopg2


def write_pstgres(header, all_description, comments):
    DB_NAME = "ffcvdwpe"
    DB_USER = "ffcvdwpe"
    DB_PASS = "ehGq2l8TRqXPmdPRmhOr6hy5D2zwoBNt"
    DB_HOST = "salt.db.elephantsql.com"
    DB_PORT = "5432"

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER,
                            password=DB_PASS, host=DB_HOST, port=DB_PORT)

    cursor = conn.cursor()

    _SQL = "insert into reddit (header, all_description,comments) values (%s,%s,%s)"

    cursor.execute(_SQL, (header,
                          all_description,
                          comments))

    conn.commit()
    cursor.close()
    conn.close()


def drop_reddit_comments():
    DB_NAME = "ffcvdwpe"
    DB_USER = "ffcvdwpe"
    DB_PASS = "ehGq2l8TRqXPmdPRmhOr6hy5D2zwoBNt"
    DB_HOST = "salt.db.elephantsql.com"
    DB_PORT = "5432"

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER,
                            password=DB_PASS, host=DB_HOST, port=DB_PORT)

    cur = conn.cursor()
    try:
        cur.execute("drop table reddit_comments")

    except Exception:
        print()

    conn.commit()
    cur.close()
    conn.close()


def drop_reddit_posts():
    DB_NAME = "ffcvdwpe"
    DB_USER = "ffcvdwpe"
    DB_PASS = "ehGq2l8TRqXPmdPRmhOr6hy5D2zwoBNt"
    DB_HOST = "salt.db.elephantsql.com"
    DB_PORT = "5432"

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER,
                            password=DB_PASS, host=DB_HOST, port=DB_PORT)

    cur = conn.cursor()
    try:
        cur.execute("drop table reddit_posts")

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
        ID SERIAL PRIMARY KEY,
        HEADER TEXT NOT NULL,
        ALL_DESCRIPTION TEXT NOT NULL,
        COMMENTS TEXT NOT NULL
        )

        """)

    conn.commit()
    cursor.close()
    conn.close()


def create_reddit_comments():
    DB_NAME = "ffcvdwpe"
    DB_USER = "ffcvdwpe"
    DB_PASS = "ehGq2l8TRqXPmdPRmhOr6hy5D2zwoBNt"
    DB_HOST = "salt.db.elephantsql.com"
    DB_PORT = "5432"

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER,
                            password=DB_PASS, host=DB_HOST, port=DB_PORT)

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE reddit_comments
        (
        id SERIAL PRIMARY KEY,
        comments TEXT NOT NULL,
        post_id INTEGER,
        FOREIGN KEY (post_id) REFERENCES reddit_posts(id)
        )

        """)

    conn.commit()
    cursor.close()
    conn.close()


def create_reddit_posts():
    DB_NAME = "ffcvdwpe"
    DB_USER = "ffcvdwpe"
    DB_PASS = "ehGq2l8TRqXPmdPRmhOr6hy5D2zwoBNt"
    DB_HOST = "salt.db.elephantsql.com"
    DB_PORT = "5432"

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER,
                            password=DB_PASS, host=DB_HOST, port=DB_PORT)

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE reddit_posts
        (
        id SERIAL PRIMARY KEY,
        header TEXT NOT NULL,
        all_description TEXT NOT NULL
        )

        """)

    conn.commit()
    cursor.close()
    conn.close()


def write_posts_reddit(header, all_description):
    DB_NAME = "ffcvdwpe"
    DB_USER = "ffcvdwpe"
    DB_PASS = "ehGq2l8TRqXPmdPRmhOr6hy5D2zwoBNt"
    DB_HOST = "salt.db.elephantsql.com"
    DB_PORT = "5432"

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER,
                            password=DB_PASS, host=DB_HOST, port=DB_PORT)

    cursor = conn.cursor()

    _SQL = "insert into reddit_posts (header, all_description) values (%s,%s)"

    cursor.execute(_SQL, (header,
                          all_description
                          ))

    conn.commit()
    cursor.close()
    conn.close()




def write_comments_reddit(comment, id_post):
    DB_NAME = "ffcvdwpe"
    DB_USER = "ffcvdwpe"
    DB_PASS = "ehGq2l8TRqXPmdPRmhOr6hy5D2zwoBNt"
    DB_HOST = "salt.db.elephantsql.com"
    DB_PORT = "5432"

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER,
                            password=DB_PASS, host=DB_HOST, port=DB_PORT)

    cursor = conn.cursor()

    _SQL = "insert into reddit_comments (comments, post_id) values (%s,%s)"

    cursor.execute(_SQL, (comment,
                          id_post
                          ))

    conn.commit()
    cursor.close()
    conn.close()
