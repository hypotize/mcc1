import pygame
import sys
from pygame.locals import *
import random
import math
import datetime

# いろをいくつか定義
colors = ((0, 0, 0),       #黒
          (255, 0, 0),     #赤
          (0, 255, 0),     #みどり
          (0, 0, 255),     #青
          (255, 255, 255)  #白
          )

#最初のペンキのいろ
color = 0

#一個の箱の大きさ(ピクセル)
block_size = 20
#箱の数(一辺) 
matrix_size = 30

# 最初は全部白にする (白は4)
mtrx =  [[4] * matrix_size for i in range(matrix_size)]

# 箱を全部書いていく
def draw():
    for i in range(matrix_size):
        for j in range(matrix_size):
            val = mtrx[j][i]
            pygame.draw.rect(screen,colors[val],[i * block_size, j * block_size, block_size,block_size], 0)

pygame.init()
screen = pygame.display.set_mode([block_size * matrix_size, block_size * matrix_size])
pygame.display.set_caption("Miura Paint")
 
done = False
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:

    #イベント処理
    had_event = False
    for event in pygame.event.get():
        had_event = True

        #画面を閉じるボタン
        if event.type == QUIT:
            pygame.quit()
        
        #キーが押されたとき
        if event.type == KEYDOWN:
            #終了
            if event.key == K_q or event.key == K_ESCAPE:
                pygame.quit()
            #色の切り替え 1 ~ 5 までのの色
            if event.key == K_1:
                color = 0
            if event.key == K_2:
                color = 1
            if event.key == K_3:
                color = 2
            if event.key == K_4:
                color = 3
            if event.key == K_5:
                color = 4
            # s で保存
            if event.key == K_s:
                dt = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = "screenshot_" + dt + ".jpg"
                pygame.image.save(screen ,filename)
                print(filename, "で保存しました。") 

        #クリックで描く
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = math.floor(pos[0] / block_size)
            row = math.floor(pos[1] / block_size)
            mtrx[row][col] = color

        #マウスののボタンを押した状態でマウスを動かして、描く
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]: 
                pos = pygame.mouse.get_pos()
                col = math.floor(pos[0] / block_size)
                row = math.floor(pos[1] / block_size)
                mtrx[row][col] = color
            
    draw()
    pygame.display.flip()
    clock.tick(20) 
pygame.quit()
