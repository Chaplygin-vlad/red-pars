import requests
import json
from pprint import pprint

token = "9c60addb817a96d319088bdba7eb0a2e74523962dbaae09efb56bd75cc739497"
key = "c2de0db812668e1f432a55aa3fc75de6"


def create_board():
    url = "https://api.trello.com/1/boards/"

    querystring = {"name": "Reggit",
                   "defaultLabels": "true",
                   "defaultLists": "true",
                   "keepFromSource": "none",
                   "prefs_permissionLevel": "private",
                   "prefs_voting": "disabled",
                   "prefs_comments": "members",
                   "prefs_invitations": "members",
                   "prefs_selfJoin": "true",
                   "prefs_cardCovers": "true",
                   "prefs_background": "blue",
                   "prefs_cardAging": "regular",
                   "key": key,
                   "token": token}

    response = requests.post(url, params=querystring)
    board = json.loads(response.text)
    return board['id']


def create_list(id_board):
    url = "https://api.trello.com/1/lists"
    querystring = {"name": "List from Reggit",
                   "idBoard": id_board,
                   "key": key,
                   "token": token}

    response = requests.request("POST", url, params=querystring)

    list_reggit = json.loads(response.text)
    return list_reggit['id']


def create_card(id_list, card_name, card_desc):
    url_create_board = "https://api.trello.com/1/cards"
    querystring = {"idList": id_list,
                   "keepFromSource": "all",
                   "key": key,
                   "token": token,
                   'name': card_name,
                   'desc': card_desc}

    response = requests.request("POST", url_create_board, params=querystring)
    card = json.loads(response.text)
    return card['id']


def create_comment(id_card, comment):
    url = f"https://api.trello.com/1/cards/{id_card}/actions/comments"
    querystring = {"text": comment, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
