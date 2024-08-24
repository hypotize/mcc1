+++
title = "レッスン 33"
date = "2024-06-17T10:00:00+09:00"
author = "小野寺 健"
description = "jupyter notebookでpythonを学ぶ"
showFullContent = false
readingTime = false
tags = ["jupyter", "python", "初級", "turtle"]
+++
# jupyter notebookでpythonを学ぶ
jupyter notebookを使ってPythonを学びましょう
## jupyterとjupyter notebookのインストール
jupyterがインストールされているか、ターミナルから以下のコマンドで確認しましょう。
```
ls ~/.local/bin
```
表示された中に`jupyter`が入っていれば、インストール済みです。入っていなかった場合は、以下のコマンドでjupyterをインストールします。
```
pip3 install jupyter
```
また、先ほどのコマンドで`jupyter-notebook`が表示されているかどうかも確認します。入っていなければ、以下のコマンドでインストールします。
```
pip3 install notebook
```
## jupyter notebookの実行
まず、ターミナルから以下のコマンドでmcc1/code/jupyterの下に移動します。
```
cd ~/mcc1/code/jupyter
```
次に以下のコマンドで`jupyter notebook`を実行します。
```
~/.local/bin/jupyter notebook
```
するとコマンドラインにメッセージが表示された後、ブラウザが自動的に立ち上がってjupyterのHome画面が表示されます。

## turtle.ipynbの実行
Filesのタブに「python入門.ipynb」と「turtle.ipynb」が表示されているので、「turtle.ipynb」をダブルクリックすると「タートルグラフィック入門」が表示されます。

あとは、表示内容に沿って[]: が表示されている行にpythonのプログラムを入力し、▶ボタンを押すことで、pythonのプログラムが実行されていきます。

## python入門.ipynbの実行
「turtle.ipynb」が終わったら、Homeタブに戻り、今度は「python入門.ipynb」をダブルクリックすると「プログラミング入門(python)」が表示されます。

turtle.ipynbと同様に表示内容に沿って[]: が表示されている行にpythonのプログラムを入力し、▶ボタンを押すことで、pythonのプログラムが実行されていきます。

## Pythonによるアルゴリズム入門１.ipynbの実行
「Pythonによるアルゴリズム入門１.ipynb」をクリックすると「Pythonによるアルゴリズム入門（その１）」が表示されます。

表示内容に従ってQ001からQ009までの演習問題を解きましょう。

わからないときは「▶　ヒント」をクリックするとヒントが表示されます。

それでもわからないときは「▶　解答例と解説」をクリックすると解答例と解説を見ることができます。

## Pythonによるアルゴリズム入門２.ipynbの実行
「Pythonによるアルゴリズム入門（その１）」の続きです。

「Pythonによるアルゴリズム入門（その１）」が終わったら、「Pythonによるアルゴリズム入門２.ipynb」をクリックすると「Pythonによるアルゴリズム入門（その２）」が表示されます。

表示内容に従ってQ010からQ020までの演習問題を解きましょう。
