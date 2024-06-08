+++
title = "レッスン 31"
date = "2024-06-07T09:00:00+09:00"
author = "小野寺 健"
description = "Webアプリを作ろう"
showFullContent = false
readingTime = false
tags = ["Webアプリ", "Python", "Flask"]
+++
# Webアプリを作ろう
## アプリとは
アプリとはアプリケーションソフトウェア(Application Software)の略で、スマホ、タブレット、PC等の上で動くソフトウェアのことです。

アプリには大きく分けて以下の２つがあります。
* ネイティブアプリ
* Webアプリ

### ネイティブアプリとは
ネイティブアプリは、スマホ、タブレット、PC等にソフトウェアをダウンロードして、スマホ、タブレット、PC等の上でソフトウェアが動作します。従って必ずしもネットワークに繋がっている必要はありません。

### Webアプリとは
一方、Webアプリは、スマホ、タブレット、PC等に搭載されているWebブラウザ（Chrome, Edge, Safari等）上で動作し、実際のソフトウェアはネットワークに繋がったサーバー上で動作します。ソフトウェアをダウンロードする必要はありませんが、必ずネットワークに繋がっている必要があります。

## Webアプリの開発環境(Flask)
Webアプリを作成するためにはサーバーを作成する必要があります。python上で簡単にWebサーバーを作成できるフレームワークとしてFlaskというフレームワークがあります。

今回はこのFlaskというフレームワークを使用して簡単なWebアプリを作成してみましょう。

## Flaskのインストール
ターミナルから以下のように`pip3`コマンドを使ってFlaskをインストールします。
```
pip3 install flask
```

## Flask開発環境の作成
`mcc1/code/python`の下に`flaskworks`というディレクトリ（フォルダ）を作成し、そのディレクトリに移動します。

ターミナルで、以下のコマンドを実行します。
```
cd mcc1/code/python
mkdir flaskworks
cd flaskworks
```

## 簡単なサーバープログラムの作成
テキストエディタを開いて、以下のプログラムを作成し、`index.py`という名前で先ほど作成した`flaskworks`ディレクトリ上に保存します。

index.py
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__=='__main__':
    app.debug = True
    app.run()
```

## サーバープログラムの実行
ターミナルから`flaskworks`ディレクトリ上で以下のプログラムを実行します。
```
python3 index.py
```
すると、以下のようなメッセージが出力されます。
```
* Serving Flask app 'index'
* Debug mode: on
* Runnning on http://127.0.0.1:5000
* Restarting with stat
* Debugger is active!
* Debugger PIN: ***-***-***
```

## Webブラウザを実行
Webブラウザを起動し、上記`http://127.0.0.1:5000`をコピぺして実行してみましょう。
以下の画面が表示されます。
```
Hello World
```
これでサーバープログラムで作成した内容がWebブラウザに表示されるようになりました。

## テンプレート利用環境の作成
文字を表示するだけでなく、いろいろなホームページの機能を利用できるようにするため、テンプレートを作成します。

そのため、ターミナルで以下のディレクトリを作成します。
```
mkdir templates
```

## テンプレートファイルの作成
テキストエディタで上記`templates`ディレクトリの下に以下のファイルを作成し、`base.html`という名前で保存します。
```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <p>{{ message }}</p>
    {% block content %}
    {% endblock %}
</body>
</html>
```
`{{ message }}`はFlaskの変数です。この後記述する index.py で渡される情報になっています。

`{% block content %}{% endblock %}`　この2つはこれから「読み込む」テンプレートファイルの場所を確保するためのコードとなります。以下のように使用します。

## テンプレートファイルを利用する
### index.htmlの作成
まずテキストエディタで上記テンプレートファイルを利用した、`index.html`というファイルを作成します。
```html
{% extends "base.html" %}
{% block content %}
    <p>テンプレートだよ</p>
{% endblock %}
```
`{% extends "base.html" %}`の1行で先程書いた`base.html`を呼び出し、`index.html`の`{% block content %} {% endblock %}`内に書かれたものを`base.html`の`{% block content %} {% endblock %}`に上書きする、という処理になっています。
### index.pyの変更
先ほどの`index.py`を`index.html`を使用するように以下のように書き換えます。
```python
from flask import Flask, render_template
app = Flask(__nama__)

@app.route('/')
def index():
    return render_template('index.html', message='Hello')

if __name__=='__main__':
    app.debug = True
    app.run()
```
### 実行
ファイルを変更すると自動的にサーバーは再起動されますが、うまくいかないときは、ターミナルからコントロールCを押して、プログラムを中断し、以下のコマンド
```
python3 index.py
```
を実行して、修正した`index.py`を反映させます。
ブラウザを再読み込みすると以下のような画面が表示されます。
```
Hello

テンプレートだよ
```
`message=''`に様々な文字に変えるとHelloの部分が変わります。

## ルーティング
１つのサーバーから、色々なページのデータを取得できる仕組みのことを**ルーティング**といいます。
### index.pyの書き換え
`index.py`を書き換えて、ルーティングの仕組みを学びましょう。
```python
from flask import Flask, render_template
app = Flask(__nama__)

@app.route('/')
def index():
    return render_template('index.html', message='indexページ')

@app.route('/hello/')
def hello():
    return render_template('index.html', message='Hello World')

if __name__=='__main__':
    app.debug = True
    app.run()
```
### 実行
```
python3 index.py
```
を再実行します。
今まで通り、`http://127.0.0.1:5000/`にアクセスすると
```
indexページ

テンプレートだよ
```
と表示されます。

一方、`http://127.0.0.1:5000/hello/`にアクセスすると
```
Hello World

テンプレートだよ
```
と表示されます。

このように**ルーティング**の仕組みを使うと、色々なページのデータを取得できるようになります。

## フォームを受け取る
フォームから入力データを受け取ってみましょう。
### base.htmlの書き換え
フォームに対応するように`base.html'を以下のように書き換えます。
```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <form method="post" action="/send">
        <input type="text" id="msg" name="msg">
        <input type="submit" value="名前">
    </form>
    {% block content %}
    {% endblock %}
</body>
</html>
```
### index.htmlの書き換え
`index.html`を以下のように書き換えます。
```html
{%extends "base.html" %}
{% block content %} 
    <p>{{ message }}</p>
{% endblock %}
```
### index.pyの変更
`index.py`を以下のように変更します。
```python
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        msg = request.form['msg']
        return render_template('index.html', message='私の名前は'+msg+'です。')
    else:
        return render_template('index.html', message='入力されていません。')

if __name__=='__main__':
    app.debug = True
    app.run()
```
### 実行
ターミナルから再実行します。
```
python3 index.py
```
ブラウザから`http://127.0.0.1:5000/`にアクセスすると以下のように表示されます。

<input type="text" id="msg" name="msg">
<input type="submit" value="名前">

フォームに「山田太郎」と入力して「名前」ボタンを押すと、アクセス先が`http://127.0.0.1:5000/send`に変わり、以下のように表示されます。

<input type="text" id="msg" name="msg">
<input type="submit" value="名前">
<p>私の名前は山田太郎です。</p>

ちなみに、ブラウザから直接`http://127.0.0.1:5000/send`にアクセスすると、以下のように表示されます。

<input type="text" id="msg" name="msg">
<input type="submit" value="名前">
<p>入力されていません。</p>

## 簡単なクイズを作る
フォームから入力データを受け取る仕組みを使って簡単なクイズを作ってみましょう。

問題を作成し、解答が当たっていたら「正解です」、外れていたら「不正解です」と表示します。

問題は解答が１つしかないものにします。例えば、「４月を英語で何というでしょう。すべて小文字で答えてください」という問題にします。
### base.htmlの書き換え
質問と解答に対応するように`base.html'を以下のように書き換えます。
```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    {% block question %}
    {% endblock %}
    <form method="post" action="/send">
        <input type="text" id="msg" name="msg">
        <input type="submit" value="解答">
    </form>
    {% block answer %}
    {% endblock %}
</body>
</html>
```
### index.htmlの書き換え
質問と解答に合わせて、`index.html`を以下のように書き換えます。
```html
{%extends "base.html" %}
{% block question %}
    <p> ４月を英語で何というでしょう。すべて小文字で答えてください </p>
{% endblock %}
{% block  answer %} 
    <p>{{ message }}</p>
{% endblock %}
```
### index.pyの変更
解答が合っているか否かを判断するよう、`index.py`を以下のように変更します。
```python
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        msg = request.form['msg']
        if msg == 'april':
            return render_template('index.html', message=msg+': 正解です。')
        else:
            return render_template('index.html', message=msg+': 不正解です。')
    else:
        return render_template('index.html', message='解答が入力されていません。')

if __name__=='__main__':
    app.debug = True
    app.run()
```
### 実行する
実行すると以下のように表示されます。

<p>４月を英語で何と言いますか？以下から正解を選択してください</p>
<input type="text" id="msg" name="msg">
<input type="submit" value="解答">

正しく入力すると
<p>４月を英語で何と言いますか？以下から正解を選択してください</p>
<input type="text" id="msg" name="msg" value="april">
<input type="submit" value="解答">
<p>正解です。</p>

と表示され、間違っていると
<p>４月を英語で何と言いますか？以下から正解を選択してください</p>
<input type="text" id="msg" name="msg" value="june">
<input type="submit" value="解答">
<p>不正解です。</p>

と表示されます。

なお、値を入力しないで解答ボタンを押したり、ブラウザから直接`http://127.0.0.1:5000/send`にアクセスすると、以下のように表示されます。

<p>４月を英語で何と言いますか？以下から正解を選択してください</p>
<input type="text" id="msg" name="msg">
<input type="submit" value="名前">
<p>解答が入力されていません。</p>


## ラジオボタンで選択する
クイズの答えを入力するのに文字を入力するようにすると、答えが完全に一致しないと正解かどうか判断できません。

そこで、いくつかの答えから正解を選択するように「ラジオボタン」を使用するように変更してみます。

先ほどの問題を以下のように変更します。

<p>４月を英語で何と言いますか？以下から正解を選択してください</p>
<input type='radio' name='question' value='April'>April
<input type='radio' name='question' value='May'>May
<input type='radio' name='question' value='June'>June
<p>
<input type='submit' value='解答'>

### base.htmlの書き換え
ラジオボタンに対応するように`base.html'を以下のように書き換えます。
```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <form method="post" action="/send">
            {% block question %}
            {% endblock %}
        <input type="submit" value="解答">
    </form>
    {% block answer %}
    {% endblock %}
</body>
</html>
```
### index.htmlの書き換え
ラジオボタンに合わせて、`index.html`を以下のように書き換えます。
```html
{%extends "base.html" %}
{% block question %}
    <p>４月を英語で何と言いますか？以下から正解を選択してください</p>
    <input type='radio' name='question' value='April'>April
    <input type='radio' name='question' value='May'>May
    <input type='radio' name='question' value='June'>June
    <p>
{% endblock %}
{% block  answer %} 
    <p>{{ message }}</p>
{% endblock %}
```
### index.pyの変更
ラジオボタンで選択した解答が合っているか否かを判断するよう、`index.py`を以下のように変更します。
```python
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST' and 'question' in request.form:
        msg = request.form['question']
        if msg == 'April':
            return render_template('index.html', message=msg+': 正解です。')
        else:
            return render_template('index.html', message=msg+': 不正解です。')
    else:
        return render_template('index.html', message='解答が入力されていません。')

if __name__=='__main__':
    app.debug = True
    app.run()
```

### 実行
ターミナルから再実行します。
```
python3 index.py
```
ブラウザから`http://127.0.0.1:5000/`にアクセスすると以下のように表示されます。

４月を英語で何と言いますか？以下から正解を選択してください<br>
<input type='radio' name='question' value='April'>April
<input type='radio' name='question' value='May'>May
<input type='radio' name='question' value='June'>June
<br>
<input type='submit' value='解答'>

正解を入力すると「April: 正解です」、間違っていると
「May: 不正解です」あるいは「June: 不正解です」と表示されます。

なお、値を入力しないで解答ボタンを押したり、ブラウザから直接`http://127.0.0.1:5000/send`にアクセスすると、「解答が入力されていません。」と表示されます。
## データからの読み込み
クイズの内容を変える度に、問題と答えをテンプレートやプログラム上で書き換えるのは大変なので、データから読み出すように変更します。

データは最終的にはCSVファイルから読み込むようにしますが、まずは以下のデータリストに設定します。
```python
data = ['４月を英語で何と言いますか？以下から正解を選択してください', 'April', 'May', 'Jun', 'April']
```
データリストは、「問題、選択肢１、選択肢２...、解答」という風になっています。
###  base.html
`base.html`は変更ありません。
### index.html
```html
{%extends "base.html" %}
{% block question %}
    <p>{{ question }} </p>
    {% for choice in choices %}
        <input type='radio' name='question' value='{{ choice }}'>{{ choice }}
    {% endfor %}
    <p>
{% endblock %}
{% block  answer %} 
    <p>{{ answer }}</p>
{% endblock %}
```
質問を「question」変数、解答を「answer」変数、選択肢を「choices」リスト変数に置き換えます。
### index.pyの変更
データリストから上記変数に変換して呼び出すよう、`index.py`を以下のように変更します。
```python
from flask import Flask, render_template, request
app = Flask(__name__)

data = ['４月を英語で何と言いますか？以下から正解を選択してください', 'April', 'May', 'June', 'April']

@app.route('/')
def index():
    return render_template('index.html', question=data[0], choices=data[1:-1])

@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST' and 'question' in request.form:
        answer = request.form['question']
        if answer == data[-1]:
            return render_template('index.html', question=data[0], choices=data[1:-1],answer=answer+': 正解です。')
        else:
            return render_template('index.html', question=data[0], choices=data[1:-1],answer=answer+': 不正解です。')
    else:
        return render_template('index.html', question=data[0], choices=data[1:-1], answer='解答が入力されていません。')

if __name__=='__main__':
    app.debug = True
    app.run()
```
### 実行
ターミナルから再実行します。
```
python3 index.py
```
先ほどと同じ結果が得られるはずです。
## CSVファイルからの読み込み
先ほどのデータを以下のようなCSVファイルにして、`index.py`と同じフォルダに`data.csv`という名前で保存します。
```
４月を英語で何と言いますか？以下から正解を選択してください,April,May,Jun,April
```
### index.pyの変更
htmlファイルの変更はありません。

CSVファイルからデータリストに読み込むよう、`index.py`を以下のように変更します。

```python
from flask import Flask, render_template, request
import csv
app = Flask(__name__)

data = None

@app.route('/')
def index():
    return render_template('index.html', question=data[0], choices=data[1:-1])

@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        answer = request.form['question']
        if answer == data[-1]:
            return render_template('index.html', question=data[0], choices=data[1:-1],answer=answer+': 正解です。')
        else:
            return render_template('index.html', question=data[0], choices=data[1:-1],answer=answer+': 不正解です。')
    else:
        return render_template('index.html', answer='解答が入力されていません。')

if __name__=='__main__':
	with open('data.csv', encoding='utf_8') as f:
		reader = csv.reader(f)
		data = [row for row in reader][0]
	app.debug = True
	app.run()
```
### 実行
実行して、結果が変わらないことを確認しましょう。

## 複数の問題に対応する
１問だけではつまないので、複数の問題に対応できるようにしましょう。

問題のCSVファイル`data.csv`を以下のように複数の問題に変更します。
```
４月を英語で何と言いますか？,April,May,June,April
閏年で月の日数が変わるのは何月ですか?,2月,3月,12月,2月
```

###  base.html
`base.html`は変更ありません。
### index.html
答えも複数あるので、答えも項目ごとに「正解」か「不正解」にするよう変更します。
```html
{%extends "base.html" %}
{% block question %}
    <table>
    {% for item in items %}
		<tr>
        <th>{{ item.question }} </th>
        {% for choice in item.choices %}
            <td><input type='radio' name='{{ item.id }}' value='{{ choice }}' {% if item.selected == choice %}checked{% endif %}>{{ choice }}</td>
        {% endfor %}
        <td>
		{% if item.result == 1 %}
			正解
		{% elif item.result == -1 %}
			不正解
        {% elif item.result == -2 %}
            未入力
		{% endif %}
        </td>
		</tr>
    {% endfor %}
    </table>
{% endblock %}
{% block answer %}
	{{ answer }}
{% endblock %}
```
### index.pyの変更
```python
from flask import Flask, render_template, request
import csv
app = Flask(__name__)

items = []

@app.route('/')
def index():
	for item in items:
		item['result'] = 0
		item['selected'] = ''
	return render_template('index.html', items=items)

from flask import Flask, render_template, request
import csv
app = Flask(__name__)

items = []

@app.route('/')
def index():
	for item in items:
		item['result'] = 0
		item['selected'] = ''
	return render_template('index.html', items=items)

@app.route('/send', methods=['GET','POST'])
def send():
	if request.method == 'POST':
		cnt = 0
		for item in items:
            if item['id'] in request.form:
			    answer = request.form[item['id']]
			    if answer == item['answer']:
				    item['result'] = 1
				    cnt += 1
			    else:
				    item['result'] = -1
			    item['selected'] = answer
            else:
                item['result'] = -2
                item['selected'] = ''
		return render_template('index.html', items=items, answer=str(len(items))+'問中'+str(cnt)+'問正解')
	else:
		for item in items:
		    item['result'] = -2
		    item['selected'] = ''
	    return render_template('index.html', items=items, answer='解答が入力されていません。')

if __name__=='__main__':
	with open('data.csv', encoding='utf_8') as f:
		reader = csv.reader(f)
		for id, row in enumerate(reader):
			item = dict()
			item['id'] = 'Q'+str(id)
			item['question'] = row[0]
			item['choices'] = row[1:-1]
			item['result'] = 0
			item['answer'] = row[-1]
			item['selected'] = ''
			items.append(item)
	app.debug = True
	app.run()
```
### 実行
実行すると以下のように表示されます。

<table>
    <tr>
    <th>４月を英語で何と言いますか？</th>
    <td><input type='radio' name='Q0' value='April'>April</td>
    <td><input type='radio' name='Q0' value='May'>May</td>
    <td><input type='radio' name='Q0' value='June'>June</td>
    </tr>
    <tr>
    <th>閏年で月の日数が変わるのは何月ですか?</th>
    <td><input type='radio' name='Q1' value='2月'>2月</td>
    <td><input type='radio' name='Q1' value='3月'>3月</td>
    <td><input type='radio' name='Q1' value='12月'>12月</td>
    </tr>
</table>
<input type="submit" value="解答">

値を入力すると以下のように表示されます。

<table>
    <tr>
    <th>４月を英語で何と言いますか？</th>
    <td><input type='radio' name='Q0' value='April' checked>April</td>
    <td><input type='radio' name='Q0' value='May'>May</td>
    <td><input type='radio' name='Q0' value='June'>June</td>
    <td>正解</td>
    </tr>
    <tr>
    <th>閏年で月の日数が変わるのは何月ですか?</th>
    <td><input type='radio' name='Q1' value='2月'>2月</td>
    <td><input type='radio' name='Q1' value='3月'>3月</td>
    <td><input type='radio' name='Q1' value='12月' checked>12月</td>
    <td>不正解</td>
    </tr>
</table>
<p>
<input type="submit" value="解答">
<p>2問中1問正解</p>

## 課題
`data.csv`を書き換えて、いろいろなクイズを作成してみましょう。