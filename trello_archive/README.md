## 8-2 Web APIで、Trelloのデータを取得・操作する
　TrelloというサービスをAPIで操作する演習を行います。

### Trelloとは
　Trelloはカンバン形式でタスク管理を行うことができるサービスです。カンバンは、タスクの流れを一枚のボードに表現することで、仕事の状態を見える化するために活用します。百聞は一見に如かず、ということで、今回の演習で使用するボードをご覧ください。

![image1](https://user-images.githubusercontent.com/13625028/87246283-6e658f00-c487-11ea-9b88-5ad5019e13d7.png)

https://trello.com/b/NmafZJXw/sampleboard

　週はじめに、今週実行したいことを「やること」の列（Trelloの世界では、リストと呼びます）に入れ、作業に着手したタスク（Trelloの世界では、カードと呼びます）を「作業中」に移動し、終わったら「完了」の列に移動させる、といった具合に使用します。

### 例題の説明
　先ほどの画像のボードsample_board（ https://trello.com/b/NmafZJXw/sampleboard ） を公開状態にしているので、TrelloのAPIを使って、皆さんの環境にコピーするプログラムを作成しましょう。

　8-2のプログラムは「trello_archive」というフォルダ内に格納し、最終的に作成するプログラムは「copy_trello_board.py」とします。

### 8-2-1 Trelloの登録とボードの準備
　次のURLから、案内に従いユーザー登録を行ってください。メールアドレスさえあれば、かんたんに登録できます。

https://trello.com/ja/signup

　ユーザー登録完了後、画面上部の「＋」ボタンをクリックし「ボードを作成」をクリック。

![image2](https://user-images.githubusercontent.com/13625028/87246285-7291ac80-c487-11ea-9ecc-e20762d91a60.png)

　「ボードタイトルを追加」という箇所に、適当な名前を入れてください。本演習では、「sample_board」とします。公開方法は、非公開で構いません。これでボードの準備は完了です。ボードの中身は、プログラムをつかって後ほど作成するので、今はボードの中身が空っぽで問題ありません。

### 8-2-2 APIキーとトークンの取得
　4-1節でスプレッドシートのAPIキーを取得したみたく、TrelloのAPIキーを取得します。TrelloのAPIキーは、以下ページから取得します。

https://trello.com/app-key

　開発者契約への同意確認のチェックボックスにチェックを入れ、「APIキーを表示」をクリックすると、画面にAPIキーが表示されるので、コピーしてどこかにメモしておきましょう。

![image3](https://user-images.githubusercontent.com/13625028/87246288-745b7000-c487-11ea-8fde-64136e6ffeb3.png)

#### トークンの取得
　次に、以下URLの「{APIキー}」を、先ほど取得したAPIキーに置き換え、アクセスしてください。{}は不要です。

https://trello.com/1/authorize?expiration=never&name=MyPersonalToken&scope=read,write&response_type=token&key={APIキー}

※ このURLは、Trelloの開発者用ドキュメントから見つけることができます。

https://developer.atlassian.com/cloud/trello/guides/rest-api/authorization/#authorizing-a-client

　URLにアクセスし、画面を最下部までスクロールし「許可」をクリックします。

![image4](https://user-images.githubusercontent.com/13625028/87246292-758c9d00-c487-11ea-82ce-80130b9476ed.png)

　許可を行うと、画面が遷移しトークンが表示されます。こちらもコピーし、どこかに保存しておいてください。APIキーもトークンも、他人に公開しないでください。

#### APIキーの認証情報を別ファイルで管理する
　APIキーとトークンは、プログラムにベタ書きして利用することもできますが、できればプログラムに秘匿情報は入れたくありません。プログラムを共有する際に、誤って共有してしまう可能性があるためです。そこで、APIキーとトークンを別のJSONファイルで管理し、プログラムからは、8-1で学んだ方法を使って読み込むようにします。

trello_api_info.json
```json
{
    "key": "XXXXXXXXXXXX",
    "token": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}
```

---

### コラム：APIドキュメントの読み方
　TrelloのAPIの実行方法を調べましょう。このような場合は「サービス名 API」とGoogleで検索し、公式情報をたどるのが最も早いです。今回の場合は、「Trello API」で検索すると、下記サイトがヒットします。

https://developer.atlassian.com/cloud/trello/rest/

　英語のサイトが表示されますが、APIは、直感的に使える場合が多いため、安心してください。

　ここでは、TrelloのボードIDを取得する方法を調べましょう。ボードのIDを取得するには、ボードを所有しているリソースが何か？をまず考えます。ボードはユーザーの所有物です。そこで、APIドキュメントページの左側のエリアをスクロールして探すと、ユーザーと直接的に表現はされていませんが、「Members」という項目があります。さらに「Members」の項目を詳しくみていくと、「Get Boards that Member belongs to」という項目が見つかります。

![image5](https://user-images.githubusercontent.com/13625028/90302913-94e27400-dee4-11ea-96c5-c274c56816ee.png)

https://developer.atlassian.com/cloud/trello/rest/api-group-members/#api-members-id-boards-get

　APIのエンドポイントを確認すると「/1/members/{id}/boards」となっていることが分かります。また、「GET」と書かれてあることから、HTTPリクエストのgetメソッドでAPIを実行できることも分かりました。

　これは、実際には次のようなAPIを実行します。「 https://api.trello.com は、どこから出てきたんだ？」といった疑問がわく方は、 (公式ドキュメント)[https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/#your-first-api-call] により詳しい説明がのっているので、ご参考になさってください。

 - ボードのIDを取得する

メソッド：GET

https://api.trello.com/1/members/{メンバーのid}/boards

　同様の確認方法で、8-2で利用するAPIのエンドポイントを調べていくと、次のようになります。

 - ボードのリスト情報を取得する / 更新する

メソッド：GET / POST

https://api.trello.com/1/boards/{ボードのid}/lists

 - リストのカード情報を取得する / 更新する

メソッド：GET / POST

https://api.trello.com/1/lists/{リストのID}/cards

　どれも「◯◯が所有する△△を取得（更新）する」という形式（ https://api.trello.com/1/◯◯/{◯◯のid}/△△ ）になっていることが分かります。これを図にすると、次のようになります。

Trelloのデータの関係性

![image6](https://user-images.githubusercontent.com/13625028/87246290-74f40680-c487-11ea-892c-4f80e0789a59.png)

　APIドキュメントの読み方は、どんなWebサービスでも大きく変わりません。多くのWebサービスではRESTという共通の設計原則に従って実装されているので、同じインターフェースで扱うことができるからです。APIと聞くと難しく聞こえるかもしれませんが、慣れればAPIをたたくだけで皆さんのできることを格段に広げてくれる強力な武器となるでしょう。

---

### 8-2-3 サンプルボードのIDを取得する
　本演習の目的は、公開されたsample_boardのリストやカード情報をすべて取得し、皆さんが8-2-1項で作成したボードにコピーすることでした。そのため、まずはsample_boardのIDを取得することからはじめましょう。

1.ボードを持つユーザーIDを調べる

　コラム「APIドキュメントの読み方」にてご説明しましたが、ボードはメンバーの持ち物でした。そのため、ボードIDを取得するAPIを実行するために、メンバーを一意に特定するIDが必要です。メンバーIDは、ボード上に表示されたユーザーアイコンをクリックすることで、調べることができます。

![image7](https://user-images.githubusercontent.com/13625028/87246284-71f91600-c487-11ea-81c8-b2fc2ca31f2d.png)

　@ではじまる英数字の羅列が、メンバーIDです。

![image8](https://user-images.githubusercontent.com/13625028/87246286-732a4300-c487-11ea-9f16-2a483acb45d5.png)

2.メンバーの持つボード一覧を取得する

　メンバーの持つボード一覧を取得するには、requestsモジュールを使い、「https://api.trello.com/1/members/{メンバーのid}/boards」に対しHTTPリクエストのgetメソッドを実行します。このとき、IDだけでなくボードの名前も取得します。取得したボード一覧から、対象ボードの絞り込みを行うために必要だからです。

3.ボードの一覧から、必要なボードの情報を絞り込む

　今回の場合は、ボード名「sample_board」が一致するものを絞り込めばよいですね。ボード一覧をforループで取り出し、ボード名が一致したボードのIDを返しましょう。

　ここまでの流れをプログラムにすると次のようになります。

```python
import requests

sample_board_member_id = 'katsuhisa_'
sample_board_name = 'sample_board'


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


sample_board_id = get_board_id(sample_board_member_id, sample_board_name)
```

　サンプルボードは公開状態にしていることもあり、APIキーとトークンは必要ありませんが、get_board_id()関数はAPIキーとトークンを受け付けられるよう実装しています。こうしておくことで、APIキーとトークンがある場合に、メンバーが所有する非公開状態のボードに対しても同様の関数を使うことができます。

### 8-2-4 サンプルボードのリスト情報を取得する
　ボードIDが分かったので、リストやカードといった、ボード内のリソースを参照できるようになりました。ボード内のリスト一覧を取得するには、「 https://api.trello.com/1/boards/{ボードのid}/lists 」に対し、HTTPリクエストを実行します。

　今回、必要なリストの情報は、IDとリストの名前です。IDは、後ほど、カード情報を取得する際に利用し、リストの名前は最終的に皆さんの演習用ボードを更新する際に元データとして利用します。リスト一つ分の情報は、辞書型オブジェクト「{'id': 'xxx', 'name': 'xxx'}」として扱い、それらを配列に格納することにしましょう。

```python
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


sample_board_list = get_board_lists(sample_board_id)
```

　今回も、先ほどと同様の理由で、get_board_lists()関数の引数にAPIキーとトークンをわたせるように実装してあります。

#### 辞書型のcopy()メソッドの使い所
　辞書型のオブジェクトを配列にappend()メソッドで追加する際は、辞書型のcopy()メソッドを利用します。

```python
lists.append(item.copy())
```

　辞書型やリスト型のような、ミュータブルなオブジェクトをappend()すると、アドレス（コンピュータのメモリ上の、情報が記憶されている場所を示す）が同じ値を参照するため、配列から値を取り出した際に、すべて同じ値となってしまいます。より詳しく知りたい方は、「値渡しと参照渡し」とWebで調べてみるとよいでしょう。

### 8-2-5 演習用ボードのIDを取得する
　リスト情報をすべて取得したので、皆さんの演習用ボードにコピーしましょう。まずは、その前準備として、皆さんのボードIDを取得します。

　皆さんのボードは、非公開状態で作成したため、ボードの情報を取得するには、APIキーとトークンが必要です。8-2-2にて、APIキーとトークンの情報を「trello_api_info.json」という別ファイルに格納したので、jsonモジュールを使って情報を読み取ります。

```python
import json

with open('trello_api_info.json', 'r', newline='') as f:
    api_data = json.loads(f.read())
    TRELLO_APP_KEY = api_data['key']
    TRELLO_APP_TOKEN = api_data['token']
```

　APIキーとトークンを使ってボードのIDを取得するには、先ほど実装したget_board_id()関数を使います。

```python
# それぞれ、皆さんのTrelloの情報に置き換えてください
your_member_id = 'XXXXXXXXXXX'
your_sample_board_name = 'sample_board'

your_board_id = get_board_id(your_member_id, your_sample_board_name, TRELLO_APP_KEY, TRELLO_APP_TOKEN)
```

### 8-2-6 演習用ボードのリストを更新する
　皆さんの演習用ボードIDを取得することができたので、リストを更新します。リストを更新するには「 https://api.trello.com/1/boards/{ボードのid}/lists 」に対し、HTTPリクエストのpostメソッドを実行すればよいです。

　リストを更新する関数は次のようになります。後ほどカード情報を更新するためにリストのIDが必要なので、returnします。

```python
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
```

　8-2-4項で取得したsample_board_listをforループで1つずつ取り出し、update_board_list()関数を実行します。

```python
# 左から「やること」「作業中」「完了」の順に表示させるために
# リストを逆順に取り出す
sample_board_list.reverse()
for sample_board_list_item in sample_board_list:
    # コピー先のボードにリストをコピー
    new_list_id = update_board_list(your_board_id, sample_board_list_item['name'], TRELLO_APP_KEY, TRELLO_APP_TOKEN)
```

　ここまでの処理で、新しいボードには、カードを持たないリスト「やること」「作業中」「完了」が更新されました。

### 8-2-7 サンプルボードのカード情報を取得する
　カードはリストの持ち物なので、カード情報を取得するAPIエンドポイントは「 https://api.trello.com/1/lists/{リストのID}/cards 」となります。

```python
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
```

　リスト内のカード情報取得は各リストに対して行う必要があるので「for sample_board_list_item in sample_board_list:」のループ内で実行します。

```python
for sample_board_list_item in sample_board_list:
    # コピー先のボードにリストをコピー
    new_list_id = update_board_list(your_board_id, sample_board_list_item['name'], TRELLO_APP_KEY, TRELLO_APP_TOKEN)
    # サンプルボードのカードを取得
    cards = get_board_cards(sample_board_list_item['id'])
```

### 8-2-8 ボードのカード情報を更新する
　カード情報の更新を行うには、「 https://api.trello.com/1/lists/{リストのID}/cards 」に対して、HTTPリクエストのpostメソッドを実行します。

```python
def update_board_card(list_id, card_name, app_key, app_token):
    url = "https://api.trello.com/1/lists/{}/cards".format(list_id)
    params = {
        "key": app_key,
        "token": app_token,
        "name": card_name
    }
    requests.post(url, params)
```

　8-2-7項で取得したカードの配列cardsの中身をforループで、1つずつ取り出しながら、update_board_card()関数を実行します。

```python
for sample_board_list_item in sample_board_list:
    # コピー先のボードにリストをコピー
    new_list_id = update_board_list(your_board_id, sample_board_list_item['name'], TRELLO_APP_KEY, TRELLO_APP_TOKEN)
    # サンプルボードのカードを取得
    cards = get_board_cards(sample_board_list_item['id'])
    for card in cards:
        # サンプルボードのカード情報で、コピー先のボードを更新
        update_board_card(new_list_id, card['name'], TRELLO_APP_KEY, TRELLO_APP_TOKEN)
```

　これで、すべての実装が完了しました。完成したプログラムを一つにまとめると、次のようになります。

■プログラム 8-3 Trelloのカードをコピーする（copy_trello_board.py）
```python
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
```

　プログラム実行後、皆さんのTrelloのボードを確認すると、次のようになります。sample_boardの内容がコピーされたことが分かりました。（なお、ボードの背景色は違っていても気にする必要はありません。）

![image9](https://user-images.githubusercontent.com/13625028/87246291-758c9d00-c487-11ea-961d-4f0a593f5449.png)

### さらなる応用
　プログラムを書くことに加え、APIドキュメントを調べながら作業することになるので、慣れない方にとっては難しく感じたかもしれません。しかし、APIドキュメントを読み、プログラムを書くことができれば、本書をここまで読み進めてきた皆さんには、まさに鬼に金棒です。多くのWebサービスは、APIを提供しているので、きっと皆さんの業務を自動化する役に立つでしょう。

