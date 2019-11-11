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
    cursor.execute('SELECT id, header, all_description FROM reddit_posts')
    records = cursor.fetchall()

    board = api_trello.get_reggit_board()
    if board is None:
        board = api_trello.create_board()
    reggit_list = api_trello.get_reggit_list()
    if reggit_list is None:
        reggit_list = api_trello.create_list(board)
    for id, header, description in records:
        id_card = api_trello.create_card(reggit_list, header, description[:1300])
        id = str(id)
        cursor.execute('SELECT id, comments FROM reddit_comments WHERE post_id = %s', (id))
        comments = cursor.fetchall()

        for id, comment in comments:
            api_trello.create_comment(id_card, comment)

    cursor.close()
    conn.close()



