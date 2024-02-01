import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_SPACE, K_j, K_f
import random

class Sprite:
	def __init__(self, image, x, y):
		self.image = image
		self.x = x
		self.y = y
	def draw(self, surface):
		surface.blit(self.image, (self.x, self.y))	
	def get_rect(self):
		rect = self.image.get_rect()
		rect.left = self.x
		rect.top = self.y
		return rect
		
class Cup(Sprite):
	def __init__(self, x, y):
		super().__init__(pygame.image.load("cup.svg"), x, y)

class Ball(Sprite):
	_image = None
	def __init__(self, x, y):
		if Ball._image is None:
			Ball._image = pygame.image.load("ball.svg")
		super().__init__(Ball._image, x, y)
		self.alive = True
		self.speed = random.randint(5,15)
		self.lightning = False
	def update(self):
		self.y += self.speed
		
class Lightning(Sprite):
	_image = None
	def __init__(self, x, y):
		if Lightning._image is None:
			image = pygame.image.load("lightning.svg")
			Lightning._image = pygame.transform.scale_by(image, 0.5)
		super().__init__(Lightning._image, x, y)
		self.alive = True
		self.lightning = True
		self.speed = 15
	def update(self):
		self.y += self.speed		

pygame.init()
SURFACE = pygame.display.set_mode((400, 400))
FPSCLOCK = pygame.time.Clock()

def main():
	failCnt = 0
	balls = []
	cup = None
	TIMECNT = 0
	score = 0
	scorefont = pygame.font.SysFont(None, 36)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_SPACE:
					cup = Cup(150, 200)
					balls.clear()
					failCnt = 0
				elif cup is not None:
					if event.key == K_j:
						if cup.x < 200:
							cup.x += 100
					elif event.key == K_f:
						if cup.x > 100:
							cup.x -= 100
		FPSCLOCK.tick(10)
		TIMECNT += 1
		if cup is not None:
			if TIMECNT % 100 == 0:
				lightning = Lightning(random.randint(1,3)*100-35, 50)
				balls.append(lightning)
			elif TIMECNT % 20 == 0:
				ball = Ball(random.randint(1,3)*100-35, 50)
				balls.append(ball)
		for ball in balls:
			if ball.get_rect().colliderect(cup.get_rect()):
				if ball.lightning:
					pygame.mixer.Sound("failed.wav").play()
					failCnt += 1
				else:
					pygame.mixer.Sound("succeed.wav").play()
					score += 1
				ball.alive = False
			if ball.y > 170:
				if not ball.lightning:
					pygame.mixer.Sound("failed.wav").play()
					failCnt += 1
				ball.alive = False
			if failCnt > 2:
				pygame.quit()
				sys.exit()
			if ball.alive:
				ball.update()
		balls = [ball for ball in balls if ball.alive]
		SURFACE.fill((255, 255, 255))
		if cup is not None:
			cup.draw(SURFACE)
		for ball in balls:
			ball.draw(SURFACE)
		score_image = scorefont.render(str(score), True, (0, 255, 0))
		SURFACE.blit(score_image, (350, 0))
		pygame.display.update()
				
if __name__ == "__main__":
	main()