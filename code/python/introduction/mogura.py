# 使用するライブラリを呼び出します
import sys
import pygame
from pygame.locals import *
from random import randint
import math

# pygameの初期設定を行います
pygame.init()
SURFACE = pygame.display.set_mode((800, 600))	#Windowサイズは800x600ピクセル
FPSCLOCK = pygame.time.Clock()
TICK = 15	#　描画間隔は１秒間に15コマ
MAX_H = TICK*6	# 隠れている時間の最大値(6秒)
MAX_E = TICK*2	# 外に出ている時間の最大値(2秒)

class Mogura:	# もぐらのクラス
	img = [None]*3	# 状態ごとの画像
	size = 0		# サイズ
	HIDDEN = 0		# 隠れている状態
	EXPOSE = 1		# 外に出ている状態
	HIT	= 2			# 命中した状態
	def setImage(file, status, size):	# 状態ごとの画像を設定する（クラス関数）
		image = pygame.image.load(file)
		image = pygame.transform.scale(image, (size, size))
		image.set_colorkey((128,128,128))
		Mogura.img[status] = image
		Mogura.size = size
	def __init__(self, x, y):			# 描画位置を指定して初期化する
		self.rect = Rect(x, y, Mogura.size, Mogura.size)
		self.status = 0
		self.setTimer()
	def setTimer(self, timer=None):		# 次の状態に変化する時間を設定
		if timer is None:
			self.timer = randint(1, MAX_H)	# デフォルト値は1～MAX_Hの間でランダム
		else:
			self.timer = timer
	def draw(self):	# 描画する
		SURFACE.blit(Mogura.img[self.status], self.rect.topleft)
	def collidepoint(self, pos):	# 命中の判定
		return self.status == Mogura.EXPOSE and self.rect.collidepoint(pos)

# メインルーチン
def main():
	global hummer_img, scorefont, sysfont
	pygame.mouse.set_visible(False)
	image = pygame.image.load("hummer.png")	# マウスの画像（ハンマー）を設定
	image = pygame.transform.scale(image, (100, 100))
	image.set_colorkey((128,128,128))
	hummer_img = image
	Mogura.setImage("moguri.png", Mogura.HIDDEN, 100)	# 隠れているモグラ画像を設定
	Mogura.setImage("mogura.png", Mogura.EXPOSE, 100)	# 外に出ているモグラ画像を設定
	Mogura.setImage("hit.png", Mogura.HIT, 100)			# 命中したモグラ画像を設定
	scorefont = pygame.font.Font("ipaexg.ttf", 24)
	sysfont = pygame.font.Font("ipaexg.ttf", 48)
	pygame.mixer.music.load("hummer.mp3")	# 効果音（ピコピコハンマー）
	while True:	# Game Over後再開したら再び実行
		play()	

# ゲーム開始	
def play():	
	global hummer_img, scorefont, sysfont
	mogura_list = [Mogura(150, 70), Mogura(350, 70), Mogura(550, 70),
		Mogura(250, 190), Mogura(450, 190),
		Mogura(150, 310), Mogura(350, 310), Mogura(550, 310),
		Mogura(250, 430), Mogura(450, 430)]
	score = 0	# 初期スコア
	game_over = False
	timer = 31*TICK-1	# ゲーム時間は31秒間
	hummer_pos = None
	# 描画処理
	while True:	# メインループ
		for event in pygame.event.get():	#　各種イベントを取得
			if event.type == QUIT:	# 右上の×ボタンをクリックしたら終了
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if game_over and event.key == K_RETURN:	# Game OverのときEnter keyを押したら再開する
					return
			if not game_over and event.type == pygame.MOUSEBUTTONDOWN:	# クリックしたら命中したか判定
				pos = pygame.mouse.get_pos()
				for mogura in mogura_list:
					if mogura.collidepoint(pos):	# 外に出ているモグラに命中したら
						mogura.status = Mogura.HIT	# 命中状態にして
						mogura.setTimer(TICK)		# 1秒間表示させる
						pygame.mixer.music.play()	# 効果音を出す
						score += 1
			if event.type == pygame.MOUSEMOTION:	# マウスの動きに合わせてハンマーが動く
				hummer_pos = pygame.mouse.get_pos()
		SURFACE.fill((0, 255, 0))	#　画面全体を緑で塗りつぶす
		score_image = scorefont.render("Score {:>4}".format(score), True, (255,255,255))
		SURFACE.blit(score_image, (20,20))	# スコアを描画
		timer_image = scorefont.render("Time {:>4}".format(math.ceil(timer//TICK)), True, (255,255,255))
		SURFACE.blit(timer_image, (680,20))	# 時間を描画
		for mogura in mogura_list:
			mogura.draw()	# もぐらを描画
		if game_over:	# ゲームオーバーならGeme Overを表示
			game_image = sysfont.render("Game Over!", True, (255, 0, 0))
			SURFACE.blit(game_image, (300, 180))
			game_image = sysfont.render("Retry: Press Enter Key", True, (255, 0, 0))
			SURFACE.blit(game_image, (200, 300))
		if hummer_pos is not None:	# ハンマーを描画
			SURFACE.blit(hummer_img, (hummer_pos[0]-50,hummer_pos[1]-50))
		pygame.display.update()	# 画面を更新
		FPSCLOCK.tick(TICK)		# 描画間隔を調整
		if timer == 0:	# 時間が0になったらゲームオーバー
			game_over = True
		else:
			timer -= 1	# 時間を更新
			for mogura in mogura_list:	# もぐらの状態を更新
				mogura.timer -= 1	# 状態変更時間を更新
				if mogura.timer == 0:	# 状態変更時間がきたら
					if mogura.status == Mogura.HIDDEN:	# もぐらが隠れていたら
						mogura.status = Mogura.EXPOSE	# 外に出す
						mogura.setTimer(randint(1, MAX_E))	# 外に出ている時間を1～MAX_E間でランダムに設定
					else:	# 外に出ているか、命中した状態なら
						mogura.status = Mogura.HIDDEN	# もぐらを隠し
						mogura.setTimer()				# 時間をランダムに初期化
				
if __name__ == '__main__':	# ここからプログラムスタート
	main()	#メインルーチンを呼び出す