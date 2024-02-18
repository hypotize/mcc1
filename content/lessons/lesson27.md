+++
title = "レッスン 27"
date = "2024-02-01T16:00:00+09:00"
author = "小野寺 健"
description = "落ちものキャッチゲームをpythonで作ろう" 
showFullContent = false
readingTime = false
tags = ["python", "ゲーム", "プログラミング", "上級"]
+++
# レッスンの目標
落ちものキャッチゲームをpython(pygame)で作ろう
## ファイルを作成する
テキストエディタを使って`mcc1/code/python`の下に`catchgame.py`というファイルを作成します。（既に`catchgame.py`は作成済みなので、「プログラムの実行」までの部分は、読むだけで、実際にプログラムを入力しなくても大丈夫です）
## モジュールのインポート
作成したcatchgame.pyに以下のようなpythonコードを入力します。
```python
import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE, K_j, K_f
import random
```
先頭の`import sys`ではシステム関係のモジュールをインポートします。
次の`import pygame`ではpygameというゲーム作成モジュールをインポートし、次の行ではpygameの中で使用する各種イベントをインポートします。
最後の`import random`ではランダム発生モジュールをインポートします。
## 初期化処理を行う
初期化の処理を追加します。
```python
WIDTH = 480
HEIGHT = 360

pygame.init()
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
FPSCLOCK = pygame.time.clock()
```
最初に`pygame.init()`でpygameを初期化します。
スクラッチの座標はx座標系は-240〜240(幅480)、y座標が-180〜180（高さ360）なのでスクラッチの座標系に合わせ480×360で画面を初期化します。
最後に、画像描画間隔を制御するための変数FPSCLOCKを獲得します。
## スプライトの骨組みを作る
スクラッチの「スプライト」の仕組みを真似るため、スプライトの骨組みを作成します。
```python
class Sprite:
	def __init__(self, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.setxy(0, 0)
	def setx(self, x):
		self.rect.centerx = x + WIDTH / 2
	def sety(self, y):
		self.rect.centery = HEIGHT / 2 - y
	def setxy(self, x, y):
		self.setx(x)
		self.sety(y)
	def setdx(self, dx):
		self.rect.centerx += dx
	def setdy(self, dy):
		self.rect.centery -= dy
	def getx(self):
		return self.rect.centerx - WIDTH / 2
	def gety(self):
		return HEIGHT / 2 - self.rect.centery
	def draw(self):
		SURFACE.blit(self.image, self.rect.topleft)
```
初期化関数`__init__()`では、スプライトの画像を受取り、スプライトの画像変数に設定し、画像の描画範囲（矩形）を設定し、位置を(0, 0)に初期化します。
次に座標を設定する関数(setx, sety, setxy)を作成します。
スクラッチの各スプライトの位置は画像の中央なので、画像描画範囲（矩形）の中央に位置を設定します。
また、座標系をスクラッチに合わせるため、設定されたxの値にWIDTH/2を足し、設定されたyの値をHEIGHT/2から引きます。
座標変更関数(setdx, setdy)は設定した値をxに足し、yから引きます。
座標を返す関数(getx, gety)はスクラッチの座標系に変換して返します。
描画関数`draw()`では、スプライトの画像を座標位置に描画します。
## コップを作る
スプライトの骨組みを利用して、コップを作成します。
```python
class Cup(Sprite):
	_image = pygame.image.load("cup.svg")
	def __init__(self, x, y):
		super().__init__(Cup._image)
```
コップの画像ファイル(cup.svg)を`pygame.image.load()`関数に渡して画像に変換してクラス変数(_image)に設定しておき、初期化関数(__init__())の中でスプライトの初期化関数に渡して初期化します。
## メイン関数を作り、関数を呼び出す。
```python
def main():
	cup = Cup()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_SPACE:
					cup.setxy(0, -100)
				elif event.key == K_j:
					if cup.getx() < 100:
						cup.setdx(100)
				elif event.key == K_f:
					if cup.getx() > -100:
						cup.setdx(-100)
		SURFACE.fill((255, 255, 255))
		cup.draw()
		pygame.display.update()
		FPSCLOCK.tick(30)
		
if __name__ == "__main__":
	main()
```
`main()`という関数を定義し、コップを初期化した後、無限ループで繰り返し処理を行います。
無限ループの中ではイベントを獲得し、イベントが「QUIT」（ウィンドウを閉じた）だったらプログラムを終了します。
イベントが「スペースキーを押す」だったら、カップの位置を(0, -100)に設定します。
イベントが「jキーを押す」だったら、x座標が100未満だったら右に100移動します。
イベントが「fキーを押す」だったら、x座標が-100より大きかっら左に移動します。
画面を「白く」描画し、コップを描画し、画面を再描画し、スクラッチ同様、1秒に30回描画するようにします。
最後にメイン関数`main()`を呼びます。
## プログラムの実行
ここまでのプログラムを`catchgame.py`という名前で`mcc1\code\python\CatchGame`の下の作成してありますので、`python3 catchgame.py`を実行してみましょう。
スクラッチの「落ちものキャッチゲームの作り方」で「コップを作る」まで作成して実行した結果と同様、スペースキーを押すとコップが中央下に移動し、fキーで左に、jキーで右に移動することが確認できます。
## ボールを作る
ここからは、実際に自分でプログラムを入力していきましょう。
スプライトの骨組みを利用して、ボールを作成します。
`class Cup(Sprite):`の後、`def main():`の前に以下のプログラムを追加します。
```python
class Ball(Sprite):
	_image = pygame.image.load("ball.svg")
	def __init__(self):
		super().__init__(Ball._image)
```
画像ファイル以外は、コップとほぼ同一です。
次にスタートしたら、1秒毎に自分自身のクローンを作り、座標を(0, 150)に設定してずっとy座標を-5ずつ変える部分を作成します。
```python
...
def main():
	cup = Cup()
	balls = []
	ballcnt = 0
	start = False
	while:
		...
			if event.keu == K_SPAVE:
				cup.setxy(0, -100)
				start = True
		...
		if start:
			ballcnt += 1
			if ballcnt == 30:
				ball = Ball()
				ball.setxy(0, 150)
				balls.append(ball)
				ballcnt = 0
		SURFACE.fill((255, 255, 255))
		cup.draw()
		for ball in balls:
			ball.draw()
			ball.setdy(-5)
		pygame.display.update()
		...
```
ボールは複数作られるので、それを格納するリスト（配列）`balls`を作成し、空で初期化します。
またボールのクローンを作る間隔をカウントする`ballcnt`という変数を用意し、0に初期化します。
また、スタートしたか否かを判断する変数`start`を用意し、`False`に初期化します。
スペースキーが押されたら、`start`変数を`True`にします。
`start`変数が`True`だったら`ballcnt`を1つずつカウントアップし、30になったら（1秒たったら）ボールのクローンを作成して、位置を(0, 150)に設定してボールのリストに追加し、`ballcnt`を0に戻します。
最後に、ボールリストに入っている各ボールを描画し、座標を更新します。
ここまで、できたら実行し、スタートしたらボールが1秒毎に上から落ちてくることを確認してください。
## ボールが下まで落ちたら、「失敗音」を出し、ボールを削除する
ボールが下まで落ちたら、「失敗音」を出し、ボールを削除します。
```python
class Ball(Sprite):
	_image = pygame.image.load("ball.svg")
	def __init__(self):
		super().__init__(Ball._image)
		self.alive = True
```
無効なボールを削除するため、ボールが有効か否かの変数`alive`を追加します。
```python
def main():
	...
	start = False
	failsound = pygame.mixer.Sound("failed.wav")
	while True:
		...
		for ball in balls:
			ball.draw()
			if ball.gety() < -50:
				failsound.play()
				ball.alive = False
			else:
				ball.setdy(-5)
		balls = [ball for ball in balls if ball.alive]
```
まず、失敗音「Oops」を追加し、`failsound`変数に設定します。
ボールのy座標が-50未満の場合、失敗音を鳴らし(`play()`）、ボールを無効にします。
最後に、ボールリストから無効なボールを削除（有効なボールだけ残す）します。
## ボールが下コップに触れたら、「成功音」を出し、ボールを削除する
```python
def main():
	...
	start = False
	failsound = pygame.mixer.Sound("failed.wav")
	succeedsound = pygame.mixer.Sound("succeed.wav")
	while True:
		...
		for ball in balls:
			ball.draw()
			if ball.rect.colliderect(cup.rect):
				succeedsound.play()
				ball.alive = False
			elif ball.gety() < -50:
				failsound.play()
				ball.alive = False
			else:
				ball.setdy(-5)
		balls = [ball for ball in balls if ball.alive]
```
「失敗音」に加え、「成功音」も追加します。
ボールがコップに触れたらというのは、ボールの描画範囲（矩形）`ball.rect`とコップの描画範囲（矩形）`cup.rect`が重なっているか否か`colliderect()`で判定し、重なっていたら成功音を鳴らして、ボールを無効にします。
## ボールの出る位置を左・真ん中・右の中からでたらめに選ぶ
ボールがクローンされたとき、ボールのx座標を-100、0、100のいずれかにします。
そのためには-1, 0, 1の数をでたらめに作ってその値に100をかけ、その値をボールのx座標にします。
```python
				ball = Ball()
				ball.setxy(random.randint(-1, 1) * 100, 150)
```
`random.randint(a, b)`はa以上b以下の整数をでたらめ（ランダム）に返す関数です。
## 3回失敗したらゲームを終了させる
失敗の回数を数える変数`failcnt`を作り、ゲーム開始時に0にします。
```python
def main():
	...
	failcnt = 0
	while True:
	...
				if event.key == K_SPACE:
					cup.setxy(0, -100)
					start = True
					failcnt = 0
```
メイン関数`main()`の初期化部分で失敗回数変数`failcnt`を定義し、0に初期化します。
また、ゲーム開始時には、0に初期化します。
次に失敗したら、失敗回数を1増やし、3回（2より大きく）なったら、ゲームを終了させます。

```python
			elif ball.gety() < -50:
				failsound.play()
				ball.alive = False
				failcnt += 1
				if failcnt > 2:
					start = False
					balls.clear()
```
ウィンドウを閉じたときのように`pygame.quit()`と`sys.exit()`を呼ぶようにすれば完全にプログラムは終了しますが、スクラッチのように再開できないので、`start`変数とボールリストを空にすることで、擬似的にゲーム終了状態にします。
プログラムは終了していないので、「スペースキーを押す」ことでいつでもゲームを再開できます。
## 失敗回数を画面に表示する
スクラッチでは、新規に作成した変数は初期値の「表示チェック」をはずさなければ、画面上に値が表示されます。
一方、python(pygame)では、変数を定義しただけでは表示してくれないので、スクラッチのように表示したい場合は、表示用のプログラムを追加する必要があります
```python
def main():
	...
	font = pygame.font.Font("../onodera/ipaexg.ttf", 16)
	while True:
	...
```
まず、メイン関数の先頭の初期化部分でフォント（文字）の設定を行います。16というのはフォントの大きさが16ポイント（文字の大きさの単位）であるということです。
```python
	...
	fail_image = font.render("失敗回数 "+str(failcnt), True, (0, 0, 0))
	SURFACE.blit(fail_image, (0, 0))
	pygame.display.update()
```
`pygame.display.update()`の直前に失敗変数を描画する処理を追加します。
変数名（「失敗回数」）と失敗回数変数`failcnt`を文字列に変換したもの`str()`を文字イメージに変換`render()`し、描画`blit()`します。
`render()`では色も一緒に指定します。
`blit()`では描画位置も一緒に指定します。
ここまでできたら、実行し、失敗回数が表示され、ボールがでたらめに発生し、3回失敗したらプログラムが終了することを確認してください。
## ボールの落ちる速さを変える
スクラッチ同様、落ちる速さを`speed`という変数にします。
クローン毎に別の変数にするため各ボールの変数として作成します。
```python
class Ball(Sprite):
	...
	def __init__(self):
		...
		self.speed = random.randint(-9, -5)
```
ボールの初期化関数`__init__()`の最後に`speed`という変数を追加し、-9から-5まででたらめ（ランダム）な値を設定します。
```python
	else:
		ball.setdy(ball.speed)
```
`setdy()`関数で各ボールのy座標を更新する部分を-5という固定値から`ball.speed`という変数に変更します。
## ボールのクローンを作る間隔を短くする
ゲームを難しくするため、ボールのクローンを作る間隔を0.5秒にします。
```python
			if ballcnt == 15:
				ball = Ball()
```
カウンタ`ballcnt`は1秒に30回更新されるので、1秒に1回から0.5秒に1回にするためには30から15に変更します。
## 点数を数える
点数の変数`score`を作成し、メイン関数`main()`の初期化部分で定義し、ゲーム開始時に0に初期化する。
```python
def main():
	...
	score = 0
	while True:
	...
			if event.key == K_SPACE:
				...
				score = 0
```
コップに触れたとき、点数を1増やす。
```python
			...
			if ball.rect.colliderect(cup.rect):
			...
				score += 1
```
画面の失敗回数の下に表示する
```python
		...
		SURFACE.blit(fail_image, (0, 0))
		score_image = font.render("点数 "+str(score), True, (0, 0, 0))
		SURFACE.blit(score_image, (0, 20))
```
ここまでできたら、実行し、点数が表示され、ボールの速さがでたらめ（ランダム）に変わり、ボールの出現間隔が短くなったことを確認してください。
## 取ってはいけないカミナリを作る
取ると失敗になるカミナリを追加します。
ボールに似ているので、ボールをコピーし、一部を書き換えます。
```python
class Lightning(Sprite):
	_image = pygame.transform.scale_by(pygame.image.load("lightning.svg"), 0.5)
	def __init__(self):
		super().__init__(Lightning._image)
		self.alive = True
		self.speed = -10
```
クラスの名前をBallからLightningに変更し、クラス変数`_image`を参照する部分も`Ball._image`から`Lightning._image`に変更します。
なお、このままの大きさだとカミナリ画像が大きすぎるので`pygame.transform.scale_by()`関数で画像のサイズを半分に変更します。
速度変数の値を固定値(-10)にします。
## コップに触れた時の処理
コップに触れた時の処理は、ボールとカミナリでは異なるので、ボールとカミナリそれぞれに`touch()`という関数を用意して、それぞれ処理を変えるようにします。
### 変数のグローバル化
ボールとカミナリからメイン関数の変数にアクセスできるよう必要な変数をグローバル化します。
```python
def main():
	global succeedsound, failsound, score, failcnt, start, balls
```
### ボールの処理の変更
次にボールがコップに触れた処理をボールの`touch()`関数に移し、ボールがコップに触れた場合、`touch()`関数を呼ぶように変更します。
```python
def Ball(Sprite):
	...
	def touch(self):
		global succeedsound, score
		succeedsound.play()
		self.alive = False
		score += 1
	...
def main():
	...
				if ball.rect.colliderect(cup.rect):
					ball.touch()
```
### カミナリの処理の追加
カミナリがコップに触れた処理をカミナリの`touch()`関数に追加します。
```python
class Lightning(Sprite):
	...
	def touch(self):
		global failsound, failcnt, start, balls
		failsound.play()
		self.alive = False
		failcnt += 1
		if failcnt > 2:
			start = False
			balls.clear()
```
## 落ちた時の処理
落ちた時の処理も、ボールとカミナリでは異なるので、ボールとカミナリそれぞれに`drop()`という関数を用意して、それぞれ処理を変えるようにします。
### ボールの処理の変更
ボールが落ちた処理をボールの`drop()`関数に移し、ボールが落ちた場合、`drop()`関数を呼ぶように変更します。
```python
class Ball(Sprite):
	...
	def drop(self):
		global failsound, failcnt, start, ball
		failsound.play()
		self.alive = False
		failcnt += 1
		if failcnt > 2:
			start = False
			balls.clear()
	...
def main():
	...
				elif ball.gety() < -50:
					ball.drop()
```
### カミナリの処理の追加
カミナリが落ちた処理をカミナリの`drop()`関数に追加します。
```python
class Lightning(Sprite):
	...
	def drop(self):
		self.alive = False
```
### 5秒に1回カミナリを発生させる
0.5秒間隔でボールを発生させる部分を変更し、5秒に1回はカミナリが発生するようにします。
発生カウント`ballcnt`はそのまま使用するので、15になったらボールを発生させて0に戻す処理を以下のように変更します。
```python
			ballcnt += 1
			if ballcnt % 15 == 0:
				ball = Ball()
				ball.setxy(random.randint(-1, 1) * 100, 150)
				balls.append(ball)
```
15になったらではなく、15で割って余りが0ならにして、カウンタ`ballcnt`は増やし続けます。
次に、150（30×5=5秒）で割って余りが0ならボールの代わりにカミナリを発生するように変更します。
```python
			ballcnt += 1
			if ballcnt % 15 == 0:
				if ballcnt % 150 == 0:
					ball = Lightning()
				else:
					ball = Ball()
				ball.setxy(random.randint(-1, 1) * 100, 150)
				balls.append(ball)
```
150で割り切れる値は15でも割り切れるので「`ballcnt`が15で割り切れたら」の処理の中で行っても問題ありません。
以上、できあがったら、実行し、5秒に1回はカミナリが発生し、カミナリに触れると失敗、カミナリをよければ何も起こらないことを確認しましょう。
