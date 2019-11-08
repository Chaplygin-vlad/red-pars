import api_trello
import psycopg2
import json


def add_trello():
    DB_NAME = "ffcvdwpe"
    DB_USER = "ffcvdwpe"
    DB_PASS = "ehGq2l8TRqXPmdPRmhOr6hy5D2zwoBNt"
    DB_HOST = "salt.db.elephantsql.com"
    DB_PORT = "5432"

    conn = psycopg2.connect(dbname=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    cursor = conn.cursor()
    cursor.execute('SELECT id, header, all_description, comments FROM reddit')
    records = cursor.fetchall()

    board = api_trello.create_board()
    reggit_list = api_trello.create_list(board)

    for id, header, description, comments in records:
        id_card = api_trello.create_card(reggit_list, header, description[:1300])
        # print(type(description),len(description), description )
        comments = comments.split('","')

        for comment in comments:
            comment = comment.replace('"', '')
            comment = comment.replace('{', '')
            comment = comment.replace('}', '')
            api_trello.create_comment(id_card, str(comment))

    cursor.close()
    conn.close()
