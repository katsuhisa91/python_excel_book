import json
from datetime import datetime, timedelta, timezone
import requests
import pygsheets

# スプレッドシート情報を取得する
with open('spreadsheet_info.json', 'r', newline='') as f:
    sp_data = json.loads(f.read())
    sp_id = sp_data['sp_id']
    service_file_path = sp_data['service_file_path']
    service_file_name = sp_data['service_file_name']

# Trello API 使用に関する情報を取得する
with open('trello_api_info.json', 'r', newline='') as f:
    api_data = json.loads(f.read())
    TRELLO_APP_KEY = api_data['key']
    TRELLO_APP_TOKEN = api_data['token']

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


def create_today_wks(spreadsheet):
    JST = timezone(timedelta(hours=+9), 'JST')
    today_date = datetime.now(JST).strftime("%Y-%m-%d")
    return spreadsheet.add_worksheet(today_date)


def copy_card_to_spreadsheet(card_name, worksheet, row_num):
    worksheet.update_value('A{}'.format(row_num), card_name)


def archive_card(card_id, app_key='', app_token=''):
    url = "https://api.trello.com/1/cards/{}".format(card_id)
    params = {
        "key": app_key,
        "token": app_token,
        "closed": "true"
    }
    requests.put(url, params)


# 作業用のスプレッドシートを準備する
gc = pygsheets.authorize(service_file=service_file_path + '/' + service_file_name)
sp = gc.open_by_key(sp_id)
wks = create_today_wks(sp)

# ボードのリストを取得
your_board_id = get_board_id(your_member_id, your_sample_board_name, TRELLO_APP_KEY, TRELLO_APP_TOKEN)
your_board_lists = get_board_lists(your_board_id, TRELLO_APP_KEY, TRELLO_APP_TOKEN)
for board_list in your_board_lists:
    # 完了リストに対してのみ処理を行う
    if '完了' == board_list['name']:
        done_cards = get_board_cards(board_list['id'], TRELLO_APP_KEY, TRELLO_APP_TOKEN)
        for i, done_card in enumerate(done_cards):
            copy_card_to_spreadsheet(done_card['name'], wks, i + 1)
            archive_card(done_card['id'], TRELLO_APP_KEY, TRELLO_APP_TOKEN)
