import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE, K_j, K_f
import random

WIDTH = 480
HEIGHT = 360

pygame.init()
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
FPSCLOCK = pygame.time.Clock()

class Sprite:
	def __init__(self, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.setxy(0, 0)
	def setx(self, x):
		self.rect.centerx = x + WIDTH / 2
	def sety(self, y):
		self.rect.centery = HEIGHT / 2 - y
	def setxy(self, x, y):
		self.setx(x)
		self.sety(y)
	def setdx(self, dx):
		self.rect.centerx += dx
	def setdy(self, dy):
		self.rect.centery -= dy
	def getx(self):
		return self.rect.centerx - WIDTH / 2
	def gety(self):
		return HEIGHT / 2 - self.rect.centery
	def draw(self):
		SURFACE.blit(self.image, self.rect.topleft)
		
class Cup(Sprite):
	_image = pygame.image.load("cup.svg")
	def __init__(self):
		super().__init__(Cup._image)
		
def main():
	cup = Cup()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_SPACE:
					cup.setxy(0, -100)
				elif event.key == K_j:
					if cup.getx() < 100:
						cup.setdx(100)
				elif event.key == K_f:
					if cup.getx() > -100:
						cup.setdx(-100)
		SURFACE.fill((255, 255, 255))
		cup.draw()
		pygame.display.update()
		FPSCLOCK.tick(30)

if __name__ == "__main__":
	main()
