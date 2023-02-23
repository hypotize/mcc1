+++
title = "レッスン 20"
date = "2023-02-23T08:30:00+09:00"
author = "小野寺 健"
description = "ゲーム入門 りんご拾い" 
showFullContent = false
readingTime = false
+++

# レッスンの目標
順番に要素を加えながら、ゲームを作って行きましょう。難しいところは先生と一緒にやりましょう！

![Screen shot of Lesson 20](/images/lesson20.png)

# セットアップ

まずは、gitから先生が作ったコードを自分のパスコンに入れましょう。ターミナルから下記を順番に打ちます。

```shell
cd mcc1
git pull
cd code/python/introduction
```

# キャラ作成

* プレイヤーのキャラクター（動物）とえさのキャラクター（フルーツ）を16x16の大きさで作成します。
* 以前あそんだ絵描きツールをちょっと改造したキャラクター作るための専用のツールがあるので、立ち上げましょう

```shell
python3 paintchar.py
```

* 背景の色は５番の灰色を使い、この色は背景以外には使わないでください。
* 書き終わったら、s キーを押して、保存しましょう。
* screenshot_20230223_101319.pngのような名前で保存されるので、あとでファイル名をもっとわかりやすいものに変更してください。
* サンプルとして、cat.png（猫）とapple.png（リンゴ）を作ってあります。

# コード編集 ステップ1

プレイヤーの画像を表示するだけのゲームを作ります。あまり面白くないですが、大事なスタートです。

プログラムの内容は下記の通りです。game.pyという名前で作成します。１から自分で打ち込んでもいいですし、step1.pyをそのままコピーして名前を変えても構いません。

```python
# 使用するライブラリを呼び出します
import sys
import pygame
from pygame.locals import *

# pygameの初期設定を行います
pygame.init()
SURFACE = pygame.display.set_mode((800, 600))	#Windowサイズは800x600ピクセル
FPSCLOCK = pygame.time.Clock()
TICK = 15	#　描画間隔は１秒間に15コマ

# メインルーチン
def main():
	# プレイヤー（猫）のイメージファイルを読み込み、５倍(80x80)に拡大する
	image = pygame.image.load("cat.png")
	player_image = pygame.transform.scale(image, (80, 80))
	# 描画処理
	while True:	# メインループ
		for event in pygame.event.get():	#　各種イベントを取得
			if event.type == QUIT:	# 右上の×ボタンをクリックしたら終了
				pygame.quit()
				sys.exit()
		SURFACE.fill((0, 0, 0))	#　画面全体を黒で塗りつぶす
		SURFACE.blit(player_image, (375, 225))	# プレイヤー（猫）を描画
		pygame.display.update()	# 画面を更新
		FPSCLOCK.tick(TICK)		# 描画間隔を調整
	
if __name__ == '__main__':	# ここからプログラムスタート
	main()	#メインルーチンを呼び出す
```

"cat.png"の部分をステップ０で自分が作成した動物に変えてみてください。

`game.py`の編集が終わったら、保存して、次のコマンドで実行してみましょう

```Shell
python3 game.py
```

# コード編集 ステップ2

プレイヤー（猫）の背景（灰色の部分）を透過します。プレイヤー（猫）の画像の背景色は灰色なので透過色に灰色(RGB(128,128,128))を指定します。

`player_image = pygame.transform.scale(image, (80, 80))`と書いてある行のあとに、次の一行を追加してください。
```Python
player_image.set_colorkey((128,128,128)) # 灰色(RGB(128,128,128))を透過色にする
```

その一行の追加ができたら、保存して、またこのコマンドで実行してみましょう

```Shell
python3 game.py
```


# コード編集 ステップ3

プレイヤー（猫）を動かします。キーボード操作で上下左右に動かします。

## 3.1

`SURFACE = pygame.display.set_mode((800, 600)) #Windowサイズは800x600ピクセル`の行のあとに、次の一行を追加してください。

```Python
pygame.key.set_repeat(15, 15) # キーを押し続けても一定間隔でイベントを発生させる
```

## 3.2

`player_image.set_colorkey((128,128,128)) # 灰色(RGB(128,128,128))を透過色にする`の行のあとに、次の行を追加してください
```Python
# プレイヤー（猫）の位置を変数に設定する
player_x = 375
player_y = 225
```

## 3.3

```sys.exit() ```
の行のあとに、次の行を追加してください
```Python
			if event.type == KEYDOWN:	# キーが押されたら
				if event.key == K_LEFT:	# ←キーなら
					player_x = max(player_x - 10, 0)	# 0以下にはならない
				if event.key == K_RIGHT:	# →キーなら
					player_x = min(player_x + 10, 720)	# 720以上にはならない
				if event.key == K_UP:	# ↑キーなら
					player_y = max(player_y - 10, 0)	# 0以下にはならない
				if event.key == K_DOWN:	# ↓キーなら
					player_y = min(player_y + 10, 520)	# 520以上にはならない				

```

## 3.4

`SURFACE.blit(player_image, (375, 225))`の行を次の一行に変えてください
```Python
SURFACE.blit(player_image, (player_x, player_y))
```

ここまできたら、もういっかい実行してみましょう。矢印キーを使って、動かしてみましょう。

```Shell
python3 game.py
```

# コード編集 ステップ4

えさのフルーツ（リンゴ）を出現させてみます。一定間隔でランダムな位置（高さ）に出現させ、一定の速度で移動させます。

## 4.1 
5行目に次のインポート文を追加します。
```Python
from random import randint # ランダムな値を発生させる
```

## 4.2
`def main():`の行のあとに次の行を追加します。

```Python
image = pygame.image.load("apple.png")
fruit_image = pygame.transform.scale(image, (80, 80))
fruit_image.set_colorkey((128,128,128)) # 灰色(RGB(128,128,128))を透過色にする
# えさのフルーツ（リンゴ）を一定間隔で4個、ランダムな高さに出現させる。(x, y, 有効)
fruits = [[i * 300, randint(0, 520), True] for i in range(4)]
```

"apple.png"のところは自分が作ったえさの絵のファイル名を指定してください。

## 4.3
`SURFACE.fill((0, 0, 0)) #　画面全体を黒で塗りつぶす`の行を消して、代わりにこの行を追加します。
```Python
                SURFACE.fill((0, 191, 255))     #　画面全体を淡い青で塗りつぶす
                for fruit in fruits:
                        if fruit[2] and fruit[0] < 800: # フルーツが有効で描画範囲内なら指定の位置に描画する                                                  
                                SURFACE.blit(fruit_image, (fruit[0], fruit[1]))
```

## 4.4
`FPSCLOCK.tick(TICK)`の行のあとに次の行を追加します。
```Python
                for fruit in fruits:
                        fruit[0] -= 20  # 各フルーツを左に20移動                
                        if fruit[0] < -40:      # フルーツが左端を超えそうなら右端奥に移動し、高さはランダムに再設定                                                                         fruit[0] += 1200
                                fruit[1] = randint(0, 520)
                                fruit[2] = True # 有効にする
```

ここまできたら、もういっかい実行してみましょう。えさが表示されます。

```Shell
python3 game.py
```

# コード編集 ステップ5

プレイヤー（猫）がえさのフルーツ（リンゴ）を食べます。プレイヤー（猫）がえさのフルーツ（リンゴ）に一定距離近づいたら、えさのフルーツを表示しないようにします。

`for fruit in fruits:`のあとに次に行を足してください
```Python
                       #　命中判定： フルーツが有効で、フルーツの位置（左上）がプレイヤーの位置(左上）の上下左右±60以内なら                                  
                        if fruit[2] and abs(fruit[0] - player_x) < 60 and abs(fruit[1] - player_y) < 60:
                                fruit[2] = False        # フルーツを無効（食べた）にする
```

もういっかい実行してみましょう。えさに近づいたら、消えます。

```Shell
python3 game.py
```

# コード編集 ステップ6

得点を表示します。得点を表示し、プレイヤー（猫）がえさのフルーツ（リンゴ）を食べたら得点を100点追加します。

## 6.1

`fruits = [[i * 300, randint(0, 520), True] for i in range(4)]`のあとに次の行を足します。

```Python
# 点数を表示するフォント（文字種）と大きさを設定する
scorefont = pygame.font.Font("ipaexg.ttf", 24)
# 点数
score = 0
```

## 6.2

`SURFACE.fill((0, 191, 255)) #　画面全体を淡い青で塗りつぶす`のあとに次の行を足します。

```Python
score_image = scorefont.render("Score {:>4}".format(score), True, (255,255,255))
SURFACE.blit(score_image, (20,20))
```
## 6.3

`fruit[2] = False # フルーツを無効（食べた）にする`のあとに次の行を足します。

```Python
score += 100　#100点追加
```

もういっかい実行してみましょう。えさをとると点数が増えます。

```Shell
python3 game.py
```

ここまでお疲れ様でした。次には課題をやってみましょう。ここからは自分で考えないと行けないです。

# 課題１
えさのフルーツの速度を最初はゆっくり、だんだん早くするようにしてみてください。

## ヒント
* 「# 各フルーツを左に20移動」という部分の-20という値を変更すると速度が変わります
* 時間によって速度を変えたければ、ループのカウンタを作って、カウンタの値によって速度を変化させます
* 得点によって速度を変えたければ、得点の値によって速度を変化させます

# 課題２
プレイヤー（猫）は常に左向きですが、動く方向によって向きを変えてください。

ヒント
プレイヤーの左右の向きを変えるのは以下の命令です。TrueとFalseを逆にすると上下の向きが変わります。

```Python
player_image = pygame.transform.flip(player_image, True, False)
```
上下左右のキーを押したとき、現在の向きと異なる場合、向きを変える必要があります。現在の向きを覚えておいて、適切に向きを変えるようにしましょう。まずは、左右だけやってみてください

# 課題３
えさの大きさを、ランダムに大きくしたり、小さくしたりして、命中の難易度を変え、大きさによって得点が変わる（大きいほど点数が低く、小さいほど点数が高い）ようにしてください。

## ヒント
 - えさの情報は現在[x位置、y位置、有効か]の３つですが、これに大きさを追加します。
 - 大きさは現在(80,80)ですが、これをy位置をランダムにしたように、例えばrandint(40,160)で1/2～2倍の範囲に変更します。
 - 変更したら描画のときに変更したsizeを以下の命令を行えば、変更できます。 元のイメージを書き換えるのではなく、描画直前に変更して変更したものを描画するようにしましょう。
```Python
fruit_image = pygame.image.load("apple.png")
[...]
image = pygame.transform.scale(fruit_image, (size, size))
SURFACE.blit(image, (fruit[0], fruit[1]))
```
 - ただし、大きさを変更してもこのままでは命中の難易度が変わらないので、命中判定の部分も変える必要があります。ちょっと難しいけど自分で考えてみてください。
 - 得点も大きさに合わせて変更する必要があります。