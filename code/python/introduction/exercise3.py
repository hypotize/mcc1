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
	fruit_image = pygame.image.load("apple.png")
	fruit_image.set_colorkey((128,128,128))	# 灰色(RGB(128,128,128))を透過色にする
	# えさのフルーツ（リンゴ）を一定間隔で4個、ランダムな高さに出現させる。(x, y, 有効)
	fruits = [[i * 300, randint(0, 520), True, randint(40, 160)] for i in range(4)]
	# 点数を表示するフォント（文字種）と大きさを設定する
	scorefont = pygame.font.Font("ipaexg.ttf", 24)
	# 点数
	score = 0
	# 描画処理
	while True:	# メインループ
		for event in pygame.event.get():	#　各種イベントを取得
			if event.type == QUIT:	# 右上の×ボタンをクリックしたら終了
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:	# キーが押されたら
				if event.key == K_LEFT:	# ←キーなら
					player_x = max(player_x - 10, 0)	# 0以下にはならない
				if event.key == K_RIGHT:	# →キーなら
					player_x = min(player_x + 10, 720)	# 720以上にはならない
				if event.key == K_UP:	# ↑キーなら
					player_y = max(player_y - 10, 0)	# 0以下にはならない
				if event.key == K_DOWN:	# ↓キーなら
					player_y = min(player_y + 10, 520)	# 520以上にはならない				
					
		SURFACE.fill((0, 191, 255))	#　画面全体を淡い青で塗りつぶす
		score_image = scorefont.render("Score {:>4}".format(score), True, (255,255,255))
		SURFACE.blit(score_image, (20,20))
		for fruit in fruits:
			if fruit[2] and fruit[0] < 800:	# フルーツが有効で描画範囲内なら指定の位置に描画する
				image = pygame.transform.scale(fruit_image, (fruit[3], fruit[3]))
				SURFACE.blit(image, (fruit[0], fruit[1]))
		SURFACE.blit(player_image, (player_x, player_y))	# プレイヤー（猫）を描画
		pygame.display.update()	# 画面を更新
		FPSCLOCK.tick(TICK)		# 描画間隔を調整
		for fruit in fruits:
			#　命中判定： フルーツが有効で、フルーツとプレイヤーが10以上重なっていたら
			if fruit[2] and fruit[0]+10 < player_x+70 and player_x+10 < fruit[0]+fruit[3]-10 and \
				fruit[1]+10 < player_y+70 and player_y+10 < fruit[1]+fruit[3]-10:
				fruit[2] = False	# フルーツを無効（食べた）にする	
				score += 100 * 80 // fruit[3]	# 100点/大きさ（倍率）追加
			fruit[0] -= 20	# 各フルーツを左に20移動
			if fruit[0] < -40:	# フルーツが左端を超えそうなら右端奥に移動し、高さはランダムに再設定
				fruit[0] += 1200
				fruit[1] = randint(0, 520)
				fruit[2] = True	# 有効にする
				fruit[3] = randint(40, 160)
	
if __name__ == '__main__':	# ここからプログラムスタート
	main()	#メインルーチンを呼び出す