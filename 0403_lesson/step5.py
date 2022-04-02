import sys
import math
import os
import pygame
import random
from pygame.locals import *

# 画像のロード
def load_png(name):
    try:
        image = pygame.image.load(name)
        image = image.convert_alpha()
    except pygame.error as message:
        print('Cannot load image:', fullname)
        raise SystemExit(message)
    return image, image.get_rect()

class Ball(pygame.sprite.Sprite):

    def __init__(self, startpos, vector):
        pygame.sprite.Sprite.__init__(self)

        self.image, self.rect = load_png('ball.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector
        self.hit = 0
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos
        (angle,z) = self.vector

        if not self.area.contains(newpos):
            tl = not self.area.collidepoint(newpos.topleft)
            tr = not self.area.collidepoint(newpos.topright)
            bl = not self.area.collidepoint(newpos.bottomleft)
            br = not self.area.collidepoint(newpos.bottomright)
            if tr and tl or (br and bl):
                angle = -angle
            if tl and bl:
                angle = math.pi - angle
            if tr and br:
                angle = math.pi - angle

        if self.rect.colliderect(paddle.rect) == 1:
            print('hit paddle')
            print(angle)
            # 角度はラジアン
            # https://univ-juken.com/kodoho
            # 0 は右方向 2 π で一周
            minangle =   math.pi *1.25
            maxangle =  math.pi *1.75
            angle = random.uniform(minangle, maxangle)
            global score
            score += 1

        if self.rect.colliderect(line.rect) == 1:
            print('hit line')
            z = 0
            global speed
            speed = 0
        self.vector = (angle,z)

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (speed * math.cos(angle),speed * math.sin(angle))
        return rect.move(dx,dy)

class Paddle(pygame.sprite.Sprite):

    def __init__(self, startpos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('paddle.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]
        
    def update(self):
        mousepos = pygame.mouse.get_pos()
        self.rect.midtop = (mousepos[0], 300)    
    
class Line(pygame.sprite.Sprite):

    def __init__(self, startpos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('line.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]

def main():
    # 画面の初期化
    pygame.init()
    screen = pygame.display.set_mode((480, 360))
    pygame.display.set_caption('ピンポンゲームステップ1')

    # 背景
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255,255))

    global paddle
    global line
    global score
    score = 0

    global speed
    speed = 6

    # ボール初期化
    #  (初期x座標,初期y座標), (初期角度ラジアン, 速度)
    ball = Ball((240,100),(-0.6,speed))

    # パドル初期化
    paddle = Paddle((10,300))

    line = Line((240,353))
    
    # 描く
    ballsprite = pygame.sprite.RenderPlain(ball)
    paddlesprite = pygame.sprite.RenderPlain(paddle)
    linesprite = pygame.sprite.RenderPlain(line)

    # 画面に出す
    screen.blit(background, (0, 0))
    #pygame.display.flip()

    # Initialise clock
    clock = pygame.time.Clock()

    font = pygame.font.SysFont('arial', 15)
    scoretext = font.render('Score: {:03d}'.format(score), True, (0,0,0))
    screen.blit(scoretext, (10,5))
    
    speedtext = font.render('Speed:  {:02d}'.format(speed), True, (0,0,0))
    screen.blit(speedtext, (10,28))
    
    # Event loop
    while 1:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)

        scoretext.fill((255, 255,255))
        screen.blit(scoretext, (10,5))
        scoretext = font.render('Score: {:03d}'.format(score), True, (0,0,0))
        screen.blit(scoretext, (10,5))

        speedtext.fill((255, 255,255))
        screen.blit(speedtext, (10,28))
        speedtext = font.render('Speed:  {:02d}'.format(speed), True, (0,0,0))
        screen.blit(speedtext, (10,28))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                if event.key == K_q:
                    return
                if event.key == K_UP:
                    speed += 1
                    if speed > 99:
                        speed = 99
                if event.key == K_DOWN:
                    speed -= 1
                    if speed < 1:
                        speed = 1

        screen.blit(background, ball.rect, ball.rect)
        screen.blit(background, paddle.rect, paddle.rect)
        screen.blit(background, line.rect, line.rect)

        ballsprite.update()
        paddlesprite.update()

        ballsprite.draw(screen)
        paddlesprite.draw(screen)
        linesprite.draw(screen)

        pygame.display.flip()


if __name__ == '__main__': main()
