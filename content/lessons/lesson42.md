+++
title = "レッスン 42"
date = "2024-10-01T09:00:00+09:00"
author = "小野寺 健"
description = "Webアプリでクイズをつくろう"
showFullContent = false
readingTime = false
tags = ["Webアプリ", "Python", "Flask"]
+++
# Webアプリでクイズをつくろう
レッスン31でつくったWebアプリをつかって、みんなでクイズをつくってあそびましょう。

## Webアプリをコピーする
レッスン31で１からWebアプリをつくるのはたいへんなので、こんかいはすでにつくってあるものをコピーします。

ターミナルにいかのコマンドをにゅうりょくしてWebアプリをコピーします。
```
cd mcc1
git pull
```

## Flaskのインストール
ターミナルからいかのコマンドをにゅうりょくしてFlaskをインストールします。
```
pip3 install flask
```

## Webアプリをうごかしてみる
Webアプリをうごかすためにターミナルからいかのコマンドをにゅうりょくします。
```
cd code/python/flaskworks
python3 index.py
```
うまくうごいたら、いかのようなメッセージがひょうじされます。
```
 * Serving Flask app 'index'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://XXX.XXX.XXX.XXX:5000
Press CTRL+C to quit
```

うえのメッセージのうち`XXX.XXX.XXX.XXX`というぶぶんは、うごかしているパソコンによってことなります。

## Webアプリのないようをブラウザでみる
Webアプリをうごかしたら、そのないようをブラウザでみます。

ブラウザ(Firefox)をたちあげて、`Google で検索、または URL を入力します`のぶぶんに、`127.0.0.1:5000`とにゅうりょくしましょう。

そうするといかのようながめんがひょうじされます。
          
<table>
    <tr>
    <th>４月を英語で何と言いますか？</th>
    <td><input type='radio' name='Q0' value='April'>April</td>
    <td><input type='radio' name='Q0' value='May'>May</td>
    <td><input type='radio' name='Q0' value='June'>June</td>
    </tr>
    <tr>
    <th>うるう年で月の日数が変わるのは何月ですか?</th>
    <td><input type='radio' name='Q1' value='2月'>2月</td>
    <td><input type='radio' name='Q1' value='3月'>3月</td>
    <td><input type='radio' name='Q1' value='12月'>12月</td>
    </tr>
</table>
<input type="submit" value="解答">

 せいかいをえらんで「解答」ボタンをおすと
 
```
２問中Ｘ問正解
```
 とひょうじされます
 
## じぶんのすきなクイズをつくる
テキストエディタをきどうして、`mcc1/code/python/flaskworks/data.csv`というファイルをひらきます。
 
```
４月を英語で何と言いますか？,April,May,June,April
うるう年で月の日数が変わるのは何月ですか?,2月,3月,12月,2月
```

コンマ(,)でくぎられているファイルをＣＳＶファイルといいます。
このＣＳＶファイルをかきかえてじぶんのすきなクイズをつくります。

１つのぎょうが１もんになります。うえのファイルには２ぎょうあるので、２もんしゅつだいされています。

コンマ(,)でくぎられたぶんをコラムといいます。

- さいしょのコラムはクイズのもんだいです。
- さいごのコラムはクイズのせいかいです。
- ２ばんめのコラムからさいごから１つまえのコラムまでのコラムがクイズのせんたくし（せいかいをふくめた、いくつかのかいとうれい）になります。
- せんたくしのかずはいくつでもかまいません。（うえのファイルでは３つです）
 
それではさっそくじぶんのすきなくいずにかきかえてください。さいしょはためしなので２もんくらいにしておきましょう。
かきかえたら、わすれずにほぞんしてください。

## たしかめる
かきかえたら、クイズがただしくひょうじされるかたしかめます。

```
 * Serving Flask app 'index'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://XXX.XXX.XXX.XXX:5000
Press CTRL+C to quit
```
というメッセージがひょうじされているがめんで「Ctrl」というキーと「C」というきーをどうじにおして、いったんWebアプリをとめます。

そうしたら、もういちど`python3 index.py`をじっこうします。キーボードからにゅうりょくしなくても「▲」キーをおすとターミナルにひょうじされるので、「Enter」キーをおしてじっこうします。

ブラウザの「こうしん」ボタン（まるいやじるしマーク）をおしてがめんをこうしんすると、あなたがつくったクイズがひょうじされます。

## おともだちにクイズをだす
ここまでできたら、ホワイトボードにあなたのなまえと、ターミナルにひょうじされている`XXX.XXX.XXX.XXX`のなまえをかいてください。

おともだちのパソコンのブラウザの`Google で検索、または URL を入力します`のぶぶんに、あなたがホワイトボードかいた`XXX.XXX.XXX.XXX:5000`をいれると、おともだちのパソコンにあなたのクイズがひょうじされます。

おなじように、おともだちがホワイトボードにかいた`XXX.XXX.XXX.XXX:5000`をあなたのパソコンのブラウザににゅうりょくすると、おともだちのクイズがひょうじされます。

## いろいなクイズをつくってみる。
ここまでうまくいったら、あとはじぶんのクイズをいろいろつくってためしてみましょう。
`data.csv`というファイルをまいかいうわがきすると、せっかくつくったまえのクイズがきえてしまうので、べつななまえ（たとえば`data1.csv`とか）でクイズをさくせいし、`cp data1.csv data.csv`で`data.csv`にコピーすれば、いろいろなクイズをけさないで、つかいたいときだけ、`data.csv`にうつすことができます。

コピーなどで`data.csv`をへんこうしたときは、かならず、「Ctrl」＋「C」でWebアプリをとめて、じっこうしなおしてください。（`data.csv`をへんこうしただけでは、Webアプリにはんえいされません）
