# 使用するライブラリを呼び出します
import sys
import pygame
from pygame.locals import *
from random import randint	# ランダムな値を発生させる

# pygameの初期設定を行います
pygame.init()
SURFACE = pygame.display.set_mode((800, 600))	#Windowサイズは800x600ピクセル
pygame.key.set_repeat(15, 15)	# キーを押し続けても一定間隔でイベントを発生させる
FPSCLOCK = pygame.time.Clock()
TICK = 15	#　描画間隔は１秒間に15コマ

RIGHT, LEFT = 0, 1

# メインルーチン
def main():
	# プレイヤー（猫）のイメージファイルを読み込み、５倍(80x80)に拡大する
	image = pygame.image.load("cat.png")
	player_image = pygame.transform.scale(image, (80, 80))
	player_image.set_colorkey((128,128,128))	# 灰色(RGB(128,128,128))を透過色にする
	# プレイヤー（猫）の位置を変数に設定する
	player_x = 375	
	player_y = 225
	# えさのフルーツ（リンゴ）のイメージファイルを読み込み、５倍(80x80)に拡大する
	image = pygame.image.load("apple.png")
	fruit_image = pygame.transform.scale(image, (80, 80))
	fruit_image.set_colorkey((128,128,128))	# 灰色(RGB(128,128,128))を透過色にする
	# えさのフルーツ（リンゴ）を一定間隔で4個、ランダムな高さに出現させる。(x, y, 有効)
	fruits = [[i * 300, randint(0, 520), True] for i in range(4)]
	# 点数を表示するフォント（文字種）と大きさを設定する
	scorefont = pygame.font.Font("ipaexg.ttf", 24)
	# 点数
	score = 0
	# 向き
	direction = LEFT
	# 描画処理
	while True:	# メインループ
		for event in pygame.event.get():	#　各種イベントを取得
			if event.type == QUIT:	# 右上の×ボタンをクリックしたら終了
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:	# キーが押されたら
				if event.key == K_LEFT:	# ←キーなら
					player_x = max(player_x - 10, 0)	# 0以下にはならない
					if direction == RIGHT:
						direction = LEFT
						player_image = pygame.transform.flip(player_image, True, False)
				if event.key == K_RIGHT:	# →キーなら
					player_x = min(player_x + 10, 720)	# 720以上にはならない
					if direction == LEFT:
						direction = RIGHT
						player_image = pygame.transform.flip(player_image, True, False)
				if event.key == K_UP:	# ↑キーなら
					player_y = max(player_y - 10, 0)	# 0以下にはならない
				if event.key == K_DOWN:	# ↓キーなら
					player_y = min(player_y + 10, 520)	# 520以上にはならない				
					
		SURFACE.fill((0, 191, 255))	#　画面全体を淡い青で塗りつぶす
		score_image = scorefont.render("Score {:>4}".format(score), True, (255,255,255))
		SURFACE.blit(score_image, (20,20))
		for fruit in fruits:
			if fruit[2] and fruit[0] < 800:	# フルーツが有効で描画範囲内なら指定の位置に描画する
				SURFACE.blit(fruit_image, (fruit[0], fruit[1]))
		SURFACE.blit(player_image, (player_x, player_y))	# プレイヤー（猫）を描画
		pygame.display.update()	# 画面を更新
		FPSCLOCK.tick(TICK)		# 描画間隔を調整
		for fruit in fruits:
			#　命中判定： フルーツが有効で、フルーツの位置（左上）がプレイヤーの位置(左上）の上下左右±60以内なら
			if fruit[2] and abs(fruit[0] - player_x) < 60 and abs(fruit[1] - player_y) < 60:
				fruit[2] = False	# フルーツを無効（食べた）にする	
				score += 100	# 100点追加
			fruit[0] -= 20	# 各フルーツを左に20移動
			if fruit[0] < -40:	# フルーツが左端を超えそうなら右端奥に移動し、高さはランダムに再設定
				fruit[0] += 1200
				fruit[1] = randint(0, 520)
				fruit[2] = True	# 有効にする
	
if __name__ == '__main__':	# ここからプログラムスタート
	main()	#メインルーチンを呼び出す