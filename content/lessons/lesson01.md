+++
title = "レッスン 01"
date = "2022-04-03T08:30:00+09:00"
author = "Michael Cashen"
description = ""

showFullContent = true
readingTime = false
+++

# レッスンの目標
他の人が遊べてちょっと楽しい2Dのミニゲームを作ること！

![Screen shot of Lesson 1 games](/images/lesson1_ss.png)


# 勉強すること
下記のゲームの基本の要素が勉強できます。
* 背景
* スプライト (登場人物)　 - 動きとかロジック
* 数学 - ゲームの世界は数学が少し必要

今回のゲームにはでて来ないけど、ゲームの中で大事な要素としては下記のがあります。
* BGM（音楽）
* 効果音
* ユーザへの遊び方の説明

# 作る方法
今回は2つの作り方を用意しました:
1. スクラッチを用いて、ビジュアルプログラミングをしていく方法。
2. Pythonという言語でpygameというゲームライブラリーを用いて、作る方法。

どの方法でも同じゲームを5つのステップでも作っていけます。

# レッスンの進め方

1. まずは最終形(Step 5)を見てみます。（下記のスクラッチのリンクまたはPythonの動かし方を参照)
2. 次に、Step 1を見てみます。ほぼ何もゲームの要素がありません。ボールが動いているだけです。
3. Step 2から順番に要素を足したり、修正したりします。そのやり方の見本を見る前に自分なりにやり方を考えたりしてみてください。困ったときだけ、見本を見ましょう。
4. ちょっとずつ作っていけば、見本と同じゲームができあがります。そこからは自分なりに変更を加えて、自分流のゲームにしましょう。

# スクラッチのプロジェクトのリンク
|ステップ|リンク|追加要素|
|----|----|----|
|Step 1|https://scratch.mit.edu/projects/668808854/|
|Step 2|https://scratch.mit.edu/projects/669495522/|パドルを追加|
|Step 3|https://scratch.mit.edu/projects/669495836/|ボールがパドルに跳ねる処理|
|Step 4|https://scratch.mit.edu/projects/669495999/|ゲームオーバーとなる線の追加|
|Step 5|https://scratch.mit.edu/projects/669496257/|スコアとスピード調整を追加|

# Pythonでの開発の進め方

* ソースコードを入手。Gitで公開しているので、そのレポジトリをクローンする

{{< code language="shell" id="1" isCollapsed="false">}}
git clone https://github.com/hypotize/mcc1
{{< /code >}}

* python3 で動かす。pygameのインストールが必要な場合、インストールする。今回のレッスンは`0403_lesson`のディレクトリの下にあります。

{{< code language="shell" id="1" isCollapsed="false">}}
python3 -m pip install pygame
cd mcc1/0403_lesson
python3 step5.py
{{< /code >}}

各ステップは step1.py ~ step5.pyのファイルで作成してあります。


