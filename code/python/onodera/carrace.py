import sys
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, KEYUP, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE
import math
import random

pygame.init()
SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()

class Time:
	def __init__(self, hour, minute, second):
		self.second = second
		self.minute = minute
		self.hour = hour
	def add(self, second):
		self.second += second
		if self.second >= 60:
			self.minute += self.second // 60
			self.second %= 60
		if self.minute >= 60:
			self.hour += self.minute // 60
			self.minute %= 60
	def sub(self, second):
		self.second -= second
		while self.second < 0:
			self.second += 60
			self.minute -= 1
		while self.minute < 0:
			self.minute += 60
			self.hour -= 1
	def equal(self, hour, minute, second):
		return self.hour == hour and self.minute == minute and self.second == second
	def __str__(self):
		return "{:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

max_count = 0;

def main():
	global car_image, tree_image, explosion_image, rock_image
	image = pygame.image.load("./png/car_back1.png")
	car_image = pygame.transform.scale(image, (100, 100))
	image = pygame.image.load("./png/bakuhatsu.png")
	explosion_image = pygame.transform.scale(image, (100, 100))
	tree_image = pygame.image.load("./png/tree.png")
	tree_image.set_colorkey((255,255,255))
	tree_image.set_alpha(254)
	rock_image = pygame.image.load("./png/rock.png")
	while True:
		game()
		
def game():
	global max_count
	rocks = []
	roads = []
	width = 100
	height = 5
	ypos = 200
	while ypos < 600:
		roads.append(Rect(400-width/2, ypos, width, height))
		width += 5
		ypos += height
	trees = []
	trees.append(Rect(450, 175, 50, 50))
	trees.append(Rect(300, 175, 50, 50))
	velocity = 1
	is_speed_up = False
	is_speed_down = False
	move_x = 0
	car_x = 350
	distance = 0
	time = Time(0,5,0)
	sysfont = pygame.font.Font("ipaexg.ttf", 24)
	endfont = pygame.font.Font("ipaexg.ttf", 72)
	game_over = True
	count_down = 49
	while True:		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_UP:
					is_speed_up = True
				elif event.key == K_DOWN:
					is_speed_down = True
				elif event.key == K_LEFT:
					move_x = -10
				elif event.key == K_RIGHT:
					move_x = 10
				elif event.key == K_SPACE:
					return
			elif event.type == KEYUP:
				if event.key == K_UP:
					is_speed_up = False
				elif event.key == K_DOWN:
					is_speed_down = False
				elif event.key == K_LEFT or event.key == K_RIGHT:
					move_x = 0
		velocity += 1 if is_speed_up else -2 if is_speed_down else -1
		if velocity < 0:
			velocity = 0
		elif velocity > 20:
			velocity = 20
		SURFACE.fill((0, 255, 0))
		pygame.draw.rect(SURFACE, (0,255,255), (0, 0, 800, 200))
		for road in roads:
			pygame.draw.rect(SURFACE, (64, 64, 64), road)
		for tree in trees:
			image = pygame.transform.scale(tree_image, tree.size)
			if tree.bottom > 0 and tree.top < 600 and tree.right > 0 and tree.left < 800:
				SURFACE.blit(image, tree.topleft)
		if not game_over:
			car_x += move_x
			if car_x < 200:
				car_x = 200
			if car_x > 500:
				car_x = 500
		else:
			if count_down > 0:
				end_image = endfont.render("{:2d}".format(count_down//10+1), True, (255, 0, 0))
				SURFACE.blit(end_image, (350,80))
			else:
				end_image = endfont.render("Game Over", True, (255, 0, 0))
				SURFACE.blit(end_image, (150,80))
		
		c_image = car_image
		for rock in rocks:
			image = pygame.transform.scale(rock_image, rock.size)
			SURFACE.blit(image, rock.topleft)
#			pygame.draw.rect(SURFACE, (255,255,0), rock, 1)
			if rock.colliderect(Rect(car_x+20, 560, 60, 20)):
				c_image = explosion_image
				game_over = True
		SURFACE.blit(c_image, (car_x, 500))
#		pygame.draw.rect(SURFACE, (255,255,0), Rect(car_x+20, 540, 40, 50),  1)
		distance_image = sysfont.render("max: {:08.2f} km".format(max_count/250), True, (0, 0, 225))
		SURFACE.blit(distance_image, (570,20))
		distance_image = sysfont.render("{:08.2f} km".format(distance/250), True, (0, 0, 225))
		SURFACE.blit(distance_image, (330,20))
		time_image = sysfont.render(str(time), True, (255, 0, 0))
		SURFACE.blit(time_image, (50,20))
		pygame.display.update()
		FPSCLOCK.tick(10)
		if not game_over:
			distance += velocity
			max_count = max(max_count, distance)
			time.sub(1)
			if time.equal(0,0,0):
				game_over = True
			for tree in trees:
				move = math.floor((tree.centery / 100)**2 / 3) * velocity
				centerx = tree.centerx + (-move if tree.centerx < 400 else move)
				centery = tree.centery + move
				width = tree.width + 2 * velocity
				height = tree.height + 2 * velocity
				top = centery - height / 2
				left = centerx - width / 2
				tree.update(left, top, width, height)
			if trees[-1].bottom >= 300:
				trees.append(Rect(450, 175, 50, 50))
				trees.append(Rect(300, 175, 50, 50))
			if trees[0].top >= 600 or trees[0].right <= 0 or trees[0].left >= 800:
				trees.pop(0)
			for rock in rocks:
				move = math.floor((rock.centery / 100)**2 / 3) * velocity
				centerx = rock.centerx + (-move/2 if rock.centerx < 380 else move/2 if rock.centerx > 420 else 0)
				centery = rock.centery + move
				width = rock.width + (velocity//2) * 2
				height = rock.height + (velocity//2) * 2
				top = centery - height / 2
				left = centerx - width / 2
				rock.update(left, top, width, height)
			if velocity > 0 and random.randint(0,9) == 0:
				rocks.insert(0, Rect(random.randint(350,450), 200, 10, 10))
			if len(rocks) > 0 and rocks[-1].top >= 600:
				rocks.pop()
		elif count_down > 0:
			count_down -= 1
			if count_down == 0:
				game_over = False

	
if __name__ == '__main__':
	main()