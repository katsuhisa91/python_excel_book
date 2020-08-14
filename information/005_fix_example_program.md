## 005「　`get_python_books.py` 24行目のsleep()関数の閉じカッコが抜けている」

### 影響箇所
第7章「7-3-5: 書籍のURLを取り出す」（p227）

### 詳細
`get_python_books.py` 24行目のsleep()関数の閉じカッコが抜けている

誤
```python
time.sleep(1
```

正
```python
time.sleep(1)
```

### 修正計画
（第三版の発売が決定したら、）第三版にて修正予定

### その他
[Issue](https://github.com/katsuhisa91/python_excel_book/issues/7) にも記載済



