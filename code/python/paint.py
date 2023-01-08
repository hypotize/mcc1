import pygame
import sys
from pygame.locals import *
import random
import math
import datetime

# Define some colors
colors = ((0, 0, 0),       #black
          (255, 0, 0),     #red
          (0, 255, 0),     #green
          (0, 0, 255),     #blue
          (255, 255, 255)  #white
          )

#initial color
color = 0

block_size = 20
matrix_size = 30

# intial matrix is all white 
mtrx =  [[4] * matrix_size for i in range(matrix_size)]

def draw():
    for i in range(matrix_size):
        for j in range(matrix_size):
            val = mtrx[j][i]
            pygame.draw.rect(screen,colors[val],[i * block_size, j * block_size, block_size,block_size], 0)

pygame.init()
 
# Set the height and width of the screen
screen = pygame.display.set_mode([block_size * matrix_size, block_size * matrix_size])
pygame.display.set_caption("Draw")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
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
            if event.key == K_q or event.key == K_ESCAPE:
                pygame.quit()
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
            if event.key == K_s:
                dt = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
                filename = "screenshot_" + dt + ".jpg"
                pygame.image.save(screen ,filename)
                print("saved to", filename) 

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = math.floor(pos[0] / block_size)
            row = math.floor(pos[1] / block_size)
            mtrx[row][col] = color

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
