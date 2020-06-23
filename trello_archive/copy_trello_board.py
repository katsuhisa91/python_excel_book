import json

import requests

with open('trello_api_info.json', 'r', newline='') as f:
    api_data = json.loads(f.read())
    TRELLO_APP_KEY = api_data['key']
    TRELLO_APP_TOKEN = api_data['token']

sample_board_member_id = 'katsuhisa_'
sample_board_name = 'sample_board'
# それぞれ、皆さんのTrelloの情報に置き換えてください
your_member_id = 'katsuhisa__'
your_sample_board_name = 'sample_board'


def get_board_id(owner_id, board_name, app_key='', app_token=''):
    params = {
        "key": app_key,
        "token": app_token,
        "fields": "name"
    }
    url = 'https://api.trello.com/1/members/{}/boards'.format(owner_id)
    response = requests.get(url, params)
    board_list = response.json()
    for board in board_list:
        if board_name in board['name']:
            board_id = board['id']
    return board_id


def get_board_lists(board_id, app_key='', app_token=''):
    lists = []
    item = {}
    url = "https://api.trello.com/1/boards/{}/lists".format(board_id)
    params = {
        "key": app_key,
        "token": app_token,
        "fields": "name"
    }
    response = requests.get(url, params)
    list_items = response.json()
    for list_item in list_items:
        item['id'] = list_item['id']
        item['name'] = list_item['name']
        # ミュータブルなオブジェクトをコピーする際は、copy()を使う
        # 単に代入すると、ポインタが同じになるので、最終的にすべて同じ値が入る
        # https://docs.python.org/ja/3.7/library/copy.html
        lists.append(item.copy())
    return lists


def update_board_list(board_id, list_name, app_key, app_token):
    url = "https://api.trello.com/1/boards/{}/lists".format(board_id)
    params = {
        "key": app_key,
        "token": app_token,
        "name": list_name
    }
    response = requests.post(url, params)
    list_item = response.json()
    return list_item['id']


def get_board_cards(list_id, app_key='', app_token=''):
    url = "https://api.trello.com/1/lists/{}/cards".format(list_id)
    params = {
        "key": app_key,
        "token": app_token,
        "fields": "name"
    }
    response = requests.get(url, params)
    card_items = response.json()
    return card_items


def update_board_card(list_id, card_name, app_key, app_token):
    url = "https://api.trello.com/1/lists/{}/cards".format(list_id)
    params = {
        "key": app_key,
        "token": app_token,
        "name": card_name
    }
    requests.post(url, params)


# サンプルボードのIDを取得
sample_board_id = get_board_id(sample_board_member_id, sample_board_name)
# サンプルボードのリスト情報を取得
sample_board_list = get_board_lists(sample_board_id)

# コピー先のボードIDを取得
your_board_id = get_board_id(your_member_id, your_sample_board_name, TRELLO_APP_KEY, TRELLO_APP_TOKEN)

# 左から「やること」「作業中」「完了」の順に表示させるために
# リストを逆順に取り出す
sample_board_list.reverse()
for sample_board_list_item in sample_board_list:
    # コピー先のボードにリストをコピー
    new_list_id = update_board_list(your_board_id, sample_board_list_item['name'], TRELLO_APP_KEY, TRELLO_APP_TOKEN)
    # サンプルボードのカードを取得
    cards = get_board_cards(sample_board_list_item['id'])
    for card in cards:
        # サンプルボードのカード情報で、コピー先のボードを更新
        update_board_card(new_list_id, card['name'], TRELLO_APP_KEY, TRELLO_APP_TOKEN)
