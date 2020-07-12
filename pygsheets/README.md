## 注意点
- service_fileは、ご自身で、Google Cloud Platformからダウンロードしたものをご利用ください
- open_by_keyの対象キーは、スプレッドシートのIDをご利用ください
- その際、スプレッドシート側の権限設定を忘れないように

必要なGoogle Cloud Platform権限は、書籍を参照ください

## 書籍で触れなかった、pygsheetsの使い方

 - シート追加

```python
sp.add_worksheet('A new worksheet')
```

 - 列の取得
 
```python
values = wks.get_col(2, include_tailing_empty=False)
```

 - 行の取得

```python
values = wks.get_row(2, include_tailing_empty=False)
```

 - すべての値の取得
 
```python
values = wks.get_all_values(returnas='matrix',
                            include_tailing_empty=False,
                            include_tailing_empty_rows=False)
```