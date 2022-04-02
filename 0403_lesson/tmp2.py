### インポート
import math
import pygame
from pygame.locals import *
 
### 定数
WIDTH   = 400       # 幅
HEIGHT  = 400       # 高さ
RADIUS  = 180       # 半径
CENTER  = int(WIDTH/2),int(HEIGHT/2)
 
### モジュール初期化
pygame.init()
 
### 時間オブジェクト生成
clock = pygame.time.Clock()
 
### 画面設定
surface = pygame.display.set_mode((WIDTH,HEIGHT))
 
### 初期角度
angle = 0
 
### 無限ループ
while True:
 
    ### 画面初期化
    surface.fill((0,0,0))
 
    ### 円表示
    pygame.draw.circle(surface, (255,0,0), (CENTER), RADIUS, 2)
 
    ### 線の終端位置
    pos_x = round(math.cos(math.radians(angle))*RADIUS)
    pos_y = round(math.sin(math.radians(angle))*RADIUS)
 
    ### 線表示
    pygame.draw.line(surface, (255,255,255), (CENTER), (CENTER[0]+pos_x,CENTER[1]-pos_y), 2)
 
    ### 画面更新
    pygame.display.update()
 
    ### フレームレート設定
    clock.tick(50)
 
    ### 角度計算
    if angle > 359:
        angle  = 0
    else:
        angle += 1
 
    ### イベント処理
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            break
    else:
        continue
 
    ### whileループ終了
    break
 
### 終了処理
pygame.quit()
