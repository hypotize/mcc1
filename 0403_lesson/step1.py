import sys
import math
import os
import pygame
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
            #else:
            # Deflate the rectangles so you can't catch a ball behind the bat
            #player1.rect.inflate(-3, -3)
            #player2.rect.inflate(-3, -3)

            # Do ball and bat collide?
            # Note I put in an odd rule that sets self.hit to 1 when they collide, and unsets it in the next
            # iteration. this is to stop odd ball behaviour where it finds a collision *inside* the
            # bat, the ball reverses, and is still inside the bat, so bounces around inside.
            # This way, the ball can always escape and bounce away cleanly
            #$if self.rect.colliderect(player1.rect) == 1 and not self.hit:
            #$    angle = math.pi - angle
            #$    self.hit = not self.hit
            #elif self.rect.colliderect(player2.rect) == 1 and not self.hit:
            #    angle = math.pi - angle
            #    self.hit = not self.hit
            #elif self.hit:
            #    self.hit = not self.hit
        self.vector = (angle,z)

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)

class Bat(pygame.sprite.Sprite):
    """Movable tennis 'bat' with which one hits the ball
    Returns: bat object
    Functions: reinit, update, moveup, movedown
    Attributes: which, speed"""

    def __init__(self, side):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('bat.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.side = side
        self.speed = 10
        self.state = "still"
        self.reinit()

    def reinit(self):
        self.state = "still"
        self.movepos = [0,0]
        if self.side == "left":
            self.rect.midleft = self.area.midleft
        elif self.side == "right":
            self.rect.midright = self.area.midright

    def update(self):
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        pygame.event.pump()

    def moveup(self):
        self.movepos[1] = self.movepos[1] - (self.speed)
        self.state = "moveup"

    def movedown(self):
        self.movepos[1] = self.movepos[1] + (self.speed)
        self.state = "movedown"

def main():
    # 画面の初期化
    pygame.init()
    screen = pygame.display.set_mode((480, 360))
    pygame.display.set_caption('ピンポンゲームステップ1')

    # 背景
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255,255))

    # Initialise players
#    global player1
#    global player2
#    player1 = Bat("left")
#    player2 = Bat("right")

    # ボール初期化
    #  (初期x座標,初期y座標), (初期角度ラジアン, 速度)
    ball = Ball((240,100),(-0.6,6))

    # 描く
#    playersprites = pygame.sprite.RenderPlain((player1, player2))
    ballsprite = pygame.sprite.RenderPlain(ball)

    # 画面に出す
    screen.blit(background, (0, 0))
    #pygame.display.flip()

    # Initialise clock
    clock = pygame.time.Clock()

    # Event loop
    while 1:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
 #           elif event.type == KEYDOWN:
 #               if event.key == K_a:
 #                   player1.moveup()
 #               if event.key == K_z:
 #                   player1.movedown()
 #               if event.key == K_UP:
 #                   player2.moveup()
 #               if event.key == K_DOWN:
 #                   player2.movedown()
 #           elif event.type == KEYUP:
 #               if event.key == K_a or event.key == K_z:
 #                   player1.movepos = [0,0]
 #                   player1.state = "still"
 #               if event.key == K_UP or event.key == K_DOWN:
 #                   player2.movepos = [0,0]
 #                   player2.state = "still"

        screen.blit(background, ball.rect, ball.rect)
        #screen.blit(background, player1.rect, player1.rect)
        #screen.blit(background, player2.rect, player2.rect)
        ballsprite.update()
        #playersprites.update()
        ballsprite.draw(screen)
        #playersprites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__': main()
