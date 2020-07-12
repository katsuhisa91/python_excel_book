## 8-1 JSONデータの処理
　JSONは、JavaScript Object Notationの略で、Pythonの辞書型のような形式のテキストデータまたはテキストファイルです。人間にとって読み書きがしやすく、また、データが名前/値のペアの集まりとして表現されているためプログラミングのデータ構造としても扱いやすくマシンフレンドリーだとも言えます。WebシステムやSaaSを外部から利用する際には、JSONデータでやり取りすることが多いです。そのためJSONデータの取り扱いは、様々なWebシステムやSaaSの効率化や自動化に取り組む基礎知識と言えるでしょう。

### 8-1-1 JSONの出力
　本節では「json」フォルダを作成し、その直下にプログラムをつくっていきます。PythonでJSONを取り扱うには、jsonモジュールを使います。以下は、jsonモジュールを使い、Pythonの値をJSONファイルとして書き出すサンプルプログラムです。

■プログラム 8-1 JSONファイルを書き出す（dumps_json.py）
```python
import json

task_data = {
    'id': 1,
    'name': 'Homework',
    'deadline': '2020/09/01'
}

with open('sample.json', 'x', newline='') as f:
    f.write(json.dumps(task_data, indent=4))
```

　jsonフォルダに「sample.json」が生成されていれば成功です。

```
json
├─ dumps_json.py
└─ sample.json
```

sample.json
```json
{
    "id": 1,
    "name": "Homework",
    "deadline": "2020/09/01"
}
```

　まず、task_dataにJSON形式に変換する元データとして、Pythonの辞書型の値を代入します。その後、JSONデータを書き出す対象となるファイルを作成すべく、xモードでopen()します。jsonモジュールのdumps()関数（dump stringの略）を使うことで、引数に指定したPythonの値を、JSON形式の文字列に変換することができます。また、「indent=4」のように指定することで、指定した数の半角スペースをインデントとして指定できます。最後に、生成した「sample.json」を見ると分かりますが、JSONは「"」で囲う必要があります。

### 8-1-2 JSONの読み込み
　次に、先ほど作成した「sample.json」をPythonから読み込みましょう。

■プログラム 8-2 JSONファイルを読み込む（loads_json.py）
```python
import json

with open('sample.json', 'r', newline='') as f:
    sample_data = json.loads(f.read())
    print(sample_data)
```

出力結果
```
{'id': 1, 'name': 'Homework', 'deadline': '2020/09/01'}
```

　PythonでJSONデータを読み込むには、json.loads()関数（load string）を使います。引数にJSON形式の文字列を指定します。出力されたデータから、取り込んだJSONデータは、Pythonの辞書型に変換されたことが分かります。ちなみに、辞書型なので、キーとして名前を指定し、「sample_data['id']」のようにすると、結果として対応する値である「1」が得られます。
