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
	player_image.set_colorkey((128,128,128))	# 灰色(RGB(128,128,128))を透過色にする
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