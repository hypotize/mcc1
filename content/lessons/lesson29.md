+++
title = "レッスン 29"
date = "2024-02-05T10:00:00+09:00"
author = "小野寺 健"
description = "カーレースゲームを改造しよう" 
showFullContent = false
readingTime = false
tags = ["python", "ゲーム", "pygame", "中級"]
+++
# レッスンの目標
カーレースゲームを改造しよう
## ファイルをコピーする
コマンドラインから以下のコマンドでフォルダを移動し、ファイルを`carrace6.py`にコピーします。
```
cd mcc1/code/python/onodera
cp carrace5.py carrace6.py
```
## carrace6.pyの書き換え
`carrace6.py`を書き換えることで、カーレースゲームを改造します。
### ペダルの追加
アクセルを↑キーからペダルに変更します。
ペダルは踏むと「b」というキーを入力するという仕様になっているので、
`K_UP`の部分を`K_b`に書き換えます。
まず、3行目を書き換えます。
* 変更前
```python
from pygame.locals import QUIT, Rect, KEYDOWN, KEYUP, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE
```
* 変更後
```python
from pygame.locals import QUIT, Rect, KEYDOWN, KEYUP, K_b, K_DOWN, K_LEFT, K_RIGHT, K_SPACE
```
次に289行目以降を書き換えます。
* 変更前
```python
				elif event.type == KEYDOWN:
					if event.key == K_UP:
						is_speed_up = True
					elif event.key == K_DOWN:
						is_speed_down = True
					elif event.key == K_LEFT:
						move_x = -10
					elif event.key == K_RIGHT:
						move_x = 10
					elif event.key == K_SPACE:
						self.restart = True
				elif event.type == KEYUP:
					if event.key == K_UP:
						is_speed_up = False
					elif event.key == K_DOWN:
						is_speed_down = False
					elif event.key == K_LEFT or event.key == K_RIGHT:
						move_x = 0
```
* 変更後
```python
				elif event.type == KEYDOWN:
					if event.key == K_b:
						is_speed_up = True
					elif event.key == K_DOWN:
						is_speed_down = True
					elif event.key == K_LEFT:
						move_x = -10
					elif event.key == K_RIGHT:
						move_x = 10
					elif event.key == K_SPACE:
						self.restart = True
				elif event.type == KEYUP:
					if event.key == K_b:
						is_speed_up = False
					elif event.key == K_DOWN:
						is_speed_down = False
					elif event.key == K_LEFT or event.key == K_RIGHT:
						move_x = 0
```
### プレイ時間の変更
プレイ時間は５分（注：実際の時間ではありません）に設定されていますが、この時間を変更してみましょう。
47行目から
```python
class GameState(State, Singleton):
	def __init__(self, init):
		if init:
			self.time = Time(0, 5, 0)	# <-- 時,分,秒　ここを変更
			self.distance = Distance(0)
```
### 効果音を入れる
各ステージ（状態）毎に効果音を入れてみましょう。
各ステージの音については、自分の好きな音に設定して構いません。
#### 前準備
各ステージの開始、終了を明確にするため、開始関数`start()`、終了関数`end()`を追加します。
```python
class State:
	def draw(self):
		pass
	def update(self, context):
		pass
	def start(self);
		pass
	def end(self):
		pass
```
ステージの切り替え時に、前のステージの終了関数と次のステージの開始関数を呼ぶように処理を追加します。
また、`state`変数を`None`に初期化し、InitState()に切り替えるように変更します。
```python
class Game(Context):
	def __init__(self):
		self.rocks = []
		self.trees = []
		self.state = None
		self.changeState(InitState())
		self.road = Road(100, (224, 224, 224))
		
	def changeState(self, state):
		if self.state is not None:
			self.state.end()
		self.state = state
		self.state.start()
```
これで各ステージ（状態）の開始時には`start()`、終了時には`end()`が呼ばれるようになります。
#### ゲーム開始時のカウントダウン
ゲーム開始時にカウントダウンの音を追加します。
```python
class InitState(State, Singleton):
	def __init__(self):
		self.count_down = 39
		self.sound = pygame.mixer.Sound("制限時間4.mp3")

	def start(self):
		self.sound.play()
```
`InitState`はゲーム開始ステージ（状態）なので、このステージの初期化関数`__init__()`で変数`sound`にカウントダウン音(制限時間4.mp3)を設定します。
このステージに開始関数`start()`を追加して、`play()`を実行するようにします。
また、カウントダウンの音声時間は4秒なので、カウントダウン時間もこれにあわせます。
#### ゲーム実行中のBGM
ゲーム実行中のBGMを追加します。
```python
class GameState(State, Singleton):
	def __init__(self, init):
		if init:
			self.time = Time(0, 10, 0)
			self.distance = Distance(0)
			if not hasattr(self, "sound"):
				self.sound = pygame.mixer.Sound("Fusion_02.mp3")
				
	def start(self):
			self.sound.play(loops=-1)
			
	def end(self):
		self.sound.stop()	
```
`GameState`はゲーム実行中ステージ（状態）なので、このステージの初期化関数`__init__()`で変数`sound`が存在しなければ、BGM音(Fusion_02.mp3)を`sound`変数に設定します。
このステージに開始関数`start()`を追加し、`play(loops=-1)`にして無限にBGMを繰り返し演奏するようにします。
ゲーム実行が終了したらBGMを止めるために、このステージに終了関数`end()`を追加し、`stop()`を実行して、BGMを止めます。
#### 衝突時の爆発音
他の車に衝突した場合の爆発音を追加します。
```python
class ExplosionState(State, Singleton):
	def __init__(self):
		self.count_down = 49
		self.sound = pygame.mixer.Sound("爆発.mp3")
		
	def start(self):
		self.sound.play()
```
`ExplosionState`は衝突ステージ（状態）なので、このステージの初期化関数`__init__()`で変数`sound`に爆発音(爆発.mp3)を設定します。
このステージに開始関数`start()`を追加し、`play()`を実行するようにします。
#### ゲームオーバー時のエンディング音楽
ゲームオーバーになった際にエンディングを音楽を追加します。
```python
class GameOverState(State, Singleton):
	def __init__(self):
		self.sound = pygame.mixer.Sound("jingle_11.mp3")
	
	def start(self):
		self.sound.play()
```
`GameOverState`はゲームオーバーステージ（状態）なので、このステージの初期化関数`__init__()`を追加し、変数`sound`にエンディング音(jingle_11.mp3)を設定します。
このステージに開始関数`start()`を追加し、`play()`を実行するようにします。
#### アクセルを踏んだ時のエンジン音
アクセルを踏んだ時にエンジン音がするようにします。
```python
class State:
...
	def accel(self, speed_up):
		pass
```
各ステージに`accel()`という関数を追加します。引数にアクセルがONかOFFかを設定するようにします。追加しましたが、このままではこの関数は何もしません。
```python
class GameState(State, Singleton):
	def __init__(self, init):
		if init:
			self.time = Time(0, 10, 0)
			self.distance = Distance(0)
			if not hasattr(self, "sound"):
				self.sound = pygame.mixer.Sound("Fusion_02.mp3")
			if not hasattr(self, "accelSound")
				self.sound = pygame.mixer.Sound("バイク通行音2.mp3")
...				
	def end(self):
		self.sound.stop()
		self.accelSound.stop()
...
	def accel(self, speed_up):
		if speed_up:
			self.accelSound.play()
		else:
			self.accelSound.stop()
```
エンジン音がするのはゲーム中だけなので、ゲーム中ステージ（状態）の`GameState`だけに`accel()`関数を追加します。
初期化関数`__init__()`で`sound`変数同様に`accelSound`変数にアクセル音の設定を行い、`accel()`関数でアクセル音を発したり止めたりします。
また、ゲーム中でなくなってもアクセル音がし続けないように`end()`関数でもアクセル音を止めます。
```python
class Game(Context):
	...
	def play(self):
		...
		while True:
			...
			for event in pygame.event.get():
				...
			self.state.accel(is_speed_up)
			velocity += 1 if is_speed_up else -2 if is_speed_down else -1
			...
```
ゲームの`play()`関数の中でアクセルキー（ペダルまたは↑）がふまれた時に`True`になり、離した時に`False`になる`is_speed_up`という変数を引数として、イベント処理後に`accel()`関数を呼びます。
### 競争相手の車の種類を増やす
競争相手の車の種類を増やし、ランダムに選ばれるようにしましょう。
```python
class Rock:
	images = [pygame.image.load("./png/toyota86.png")]
	def __init__(self, speed)
		self.x = random.randint(354, 446) 
		self.y = 200
		self.size = 7
		self.ratex = 1
		self.ratey = 0.6
		self.speed = speed
		self.image = random.choice(Rock.images)
...
	def draw(self, debug=False):
		if self.y >= 200:
			rect = self.getRect()
			image = pygame.transform.scale(self.image, rect.size)
			SURFACE.blit(image, rect.topleft)
```
競争相手の車の画像を複数設定できるよう、変数`images`をリスト（配列）にします。今は１画像だけですが、`images = [pygame.image.load("./png/toyota86.png"), pygame.image.load("./png/XXX.png")]`のように画像を追加することで、複数の画像を設定することができます。自分の好きな車種を追加しましょう。
`random.choice()`関数で複数のリストの中からランダムに選んで`image`変数に設定し、`draw()`関数で`image`変数に設定された画像が表示されます。
## 背景を追加する
臨場感を出すため、背景画像を追加してみましょう。
### 背景画像の読み込み
```python
class Game(Context):
	def __init__(self):
		...
		self.background = pygame.transform.scale(pygame.image.load("./background.png"), (800, 600))
```
ゲームの初期化関数`__init__()`の最後で背景イメージ`background.png`を読み込み、`background`という変数に設定します。
`pygame.transform.scale()`という関数で画像のサイズを画面のサイズにあわせて変形していますが、画像の縦横比が8:6でない場合は、横を800にした時に縦横比が元の画像の縦横比と同じになるよう、縦の値600を変更してください。
### 背景画像の描画
元のプログラムでは、ゲームの`play()`関数の後ろの方で、まず全体の背景を`SURFACE.fill(0, 255, 0)`で緑色にして、その後`pygame.draw.rect(SURFACE, (0, 255, 255), (0, 0, 800, 200))`で画面の上の部分を空色（シアン）で四角く塗っています。
この部分を背景画像の描画に置き換えます。
```python
class Game(Context):
	...
	def play(self):
		...
		SURFACE.fill(0, 30, 67)
		SURFACE.blit(self.background, (0, 0), (0, 0, 800, 200))
```
これで空の部分が背景画像の上の部分に置き換わります。
`(0, 0, 800, 200)`の２番目の値を変えると、背景の表示される部分を変えることもできます。
また、今回の背景画像は夜の街なので、緑色の全体背景は合いません。そこで全体背景をミッドナイトブルー（真夜中の青）である`(0, 30, 67)`に書き換えています。
### 速度や距離の表示色を変える
背景画像が暗いので、速度や距離を表示している青色は見にくくなってしまいました。
そこで、速度や距離の表示色を白に変更します。
```python
class GameState(State, Singleton):
	...
	def draw(self):
		...
		speed_image = SPEEDFONT.render("{:3d} Km/h".format(speed), True, (255, 255, 255))
	...
class Distance:
	...
	def draw(self):
		image = SYSFONT.render("max: {:08.2f} km".format(max_count/250), True, (255, 255, 225))
		SURFACE.blit(image, (570,20))
		image = SYSFONT.render("{:08.2f} km".format(self.distance/250), True, (255, 255, 225))
		SURFACE.blit(image, (330,20))	
```
青色(0, 0, 255)だった部分を白色(255, 255, 255)に全て変更します。	
自分の好きな背景に変更し、背景に合わせて文字色も変えてみましょう。

