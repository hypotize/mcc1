import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
import random

class CustomButton:
	def __init__(self, i):
		self.font = pygame.font.SysFont(None, 40)
		self.isMovable = False
		self.visible = True
		self.name = str(i+1)
		self.position = i
		self.rect = pygame.Rect((i % 4) * 100, (i // 4) * 100, 99, 99)
		self.setText(self.name)
	def setText(self, text):
		self.text = self.font.render(text, True, (0, 0, 0))
		self.text_rect = self.text.get_rect()
	def collidepoint(self, x, y):
		return self.rect.collidepoint(x, y)
	def move(self, cb):
		if self.isMovable:
			self.position, cb.position = cb.position, self.position
			self.rect, cb.rect = cb.rect, self.rect
	def show(self, surface):
		if self.visible:
			pygame.draw.rect(surface, (192, 192, 192), self.rect)
			pygame.draw.rect(surface, (0, 0, 0), self.rect, width=1)
			self.text_rect.center = self.rect.center
			surface.blit(self.text, self.text_rect.topleft)

class Game:
	def __init__(self, title, width, height):
		pygame.init()
		self.SURFACE = pygame.display.set_mode([width, height])
		pygame.display.set_caption(title)
		self.FPSCLOCK = pygame.time.Clock()
		self.myCustomButton = []
		self.randlist = []
		for i in range(16):
			self.myCustomButton.append(CustomButton(i))
		self.init()
	def init(self):
		self.myCustomButton[15].visible = False
		self.setMovable()
		for i in range(100):
			random.choice(self.randlist).move(self.myCustomButton[15])
			self.setMovable()
	def setMovable(self):
		self.randlist.clear()
		x15 = self.myCustomButton[15].position % 4
		y15 = self.myCustomButton[15].position // 4
		for button in self.myCustomButton:
			x = button.position % 4
			y = button.position // 4
			if (y == y15 and abs(x - x15) == 1) or \
				(x == x15 and abs(y - y15) == 1):
				button.isMovable = True
				self.randlist.append(button)
			else:
				button.isMovable = False
	def checkComplete(self):
		for button in self.myCustomButton:
			if button.name != str(button.position+1):
				return
		self.myCustomButton[15].setText("OK")
		self.myCustomButton[15].visible = True
	def button_click(self, x, y):
		for button in self.myCustomButton:
			if button.collidepoint(x, y):
				if button == self.myCustomButton[15] and button.visible:
					self.init()
				else:
					button.move(self.myCustomButton[15])
					self.setMovable()
					self.checkComplete()
				break
	def show(self):
		self.SURFACE.fill((255, 255, 255))
		for button in self.myCustomButton:
			button.show(self.SURFACE)
		pygame.display.update()
		self.FPSCLOCK.tick(15)

def main():
	game = Game("15 puzzle", 400, 400)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				x, y = event.pos
				game.button_click(x, y)
		game.show()

if __name__ == '__main__':
	main()
