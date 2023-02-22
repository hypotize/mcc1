# 使用するライブラリを呼び出します
import sys
import pygame
from pygame.locals import *

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
					
		SURFACE.fill((0, 0, 0))	#　画面全体を黒で塗りつぶす
		SURFACE.blit(player_image, (player_x, player_y))	# プレイヤー（猫）を描画
		pygame.display.update()	# 画面を更新
		FPSCLOCK.tick(TICK)		# 描画間隔を調整
	
if __name__ == '__main__':	# ここからプログラムスタート
	main()	#メインルーチンを呼び出す