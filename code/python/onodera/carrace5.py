import sys
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, KEYUP, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE
import math
import random

pygame.init()
width = 800
height = 600
SURFACE = pygame.display.set_mode((width, height))
FPSCLOCK = pygame.time.Clock()
SYSFONT = pygame.font.Font("ipaexg.ttf", 24)
SPEEDFONT = pygame.font.Font("ipaexg.ttf", 40)
TITLEFONT = pygame.font.Font("ipaexg.ttf", 72)
max_count = 0
velocity = 0

class State:
	def draw(self):
		pass
	def update(self, context):
		pass
		
class Singleton(object):
	def __new__(cls, *args, **kargs):
		if not hasattr(cls, "_instance"):
			cls._instance = super(Singleton, cls).__new__(cls)
		return cls._instance
		
class InitState(State, Singleton):
	def __init__(self):
		self.count_down = 49
		
	def draw(self):
		global velocity
		velocity = 0
		GameState(True).draw()
		image = TITLEFONT.render("{:2d}".format(self.count_down//10+1), True, (255, 0, 0))
		SURFACE.blit(image, (350,80))
	
	def update(self, context):
		self.count_down -= 1
		if self.count_down == 0:
			context.changeState(GameState(True))
		return False

class GameState(State, Singleton):
	def __init__(self, init):
		if init:
			self.time = Time(0, 5, 0)
			self.distance = Distance(0)
	
	def draw(self):
		self.distance.draw()
		self.time.draw()
		speed = velocity*144//10
		speed_image = SPEEDFONT.render("{:3d} Km/h".format(speed), True, (0, 0, 255))
		SURFACE.blit(speed_image, (600,80))
	
	def update(self, context):
		global max_count
		self.distance.add(velocity)
		max_count = max(max_count, self.distance.get())
		self.time.sub(1)
		if self.time.equal(0,0,0):
			context.changeState(GameOverState())
			return False
		if context.update():
			context.changeState(ExplosionState())
		return False

class GameOverState(State, Singleton):
	def draw(self):
		velocity = 0
		GameState(True).draw()
		image = TITLEFONT.render("Game Over", True, (255, 0, 0))
		SURFACE.blit(image, (200,80))

	def update(self, context):
		if context.restart:
			context.changeState(InitState())
			return True
		return False
		
class ExplosionState(State, Singleton):
	def __init__(self):
		self.count_down = 49
		
	def draw(self):
		GameState(False).draw()
		image = TITLEFONT.render("{:2d}".format(self.count_down//10+1), True, (255, 0, 0))
		SURFACE.blit(image, (350,80))
		
	def update(self, context):
		global velocity
		velocity = 0
		self.count_down -= 1
		if self.count_down == 0:
			context.changeState(GameState(False))
			return True
		GameState(False).update(context)
		return False

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
	def draw(self):
		image = SYSFONT.render(str(self), True, (255, 0, 0))
		SURFACE.blit(image, (50,20))
		
class Distance:
	def __init__(self, distance):
		self.distance = distance
	def add(self, velocity):
		self.distance += velocity
	def draw(self):
		image = SYSFONT.render("max: {:08.2f} km".format(max_count/250), True, (0, 0, 225))
		SURFACE.blit(image, (570,20))
		image = SYSFONT.render("{:08.2f} km".format(self.distance/250), True, (0, 0, 225))
		SURFACE.blit(image, (330,20))
	def get(self):
		return self.distance
		
class Car:
	image = pygame.image.load("./png/supra.png")
	explosion_image = pygame.image.load("./png/explosion.png")
	def __init__(self, x, y, size):
		self.x = x
		self.y = y
		self.size = size
		self.image = pygame.transform.scale(Car.image, (size, int(size * Car.image.get_height() / Car.image.get_width())))
		self.ratex = 0.73
		self.ratey = 0.7
	def move(self, road, dx):
		self.x += dx
		road_half = road.getWidth(self.y) / 2
		size_half = self.size * self.ratex / 2
		if self.x < width / 2 - road_half + size_half:
			self.x = width / 2 - road_half + size_half
		if self.x > width / 2 + road_half - size_half:
			self.x = width / 2 + road_half - size_half
	def draw(self, debug=False):
		x = self.x - self.image.get_width() / 2
		y = self.y - self.image.get_height() / 2
		SURFACE.blit(self.image, (x, y))
		if debug:
			pygame.draw.rect(SURFACE, (255,255,0), self.getRect(), 1)
	def getRect(self):
		x = self.x - self.image.get_width() / 2
		y = self.y - self.image.get_height() / 2
		rect = Rect(x, y, self.image.get_width(), self.image.get_height()).scale_by(self.ratex, self.ratey)
		return rect
	def explosion(self):
		self.image = pygame.transform.scale(Car.explosion_image, (300, 300))
	
class Tree:
	image = pygame.image.load("./png/light.png")
	def __init__(self):
		self.left = 315
		self.right = 485
		self.y = 175
		self.size = 50
	def inbound(self):
		return self.left >= 0 and self.right < 800 and self.y < 600	
	def draw(self):
		if self.inbound():
			size = int((self.y - 100) / 400 * 10 * self.size)
			image = pygame.transform.scale(Tree.image, (size, size))
			image2 = pygame.transform.flip(image, True, False)
			SURFACE.blit(image, (self.left - size / 2, self.y - size / 2))
			SURFACE.blit(image2, (self.right - size / 2, self.y - size / 2))
	def move(self, velocity):
		movex = int(velocity * 5 / (self.y - 100) * (self.right - 400))
		movey = velocity * 5
		self.left -= movex
		self.right += movex
		self.y += movey
	
class Rock:
	image = pygame.image.load("./png/toyota86.png")
	def __init__(self, speed):
		self.x = random.randint(354, 446) 
		self.y = 200
		self.size = 7
		self.ratex = 1
		self.ratey = 0.6
		self.speed = speed
	def inbound(self):
		return self.y > 100 and self.y <= 600 
	def getRect(self):
		size = int((self.y - 100) / 400 * 10 * self.size)
		x = self.x - size / 2
		y = self.y - size / 2
		return Rect(x, y, size, size)
	def draw(self, debug=False):
		if self.y >= 200:
			rect = self.getRect()
			image = pygame.transform.scale(Rock.image, rect.size)
			SURFACE.blit(image, rect.topleft)
			if debug:
				rect = self.getRect()
				rect = rect.scale_by(self.ratex, self.ratey).move(0, rect.height * 0.22)
				pygame.draw.rect(SURFACE, (255,255,0), rect, 1)
	def collision(self, car):
		rect = self.getRect()
		rect = rect.scale_by(self.ratex, self.ratey).move(0, rect.height * 0.22)
		return rect.colliderect(car.getRect())
	def move(self, velocity):
		velocity -= self.speed
		movex = int(velocity * 5 / (self.y - 100) * (self.x - 400))
		movey = velocity * 5
		self.x += movex
		self.y += movey

class Road:
	def __init__(self, width, color):
		self.roads = []
		self.width = width
		height = 5
		ypos = 200
		self.color = color
		while ypos < 600:
			self.roads.append(Rect(400 - width / 2, ypos, width, height))
			width += 5
			ypos += height
	def draw(self):
		for road in self.roads:
			pygame.draw.rect(SURFACE, self.color, road)
	def getWidth(self, y):
		return (y - 100) / 100 * self.width 
		
def main():
	global road
	game = Game()
	while True:
		game.play()
		
class Context:
	def changeState(self, state):
		pass
		
class Game(Context):
	def __init__(self):
		self.rocks = []
		self.trees = []
		self.state = InitState()
		self.road = Road(100, (224, 224, 224))
		
	def changeState(self, state):
		self.state = state
		
	def play(self):
		global velocity
		self.rocks.clear()
		self.trees.clear()
		self.trees.append(Tree())
		is_speed_up = False
		is_speed_down = False
		self.car = Car(400, 500, 100)
		move_x = 0
		while True:
			self.restart = False
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
						self.restart = True
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
			self.road.draw()
			for tree in reversed(self.trees):
				tree.draw()
			self.car.move(self.road, move_x)
			isCollision = False
			for rock in self.rocks:
				rock.draw()
			self.car.draw()
			self.state.draw()
			pygame.display.update()
			FPSCLOCK.tick(10)
			if self.state.update(self):
				return
				
	def update(self):
		for tree in self.trees:
			tree.move(velocity)
		if self.trees[-1].y >= 250:
			self.trees.append(Tree())
		self.trees = [tree for tree in self.trees if tree.inbound()]
		for rock in self.rocks:
			rock.move(velocity)
			if rock.collision(self.car):
				self.car.explosion()
				self.rocks.clear()
				return True
		if velocity > 0 and random.randint(0, 9) == 0:
			self.rocks.insert(0, Rock(random.randint(5, 15)))
		self.rocks = [rock for rock in self.rocks if rock.inbound()]
		return False
		
if __name__ == '__main__':
	main()