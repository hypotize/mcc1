#　Ping Pong game Step 2  - Add Paddle 
# Michael Cashen 
# Builds on Tom's Pong 
# https://github.com/cprn/pong/blob/master/pong.py
#
# Released under the GNU General Public License

import sys
import math
import os
import pygame
from pygame.locals import *

# 画像のロード
def load_png(name):
    try:
        image = pygame.image.load(name)
    except pygame.error as message:
        print('Cannot load image:', fullname)
        raise SystemExit(message)
    return image, image.get_rect()


# ボール　クラスの定義
class Ball(pygame.sprite.Sprite):


    #初期化
    def __init__(self, startpos, vector):
        pygame.sprite.Sprite.__init__(self)

        self.image, self.rect = load_png('ball.png')

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.vector = vector
        self.rect.center = startpos

    #更新
    def update(self):
        
        #　角度とスピードからx軸と y軸の移動距離を計算
        # https://hakuhin.jp/as/math.html 
        (angle,speed) = self.vector
        x_change = speed * math.cos(angle)
        y_change = speed * math.sin(angle)
        newpos = self.rect.move(x_change,y_change)
        self.rect = newpos

        # ボールの一部でもエリアの外行った場合の処理
        if not self.area.contains(newpos):

            #左上が外ならTrue
            tl = not self.area.collidepoint(newpos.topleft)

            #右上が外ならTrue
            tr = not self.area.collidepoint(newpos.topright)

            #左下が外ならTrue
            bl = not self.area.collidepoint(newpos.bottomleft)

            #右下が外ならTrue
            br = not self.area.collidepoint(newpos.bottomright)

            #上の辺
            if tr and tl:
                print("hit top wall")
                new_angle = -angle 

            #下の辺
            if br and bl:
                print("hit bottom wall")
                new_angle = -angle 

            #左の辺
            if tl and bl:
                print("hit left wall")
                new_angle = math.pi - angle

            #右の辺
            if tr and br:
                print("hit right wall")
                new_angle = math.pi - angle
                
            if new_angle <  0: 
               new_angle  = new_angle + math.pi * 2  


            print(angle, " => ", new_angle)
            self.vector = (new_angle,speed)

# パドル　クラスの定義
class Paddle(pygame.sprite.Sprite):

    #初期化
    def __init__(self, startpos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('paddle.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.center = startpos
        
    def update(self):
        mousepos = pygame.mouse.get_pos()
        self.rect.midtop = (mousepos[0], 300)    
    


def main():

    # 画面の初期化
    pygame.init()
    screen = pygame.display.set_mode((480, 360))
    pygame.display.set_caption('ピンポンゲーム ステップ2')

    # 背景
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255,255))


    # ボール初期化
    # (初期x座標,初期y座標), (初期角度ラジアン, 速度)
    ball = Ball((240,100),(math.pi * 1.75,6))

    # パドル初期化
    paddle = Paddle((10,300))

    # 描く
    ballsprite = pygame.sprite.RenderPlain(ball)
    paddlesprite = pygame.sprite.RenderPlain(paddle)

    # 画面に出す
    screen.blit(background, (0, 0))

    # 動きを管理するClockを初期化
    clock = pygame.time.Clock()

    # ずっと処理
    while 1:

        # 一秒に最大60回処理
        clock.tick(60)

        #イベント処理
        for event in pygame.event.get():

            #画面を閉じるボタン
            if event.type == QUIT:
                return

            #キーが押されたとき
            if event.type == KEYDOWN:
                if event.key == K_q or event.key == K_ESCAPE:
                    return

        #ボールとパドルがあった場所に背景をもう一回描く
        screen.blit(background, ball.rect, ball.rect)
        screen.blit(background, paddle.rect, paddle.rect)


        #ボールとパドルのアップデート処理(位置計算)
        ballsprite.update()
        paddlesprite.update()


        #ボールを描く
        ballsprite.draw(screen)
        paddlesprite.draw(screen)


        #表示更新
        pygame.display.flip()


if __name__ == '__main__': main()
