import sys        # プログラムを終了する関数sys.exit()を使用する
import pygame    # Pygameを使用する
from pygame.locals import QUIT    # ウィンドウを閉じた時のコード

# 最初に1度だけ実行される部分
pygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((600, 400))    # 600x400のウィンドウを作成し、SURFACE変数に設定
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数

def main():    # メイン関数
     # 必要ならこの部分にも1度だけ実行される部分を記載する
    while True:    # ずっと
        for event in pygame.event.get():
            if event.type == QUIT:    # ウィンドウを閉じたらプログラムを終了する
                pygame.quit()
                sys.exit()

          # フレームを表示するたびに実行される部分
        SURFACE.fill((255, 255, 255))    # 背景を白で描画（クリア）する
          # ここで図形を描画する

        pygame.display.update()    # ウィンドウを更新
        FPSCLOCK.tick(3)    # １秒に3回フレームを更新する

if __name__ == '__main__':    # メイン関数を呼ぶ
    main()
