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
テキストエディタを使ってmcc1/code/pythonの下にcatchgame.pyというファイルを作成します。
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
## スプライトの骨組みを作る
スクラッチの「スプライト」の仕組みを真似るため、スプライトの骨組みを作成します。
```python
class Sprite:
	def __init__(self, image, x, y):
		self.image = image
		self.x = x
		self.y = y
	def draw(self, surface):
		surface.bilt(self.image, (self.x, self.y))
	def get_rect(self):
		rect = self.image.get_rect()
		rect.left = self.x
		self.top = self.y
		return rect
```
初期化関数`__init__()`では、スプライトの画像と初期の座標値を受取り、スプライトの変数に設定します。
描画関数`draw()`では、スプライトの画像を座標位置に描画します。
触れたかどうか判断するため、スプライトの画像範囲を取得する`get_rect()`関数を用意し、座標位置と画像から画像範囲（矩形）を返します。
## コップを作る
スプライトの骨組みを利用して、コップを作成します。
```python
class Cup(Sprite):
	def __init__(self, x, y):
		super().__init__(pygame.image.load("cup.svg"), x, y)
```
初期化関数でコップの画像ファイル(cup.svg)を`pygame.image.load()`関数に渡して画像に変換し、初期座標値とともに設定します。
## ボールを作る
スプライトの骨組みを利用して、ボールを作成します。
```python
class Ball(Sprite):
	_image = None
	def __init__(self, x, y):
		if Ball._image is None:
			Ball._image = pygame.image.load("ball.svg")
		super().__init__(Ball._image, x, y)
		self.alive = True
		self.speed = random.randint(5, 15)
		self.lightning = False
	def update(self)
		self.y += self.speed
```
コップと異なり、ボールはクローンを何個も作成するため、毎回画像ファイルを画像に変換するのは無駄なので`_image`という変数に画像を設定し、画像を使いまわすようにしています。
また、ボールは削除されるので、有効か否かを判定する`alive`変数を用意し、Trueに
設定しておきます。
さらに`speed`という変数に速度（ここではランダム値）を設定します。
`lightning`変数はこのあと作成する「カミナリ」と「ボール」を区別するためのものです。「ボール」は「カミナリ」ではないのでFalseにしておきます。
最後に、`update()`関数で速度変数で座標位置を更新します。
## 取ってはいけないカミナリを作る
取ると失敗になるカミナリを追加します。
ボールに似ているので、ボールをコピーし、一部を書き換えます。
```python
class Lightning(Sprite):
	_image = None
	def __init__(self, x, y):
		if Lightning._image is None:
			image = pygame.image.load("lightning.svg")
			Lightning._image = pygame.transform.scale_by(image, 0.5)
		super().__init__(Lightning._image, x, y)
		self.alive = True
		self.speed = 15
		self.lightning = True
	def update(self)
		self.y += self.speed
```
クラスの名前をBallからLightningに変更し、クラス変数`_image`を参照する部分も`Ball._image`から`Lightning._image`に変更します。
なお、このままの大きさだとカミナリ画像が大きすぎるので`pygame.transform.scale_by()`関数で画像のサイズを半分に変更します。
速度変数の値を固定値(15)にし、「カミナリ」なので`lightning`変数をTrueにします。
## ゲームの初期化
ゲームの初期化を行います。
```python
pygame.init()
SURFACE = pygame.display.set_mode((400, 400))
FPSCLOCK = pygame.time.Clock()
```
pygameの初期化を行い、画面の大きさを400×400に設定し、画面の書き換えを管理する変数`FPSCLOCK`を取得します。
## ゲームのメイン関数
ゲーム本体のメイン関数を作成します。
### 各種変数の初期化
まず最初にゲームで使用する変数を初期化します。
```python
def main():
	failCnt = 0
	balls = []
	cup = None
	TIMECNT = 0
	score = 0
	scorefont = pygame.font.SysFont(None, 36)
```
`failcnt`は失敗した回数で0に初期化され、3回失敗するとゲームが終了します。
`balls`はボールやカミナリなど複数のスプライトをまとめて管理するリストで初期値は空です。
`cup`はコップで、`None`に初期化しておきます。
`TIMECNT`は時間のカウンタで0に初期化し、ボールやカミナリの出現タイミングに使用します。
### メインルーチン
ずっと処理を続ける処理
```python
	while True:
```
### イベントを処理する部分
キーボード入力などのイベントを処理します。
#### 終了イベントの処理
```python
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
```
ウィンドウの右上の☓マークを押したら、QUITというイベントが発生するので、pygameを終了し、プログラムを終了します。
#### スペースキーイベントの処理
```python
			elif event.type == KEYDOWN:
				if event.key == K_SPACE:
					cup = Cup(150, 200)
					balls.clear()
					failCnt = 0 
```
スペースキーを押したら、ゲームが始まるのでカップ(cup)を初期座標で初期化し、ボールリストを空にし、失敗カウントも初期化します。
#### jキーイベントの処理
```python
				elif cup is not None:
					if event.key == K_j:
						if cup.x < 200:
							cup.x += 100
```
cup変数がNoneのときはゲームが始まっていないので、cup変数がNoneでないときだけ処理を行います。
jキーが押されたら、カップが右端でなければ、座標値を100足します。
#### fキーイベントの処理
```python
					elif event.key == K_f:
						if cup.x > 100:
							cup.x -= 100
```
fキーが押されたら、カップが左端でなければ、座標値を100引きます。
### 時間の処理
```python
		FPSCLOCK.tick(10)
		TIMECNT += 1
		if cup is not None:
			if TIMECNT % 100 == 0:
				lightning = Lightning(random.randint(1,3)*100-35, 50)
				balls.append(lightning)
			elif TIMECNT % 20 == 0:
				ball = Ball(random.randint(1,3)*100-35, 50)
				balls.append(ball)		
```
`FPSCLOCK.tick(10)`で0.1秒ごとにメインループを繰り返すようにします。
TIMECNT変数を0.1秒毎に更新し、10秒に１回、カミナリを発生、2秒に１回、ボールを発生するようにします。
### ボール（またはカミナリ）がカップに触れた処理
```python
		for ball in balls:
			if ball.get_rect().colliderect(cup.get_rect()):
				if ball.lightning:
					pygame.mixer.Sound("failed.wav").play()
					failCnt += 1
				else:
					pygame.mixer.Sound("succeed.wav").play()
					score += 1
				ball.alive = False
```
ボールリストからボール（またはカミナリ）を１つずつ取り出し、その矩形範囲とカップの矩形範囲が重なっているか否かでカップに触れたか否かを判定し、触れていたら、カミナリなら失敗処理（失敗音と失敗カウントの更新）、ボールなら成功処理（成功音と得点の更新）を行い、そのボール（またはカミナリ）を無効にする。
### ボール（またはカミナリ）が下まで落ちた処理
```python
			if ball.y > 170:
				if not ball.lightning:
					pygame.mixer.Sound("failed.wav").play()
					failCnt += 1
				ball.alive = False
```
ボール（またはカミナリ）が下まで落ちたら、ボールならば（カミナリでなければ）、失敗処理（失敗音と失敗カウントの更新）をし、ボール（またはカミナリ）を無効にする。
### 3回失敗したらゲームオーバー
```python
			if failCnt > 2:
				pygame.quit()
				sys.exit()
```
失敗回数が3回（2より大きく）になったら、pygameを終了し、プログラムを終了する
### ボール（またはカミナリ）の位置の更新
```python
			if ball.alive:
				ball.update()
```
ボール（またはカミナリ）が有効なら位置を更新する
### 無効なボール（またはカミナリ）の削除
```python
		balls = [ball for ball in balls if ball.alive]
```
ボールリストの中のボール（またはカミナリ）のうち有効なもののみ残す
### 描画処理
画面をクリアし、カップとボール（またはカミナリ）を描画し、スコアを描画して、画面を再描画します。
```python
		SURFACE.fill((255, 255, 255))
		if cup is not None:
			cup.draw(SURFACE)
		for ball in balls:
			ball.draw(SURFACE)
		score_image = scorefont.render(str(score), True, (0, 255, 0))
		SURFACE.blit(score_image, (350, 0))
		pygame.display.update()
```
### メイン関数の呼び出し
```
if __name__ == "__main__":
	main()
```
最後にメイン関数を呼び出します。
以上のコードは、`mcc1/code/python/CatchGame/`の下に`catchgame.py`という名前で作成されています。また必要な画像ファイル、音声ファイルも格納されています。
```
python3 catchgame.py
```
で遊ぶことができます。

