+++
title = "レッスン 05"
date = "2022-04-30T10:00:00+09:00"
author = "橋本　吉生 + Michael Cashen"
description = "Pythonの画像処理のライブラリーを使って、いろいろな画像の処理の方法をみてみましょう"
showFullContent = false
readingTime = false
+++

# レッスンの目標
好きな画像を自分のパソコンで保存して、Pythonで書かれたプログラム実行して、その画像に色々な画像処理を実行してみましょう。次に、そのプログラムで使われているライブラリーを調べて、少し理解して、余裕があれば、プログラムを微修正してみましょう。

![ Lesson 5 various images](/images/lesson5.png)

# 準備

Pythonのバージョン3で書かれたプログラムを動かします。

まずは、自分のパソコンに今日使うコードを自分のパソコンに持ってきます。三浦コンピュータクラブのGithubのレポジトリー(置き場所)をクローン（コピー）します。今日のためのディレクトリを今日の日付（など）の名前で作って、その中に入れます。
下記にコマンドはコピーでもいいですが、練習のために、自分で丁寧で打ってもよいです。

{{<code language="shell" isCollapsed="false">}}
mkdir 0501
cd 0501
git clone https://github.com/hypotize/mcc1
{{</code>}}

今回のプログラムが入っているディレクトリに入ります。
{{< code language="shell" isCollapsed="false">}}
cd mcc1/code/lesson05 
{{</code >}}
OSのファイルビューアでも同じディレクトリを開いて見ましょう。OSによって異なりますが、下記の近い表示になります。
![Lesson 5 ](/images/lesson5_file_viewer.png)

# 実行

おいてあるREADME.txtを開いて、プログラムの実行方法を確認しましょう。README.txtで書かれているように、必要なPythonのライブラリーをインストールして、image_processing.pyのファイルを実行しましょう。処理の種類ごとにフォルダが作成されて、その中に加工された画像ファイルが保存されます。

# 画像入手

サンプル画像での実行ができ、実行の方法がわかったら、いろいろな画像で試してみましょう。入週方法をいくつか紹介します。

## Pinterest
[Pinterest](https://www.pinterest.jp/)はユーザが好きな画像を集めるサイトです。なかな面白いです。グーグルアカウントを使って、サインアップしましょう。

## Yahooきっず
[https://kids.yahoo.co.jp/](https://kids.yahoo.co.jp/)はこども向けの画像検索のサービスもあります。いろいろな図鑑もあります:[https://kids.yahoo.co.jp/zukan/](https://kids.yahoo.co.jp/zukan/)。好きな画像を見つけたら、右クリックして、画像を保存してください。

## Google画像検索
中学生以上の人はGoogleで画像検索をするのも良いでしょう。

## セルフィー
セルフィー（自分の顔の写真)が取れるソフトはだいたい入っています。MacにはPhoto Booth、LinuxにはCheeseというアプリを立ち上げてあそんでみましょう!隣の人とツーショットも良いでしょう。Windowsなら、Photo Booth Proをインストールして使ってみましょう。

![Selfie](/images/lesson5_selfie.png)

# ソースコードを読みましょう。
画像処理の指示（プログラム）が書かれているファイルを開いて見ましょう。ファイルビューアから`image_processing.py`のファイルを右クリックして、テキストエディターで開きましょう。

## Pillow を調べてみよう
Pythonの画像処理に使うPillowのライブラリーはなかなか強力トです。いろいろできます。正式なドキュメントは[ここ](https://pillow.readthedocs.io/en/stable)]で公開しているが、英語です。しかし、日本語で解説をしている人はいっぱいいます。例えば、色の反転なら、下記の記事が参考になります: [https://note.nkmk.me/python-pillow-invert/](https://note.nkmk.me/python-pillow-invert/)。書かれている方は相当Python好きのようです。

