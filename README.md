## 『Pythonでかなえる　Excel作業効率化』サポートページ
本ページは [『Pythonでかなえる　Excel作業効率化』](https://gihyo.jp/book/2020/978-4-297-11450-3) のサポートページです。書籍内のプログラムや、読者特典について案内しています。

![book_image](http://image.gihyo.co.jp/assets/images/cover/2020/9784297114503.jpg)

https://gihyo.jp/book/2020/978-4-297-11450-3

本書目次
```
# Pythonでかなえる　Excel作業効率化
## はじめに

## 第1章　Pythonをはじめよう
### 1-1　Pythonの特徴
#### Column　オープンソースソフトウェア（OSS）はどうして無料なの？
### 1-2　Pythonのインストール
#### 1-2-1　Anacondaのダウンロード
##### Column　Python 2？　Python 3？
#### 1-2-2　Anacondaのインストール
### 1-3　Pythonをさわってみよう
#### 1-3-1　CUIの起動
#### 1-3-2　Pythonの対話モードの起動
### 1-4　PyCharmを使おう
#### 1-4-1　PyCharmのダウンロード
#### 1-4-2　PyCharmのインストール
#### 1-4-3　PyCharmを日本語で利用する
#### 1-4-4　インタープリターの設定
#### 1-4-5　「hello world」と表示するプログラムの作成
##### Column　PyCharmをすぐ呼び出せるようにしておこう

## 第2章　Pythonを動かしてみよう
### 2-1　Pythonのきほん
#### 2-1-1　データの性質
#### 2-1-2　オブジェクトと関数
#### 2-1-3　計算してみよう
#### 2-1-4　異なるデータ型同士の計算
#### 2-1-5　オブジェクトを操作する
#### 2-1-6　同じオブジェクトを使いまわす
### 2-2　ある条件で処理を分ける
#### 2-2-1　条件を判定する
#### 2-2-2　条件に応じて処理をする
### 2-3　オブジェクトをひとまとまりで扱う
#### 2-3-1　中身をあとから変更できるリスト型
#### 2-3-2　中身をあとから変更できないタプル型
##### Column　ミュータブルとイミュータブル
#### 2-3-3　キーと値をセットで扱う辞書型
### 2-4　同じ処理を繰り返し行う
#### 2-4-1　要素の数だけ処理を繰り返す
#### 2-4-2　条件が続く限り処理を繰り返す
#### 2-4-3　処理の途中でループを抜け出す
### 2-5　定義した処理を実行する
#### Column　インデントは半角スペース4つ？
#### 2-5-1　関数にわたす情報・関数から戻ってくる情報
#### 2-5-2　変数が使える範囲
##### Column　エラーメッセージが表示されたら
#### 2-5-3　あらかじめ用意されている関数
### 2-6　ファイルを機能ごとに分けて再利用する
#### 2-6-1　使いたいファイルを読み込ませる
#### 2-6-2　あらかじめ用意されているライブラリを使う
##### Column　サードパーティライブラリ
### 2-7　例外処理

## 第3章　Excel作業を自動化しよう
### 3-1　Excelファイルを操作するための準備
#### 3-1-1　OpenPyXLをインストールする
#### 3-1-2　新しいフォルダの作成
#### 3-1-3　Excelファイルをフォルダに配置する
##### Column　PyCharm上でのファイル移動
### 3-2　Excelの値を表示する
#### 3-2-1　指定したセルの値を取得する
##### Column　取得するセル位置を指定するほかの方法
#### 3-2-2　複数のセルをまとめて取得する
### 3-3　Excelファイルを編集する
#### 3-3-1　Excelファイルを新規作成する
#### 3-3-2　Excelシートを追加／削除する
#### 3-3-3　セルの値を編集する
#### 3-3-4　フォントを設定する
### 3-4　Excelのレイアウトを編集する
#### 3-4-1　Excelの行と列の幅を設定する
#### 3-4-2　行と列を固定表示する
##### Column　#からはじまる行はなに？
### 3-5　Excelのグラフを作成する
#### 3-5-1　グラフが読み込むデータを決める
#### 3-5-2　グラフの種類を決める
#### 3-5-3　グラフにデータをわたす
#### 3-5-4　グラフをつくる
#### 3-5-5　データから系列をつくる
##### Column　PyCharmのコーディングアシスタンスについて
##### Column　GitやGitHubでプログラムを管理しよう

### 第4章　Googleスプレッドシート操作も自動化しよう
#### 4-1　Googleスプレッドシートを操作するための初期設定
#### 4-1-1　Googleアカウントの作成
#### 4-1-2　Google Cloud Platformプロジェクトの作成
#### 4-1-3　スプレッドシートを操作するためのAPIを有効化する
#### 4-1-4　サービスアカウントを作成し，認証情報をダウンロードする
#### 4-1-5　利用ライブラリをインストールする
### 4-2　新しいスプレッドシートを作成する
#### 4-2-1　プログラムがAPIにアクセスできるよう設定する
#### 4-2-2　スプレッドシートを作成する
#### 4-2-3　スプレッドシートの共有権限を変更する
#### 4-2-4　スプレッドシートのURLを表示する
##### Column　新しいシートを追加する
### 4-3　セルの値を取得する
#### 4-3-1　事前準備
#### 4-3-2　スプレッドシートを開く
#### 4-3-3　セルの値を取得する
### 4-4　セルの値を編集する

## 第5章　Excel作業の前工程・後工程を自動化しよう
### 5-1　フォルダ・ファイル操作
#### 5-1-1　絶対パスと相対パス
#### 5-1-2　フォルダにあるファイルを一覧表示する
#### 5-1-3　フォルダを作成する
#### 5-1-4　ファイルの書き込みと読み込み
##### Column　モードオプションw，x，a の選び方
#### 5-1-5　ファイルを移動する
### 5-2　文字列操作
#### 5-2-1　文字列を検索する
##### Column　encoding オプションの指定について
#### 5-2-2　正規表現を使って文字列を検索する
#### 5-2-3　検索一致した文字列の位置を調べる
#### 5-2-4　文字列を置換する
##### Column　よりシンプルな文字列置換
##### Column　format()メソッドで文字列に変数を埋め込む
### 5-3　CSVデータの処理
#### 5-3-1　CSVの出力
##### Column　newlineオプションの指定について
#### 5-3-2　CSVの読み込み
#### 5-3-3　CSVの加工
### 5-4　Webからデータを取得しよう
#### Column　Webから情報を取得する際の注意点

## 第6章　表計算やデータ分析をやってみよう
### 6-1　データ分析を始める前に
#### 6-1-1　ExcelとPythonの使い分け
#### 6-1-2　データ分析の流れ
### 6-2　JupyterLabを使ってみよう
#### 6-2-1　JupyterLabとは
##### Column　Jupyter Notebookとの違いは？
#### 6-2-2　JupyterLabを起動する
#### 6-2-3　実行してみよう
##### Column　新しいファイルの追加
#### 6-2-4　pandasの基本的な使い方
### 6-3　データを分析する
#### 6-3-1　データの準備
#### 6-3-2　データを読み込む
##### Column　データセットの書き込み方法
#### 6-3-3　データを結合する
##### Column　手動でのデータ追加方法
##### Column　欠損値を補うには
#### 6-3-4　データを集計する
### 6-4　データを可視化する
#### 6-4-1　日本語フォントの使用について
#### 6-4-2　棒グラフを作成する
#### 6-4-3　折れ線グラフを作成する
##### Column　プログラムの書き進め方

## 第7章　いろんな業務を自動化してみよう
### 7-1　複数のExcelファイルに分散した売上データを分析する
#### 例題の説明
#### 7-1-1　フォルダの中のExcelファイルを読み込む
#### 7-1-2　各月ごとに分かれている売上データを連結する
##### Column　インポートの順序とグループ化
#### 7-1-3　売上データと顧客流入元データを結合する
#### 7-1-4　顧客流入元ごとの売上合計を集計する
#### 7-1-5　Excelファイルに集計データを出力する
#### さらなる応用
### 7-2　特定のルールに従って，フォルダ構成を整理する
#### 例題の説明
#### 7-2-1　作業用フォルダにすべてのファイルをコピーする
#### 7-2-2　すべてのファイルを取得する
#### 7-2-3　取得したファイルが請求書ファイルかどうかを判別する
##### Column　処理を関数にする基準は？
#### 7-2-4　新しいファイル名とフォルダ名を取得する
#### 7-2-5　新しいフォルダを作成する
#### 7-2-6　ファイル名変更とフォルダ移動を行う
##### さらなる応用
### 7-3　Webスクレイピングでデータを取得する
#### 例題の説明
#### 7-3-1　対象のWebページを確認する
##### Column　クエリパラメータ
#### 7-3-2　Webページから情報を取得する
#### 7-3-3　CSSセレクタを確認する
#### 7-3-4　取得したHTMLを解析する
#### 7-3-5　書籍のURLを取り出す
#### さらなる応用
##### Column　Webページから画像を取得する

## おわりに
## 参考文献
## 索引
## 読者特典
```

---

### 目次

 - [お知らせ](#h1)
 - [プログラムについて](#h2)
 - [読者特典](#h3)

---

### お知らせ<a name="h1"></a>

| 更新日 | お知らせ番号 | お知らせ内容 | 書籍該当箇所 |
| ---- | ---- | ---- | ---- |
| 2020/07/12 | [001](https://github.com/katsuhisa91/python_excel_book/blob/master/information/001_update_github_ui.md) | GitHubのUI変更に伴い、コードをダウンロードするUIが書籍内の情報と異なります | はじめに「コードのダウンロード」(p7) |

---

### プログラムについて<a name="h2"></a>
　書籍内のプログラムと、それぞれの保管場所の一覧です。

#### 第2章「Pythonを動かしてみよう」

|  プログラム番号  |  プログラム名  |
| ---- | ---- |
| 2-1 | [one.py](https://github.com/katsuhisa91/python_excel_book/blob/master/one.py) |
| 2-2 | [hello_world.py](https://github.com/katsuhisa91/python_excel_book/blob/master/hello_world.py) |
| 2-3 | [calc.py](https://github.com/katsuhisa91/python_excel_book/blob/master/calc.py) |
| 2-4 | [calc2.py](https://github.com/katsuhisa91/python_excel_book/blob/master/calc2.py) |
| 2-5 | [calc_string.py](https://github.com/katsuhisa91/python_excel_book/blob/master/calc_string.py) |
| 2-6 | [error_calc_string.py](https://github.com/katsuhisa91/python_excel_book/blob/master/error_calc_string.py) |
| 2-7 | [conversion_type.py](https://github.com/katsuhisa91/python_excel_book/blob/master/conversion_type.py) |
| 2-8 | [upper_string.py](https://github.com/katsuhisa91/python_excel_book/blob/master/upper_string.py) |
| 2-9 | [var_string.py](https://github.com/katsuhisa91/python_excel_book/blob/master/var_string.py) |
| 2-10 | [gtlt.py](https://github.com/katsuhisa91/python_excel_book/blob/master/gtlt.py) |
| 2-11 | [if.py](https://github.com/katsuhisa91/python_excel_book/blob/master/if.py) |
| 2-12 | [if2.py](https://github.com/katsuhisa91/python_excel_book/blob/master/if2.py) |
| 2-13 | [list.py](https://github.com/katsuhisa91/python_excel_book/blob/master/list.py) |
| 2-14 | [list2.py](https://github.com/katsuhisa91/python_excel_book/blob/master/list2.py) |
| 2-15 | [list3.py](https://github.com/katsuhisa91/python_excel_book/blob/master/list3.py) |
| 2-16 | [list4.py](https://github.com/katsuhisa91/python_excel_book/blob/master/list4.py) |
| 2-17 | [tuple.py](https://github.com/katsuhisa91/python_excel_book/blob/master/tuple.py) |
| 2-18 | [tuple2.py](https://github.com/katsuhisa91/python_excel_book/blob/master/tuple2.py) |
| 2-19 | [dict.py](https://github.com/katsuhisa91/python_excel_book/blob/master/dict.py) |
| 2-20 | [dict2.py](https://github.com/katsuhisa91/python_excel_book/blob/master/dict2.py) |
| 2-21 | [for_loop.py](https://github.com/katsuhisa91/python_excel_book/blob/master/for_loop.py) |
| 2-22 | [for_loop2.py](https://github.com/katsuhisa91/python_excel_book/blob/master/for_loop2.py) |
| 2-23 | [for_loop3.p](https://github.com/katsuhisa91/python_excel_book/blob/master/for_loop3.py) |
| 2-24 | [dict_keys_values_items.py](https://github.com/katsuhisa91/python_excel_book/blob/master/dict_keys_values_items.py) |
| 2-25 | [for_loop4.py](https://github.com/katsuhisa91/python_excel_book/blob/master/for_loop4.py) |
| 2-26 | [while.py](https://github.com/katsuhisa91/python_excel_book/blob/master/while.py) |
| 2-27 | [for_loop5.py](https://github.com/katsuhisa91/python_excel_book/blob/master/for_loop5.py) |
| 2-28 | [double.py](https://github.com/katsuhisa91/python_excel_book/blob/master/double.py) ※1 |
| 2-29 | [double2.py](https://github.com/katsuhisa91/python_excel_book/blob/master/double2.py) ※1 |
| 2-30 | [global_var.py](https://github.com/katsuhisa91/python_excel_book/blob/master/global_var.py) ※1 |
| 2-31 | [local_var.py](https://github.com/katsuhisa91/python_excel_book/blob/master/local_var.py) ※1 |
| 2-32 | [hello.py](https://github.com/katsuhisa91/python_excel_book/blob/master/hello.py) |
| 2-33 | [use_hello_module1.py](https://github.com/katsuhisa91/python_excel_book/blob/master/use_hello_module1.py) |
| 2-34 | [use_hello_module2.py](https://github.com/katsuhisa91/python_excel_book/blob/master/use_hello_module2.py) |
| 2-35 | [use_hello_module3.py](https://github.com/katsuhisa91/python_excel_book/blob/master/use_hello_module3.py) |
| 2-36 | [today.py](https://github.com/katsuhisa91/python_excel_book/blob/master/today.py) |
| 2-37 | [fruits.py](https://github.com/katsuhisa91/python_excel_book/blob/master/fruits.py) |
| 2-38 | [fruits_try_exception.py](https://github.com/katsuhisa91/python_excel_book/blob/master/fruits_try_exception.py) |

 ※1...書籍では、関数定義前後の空行（改行のみの行）は一行だけですが、二行空行をいれることが望ましいです。書籍内でも紹介しているPEP-8で、関数定義の前後は、2行ずつ空けることが望ましいと記載されているためです。動作上は空行が何行でも影響はありません。

#### 第3章「Excel作業を自動化しよう」

|  プログラム番号  |  プログラム名  |
| ---- | ---- |
| 3-1 | [get_cell.py](https://github.com/katsuhisa91/python_excel_book/blob/master/openpyxl/get_cell.py) |
| 3-2 | [get_column.py](https://github.com/katsuhisa91/python_excel_book/blob/master/openpyxl/get_column.py) |
| 3-3 | [get_column2.py](https://github.com/katsuhisa91/python_excel_book/blob/master/openpyxl/get_column2.py) |
| 3-4 | [create_excel_file.py](https://github.com/katsuhisa91/python_excel_book/blob/master/openpyxl/create_excel_file.py) |
| 3-5 | [add_sheet.py](https://github.com/katsuhisa91/python_excel_book/blob/master/openpyxl/add_sheet.py) |
| 3-6 | [remove_sheet.py](https://github.com/katsuhisa91/python_excel_book/blob/master/openpyxl/remove_sheet.py) |
| 3-7 | [create_excel_file2.py](https://github.com/katsuhisa91/python_excel_book/blob/master/openpyxl/create_excel_file2.py) |
| 3-8 | [set_formula.py](https://github.com/katsuhisa91/python_excel_book/blob/master/openpyxl/set_formula.py) |
| 3-9 | [set_font.py](https://github.com/katsuhisa91/python_excel_book/blob/master/openpyxl/set_font.py) |
| 3-10 | [set_layout.py](https://github.com/katsuhisa91/python_excel_book/blob/master/openpyxl/set_layout.py) |
| 3-11 | [set_freeze_panes.py](https://github.com/katsuhisa91/python_excel_book/blob/master/openpyxl/set_freeze_panes.py) |
| 3-12 | [add_chart.py](https://github.com/katsuhisa91/python_excel_book/blob/master/openpyxl/add_chart.py) |
| 3-13 | [add_chart2.py](https://github.com/katsuhisa91/python_excel_book/blob/master/openpyxl/add_chart2.py) |

#### 第4章「Googleスプレッドシート操作も自動化しよう」

|  プログラム番号  |  プログラム名  |
| ---- | ---- |
| 4-1 | [create_spreadsheet.py](https://github.com/katsuhisa91/python_excel_book/blob/master/pygsheets/create_spreadsheet.py) |
| 4-2 | [get_cell.py](https://github.com/katsuhisa91/python_excel_book/blob/master/pygsheets/get_cell.py) |
| 4-3 | [update_cell.py](https://github.com/katsuhisa91/python_excel_book/blob/master/pygsheets/update_cell.py) |

#### 第5章「Excel作業の前工程・後工程を自動化しよう」

|  プログラム番号  |  プログラム名  |
| ---- | ---- |
| 5-1 | [getcwd.py](https://github.com/katsuhisa91/python_excel_book/blob/master/os/getcwd.py) |
| 5-2 | [list_current_dir.py](https://github.com/katsuhisa91/python_excel_book/blob/master/os/list_current_dir.py) |
| 5-3 | [list_pycharm_dir.py](https://github.com/katsuhisa91/python_excel_book/blob/master/os/list_pycharm_dir.py) |
| 5-4 | [ist_dir_recursive.py](https://github.com/katsuhisa91/python_excel_book/blob/master/os/list_dir_recursive.py) |
| 5-5 | [make_dir.py](https://github.com/katsuhisa91/python_excel_book/blob/master/os/make_dir.py) |
| 5-6 | [make_txt.py](https://github.com/katsuhisa91/python_excel_book/blob/master/os/make_txt.py) |
| 5-7 | [read_txt.py](https://github.com/katsuhisa91/python_excel_book/blob/master/os/read_txt.py) |
| 5-8 | [move_file.py](https://github.com/katsuhisa91/python_excel_book/blob/master/os/move_file.py) |
| 5-9 | [copy_file.py](https://github.com/katsuhisa91/python_excel_book/blob/master/os/copy_file.py) |
| 5-10 | [rename_file.py](https://github.com/katsuhisa91/python_excel_book/blob/master/os/rename_file.py) |
| 5-11 | [find.py](https://github.com/katsuhisa91/python_excel_book/blob/master/text_search/find.py) |
| 5-12 | [postal_code_findall.py](https://github.com/katsuhisa91/python_excel_book/blob/master/text_search/postal_code_findall.py) |
| 5-13 | [postal_code_findall_2.py](https://github.com/katsuhisa91/python_excel_book/blob/master/text_search/postal_code_findall_2.py) |
| 5-14 | [postal_code_search.py](https://github.com/katsuhisa91/python_excel_book/blob/master/text_search/postal_code_search.py) |
| 5-15 | [sub.py](https://github.com/katsuhisa91/python_excel_book/blob/master/text_search/sub.py) |
| 5-16 | [replace_txt.py](https://github.com/katsuhisa91/python_excel_book/blob/master/text_search/replace_txt.py) |
| 5-17 | [format.py](https://github.com/katsuhisa91/python_excel_book/blob/master/text_search/format.py) |
| 5-18 | [format2.py](https://github.com/katsuhisa91/python_excel_book/blob/master/text_search/format2.py) |
| 5-19 | [make_csv.py](https://github.com/katsuhisa91/python_excel_book/blob/master/csv/make_csv.py) |
| 5-20 | [read_csv.py](https://github.com/katsuhisa91/python_excel_book/blob/master/csv/read_csv.py) |
| 5-21 | [edit_csv.py](https://github.com/katsuhisa91/python_excel_book/blob/master/csv/edit_csv.py) |

#### 第6章「表計算やデータ分析をやってみよう」

|  プログラム番号  |  プログラム名  |
| ---- | ---- |
| - | [sample.ipynb](https://github.com/katsuhisa91/python_excel_book/blob/master/data_analysis/sample.ipynb) |
| - | [sample2.ipynb](https://github.com/katsuhisa91/python_excel_book/blob/master/data_analysis/sample2.ipynb) |
| - | [customer_analysis.ipynb](https://github.com/katsuhisa91/python_excel_book/blob/master/data_analysis/customer_analysis.ipynb) |

#### 第7章「いろんな業務を自動化してみよう」

|  プログラム番号  |  プログラム名  |
| ---- | ---- |
| 7-2 | [analysis_of_sales_channel.py](https://github.com/katsuhisa91/python_excel_book/blob/master/sales_analysis/analysis_of_sales_channel.py) |
| 7-3 | [rename_and_move_invoice_files.py](https://github.com/katsuhisa91/python_excel_book/blob/master/organize_data/rename_and_move_invoice_files.py) |
| 7-5 | [get_python_books.py](https://github.com/katsuhisa91/python_excel_book/blob/master/scraping/get_python_books.py) |
| 7-8 | [get_book_image.py](https://github.com/katsuhisa91/python_excel_book/blob/master/scraping/get_book_image.py) |

以下のプログラム番号のプログラムは、それぞれ途中経過のため記載していません。それぞれ、完成版プログラムをご参照ください。

|  途中経過の<br>プログラム  |  完成版の<br>プログラム  |
| ---- | ---- |
| 7-1 | 7-2 |
| 7-4 | 7-5 |
| 7-6 | 7-8 |
| 7-7 | 7-8 |

---

### 読者特典 : 第8章「Web APIで、SaaSのデータを取得・操作しよう」<a name="h3"></a>
　近年は、社内で複数のSaaSを利用している方も多いでしょう。そこで、Web APIを利用して、SaaSから必要なデータを取り出したり、Python経由でSaaSのデータを操作したりする一連の流れを、読者特典としてご用意しました。

 - [8-1 JSONデータの処理](https://github.com/katsuhisa91/python_excel_book/tree/master/json)
 - [8-2 Web APIで、Trelloのデータを取得・操作する](https://github.com/katsuhisa91/python_excel_book/tree/master/trello_archive)

```
## 第8章　Web APIで、SaaSのデータを取得・操作しよう
### 8-1 JSONデータの処理
#### 8-1-1 JSONの出力
#### 8-1-2 JSONの読み込み
### 8-2 Web APIで、Trelloのデータを取得・操作する
#### 8-2-1 Trelloの登録とボードの準備
### 8-2-2 APIキーとトークンの取得
#### Column　APIドキュメントの読み方
#### 8-2-3 サンプルボードのIDを取得する
#### 8-2-4 サンプルボードのリスト情報を取得する
#### 8-2-5 演習用ボードのIDを取得する
#### 8-2-6 演習用ボードのリストを更新する
#### 8-2-7 サンプルボードのカード情報を取得する
#### 8-2-8 ボードのカード情報を更新する
```

|  プログラム番号  |  プログラム名  |
| ---- | ---- |
| 8-1 | [dumps_json.py](https://github.com/katsuhisa91/python_excel_book/blob/master/json/dumps_json.py) |
| 8-2 | [loads_json.py](https://github.com/katsuhisa91/python_excel_book/blob/master/json/loads_json.py) |
| 8-3 | [copy_trello_board.py](https://github.com/katsuhisa91/python_excel_book/blob/master/trello_archive/copy_trello_board.py) |
