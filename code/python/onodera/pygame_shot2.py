import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE, Rect
import requests
import sys
import platform
import time
import queue
import threading
import math
from win32gui import SetForegroundWindow

surface = None
fpsclock = None

class Client:
	def __init__(self, q, url):
		self.q = q
		self.url = url
		self.headers = {"Content-Type": "application/json"}
	def c2s(self, command, value=""):
		data = {"command" : command, "value" : value}
		r = requests.post(url, headers=self.headers, json=data)
		if r.status_code != 200:
			print("cannot post: error code =", r.status_code)
			return None;
		return r.json()
	def com_init(self, name):
		self.name = name
		result = self.c2s("register", name)
		if result is None or result["result"] == "error":
			if result is not None:
				print(result)
			return False
		try:
			opponent = None
			while opponent is None:
				result = self.c2s("opponent")
				if result is None or result["result"] == "error":
					if result is not None:
						print(result)
					return False
				if result["result"] == "connected":
					print(result["value"], "さんと接続しました")
					self.sid = False
					self.opponent = result["value"]
					return True
				if len(result) == 1:
					print("接続相手が見つかりません")
					time.sleep(1)
					continue
				for key, value in result.items():
					if key == "result":
						continue
					opponent = (key, value)
					break
			result = self.c2s("connect", opponent[0])
			if result is None or result["result"] == "error":
				if result is not None:
					print(result)
				return False
			if result["result"] == "succeed" or \
				result["result"] == "connected":
				print(result["value"], "さんと接続しました")
			self.opponent = result["value"]
			self.sid = result["result"] == "succeed"
			return True
		except:
			self.c2s("quit")
			sys.exit()
		
class Server:
	def __init__(self, q, url):
		self.q = q
		self.url = url
		self.thread = threading.Thread(target=self.c2s, daemon=True)
		self.thread.start()
	def c2s(self):
		try:
			while True:
				r = requests.get(url)
				if r.status_code != 200:
					raise Exception("cannot get: error code = {}".format(r.status_code))
				else:
					result = r.json()
					if "error" in result:
						raise Exception("error! reason : " + result["error"])
					if result["command"] != "none":
						if "value" in result:
							msg = result["command"] + "#" + result["value"]
						else:
							msg = result["command"] + "#"
						self.q.put(msg)
					else:
						time.sleep(0.1)
		except Exception as e:
			print(e)

class Ship:
	def __init__(self, is_self, name):
		self.point = 0
		self.angle = -20
		self.shots = []
		self.size = 100
		self.is_self = is_self
		self.name = name
		self.font = pygame.font.Font("ipaexg.ttf", 20)
		if is_self:
			image = pygame.image.load("png/war_sentouki_man.png")
			self.image = pygame.transform.scale(image, (self.size, self.size))
		else:
			image = pygame.image.load("png/war_sentouki_woman.png")
			image = pygame.transform.scale(image, (self.size, self.size))
			self.image = pygame.transform.flip(image, True, False)
		self.orgimg = self.image
		image = pygame.image.load("png/bakuhatsu.png")
		self.explosion_img = pygame.transform.scale(image, (self.size, self.size))
		self.alive = True
	def restart(self):
		self.angle = -20
		self.shots.clear()
		self.image = self.orgimg
		self.alive = True
	def setpos(self, pos):
		self.rect = Rect(pos[0] + self.size / 4, pos[1] + self.size / 4, self.size / 2, self.size / 1.5)
	def move(self, dy):
		if self.alive and ((dy > 0 and self.rect.bottom + dy < 600) or (dy < 0 and self.rect.top + dy > 0)):
			self.rect = self.rect.move(0, dy)
	def rotate(self, angle):
		if self.alive and (self.angle + angle >= -65 and self.angle + angle <= 25):
			self.angle += angle
	def shot(self, angle=None):
		if angle is None:
			angle = self.angle+20
		if self.alive and len(self.shots) < 7:
			shot = Shot(self.is_self, angle)
			shot.setpos((self.rect.center[0] + (50 if self.is_self else -50), self.rect.center[1]+20))
			self.shots.append(shot)
			return angle
		return None
	def explosion(self):
		self.image = self.explosion_img
		self.shots.clear()
		self.alive = False
	def draw(self):
		image = pygame.transform.rotate(self.image, -self.angle if self.is_self else self.angle)
		surface.blit(image, (self.rect.topleft[0] - self.size / 4, self.rect.topleft[1] - self.size / 4))
		name = self.font.render(self.name, True, (0,0,0))
		surface.blit(name, (self.rect.center[0]-30, self.rect.center[1]+50))
		for shot in self.shots:
			shot.draw()
			if shot.move():
				self.shots.remove(shot)
		
		
class Shot:
	def __init__(self, is_self, angle):
		self.size = 4
		self.is_self = is_self
		self.dy = math.sin(math.radians(angle)) * 10;
		self.dx = math.cos(math.radians(angle)) * 10
	def setpos(self, pos):
		self.rect = Rect(pos[0], pos[1], self.size, self.size)
	def move(self):
		if self.is_self:
			if self.rect.right + self.dx < 800 and self.rect.top + self.dy > 0 and self.rect.bottom + self.dy < 600:
				self.rect = self.rect.move(self.dx, self.dy)
			else:
				return True
		else:
			if self.rect.left - self.dx > 0 and self.rect.top + self.dy > 0 and self.rect.bottom + self.dy < 600:
				self.rect = self.rect.move(-self.dx, self.dy)
			else:
				return True
		return False
	def draw(self):
		pygame.draw.circle(surface, (0,255,0) if self.is_self else (0,0,255), self.rect.center, self.size)


	
def main(client):
	global surface, fpsclock
	pygame.init()
	surface = pygame.display.set_mode((800,650))
	pygame.display.set_caption("Shot2")
	SetForegroundWindow(pygame.display.get_wm_info()['window'])
	fpsclock = pygame.time.Clock()
	sysfont = pygame.font.Font("ipaexg.ttf", 30)
	numfont = pygame.font.Font("ipaexg.ttf", 12)
	myship = Ship(True, client.name)
	yourship = Ship(False, client.opponent)
		
	while True:
		myship.restart()
		yourship.restart()
		myship.setpos((50, 250))
		yourship.setpos((650, 250))
		move_y = 0
		angle = 0
		message = None
		wait = 0
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					client.c2s("quit")
					pygame.quit()
					sys.exit()
				elif event.type == KEYDOWN:
					if event.key == K_UP:
						move_y = -10
					elif event.key == K_DOWN:
						move_y = 10
					elif event.key == K_SPACE:
						shot_angle = myship.shot()
						if shot_angle is not None:
							client.c2s("shot", str(shot_angle))
					elif event.key == K_LEFT:
						angle = 5
					elif event.key == K_RIGHT:
						angle = -5
				elif event.type == KEYUP:
					move_y = 0
					angle = 0
			if move_y != 0:
				myship.move(move_y)
				client.c2s("move", str(move_y))
			if angle != 0:
				myship.rotate(angle)
				client.c2s("rotate", str(angle))
			if client.q.empty() == False:
				cmd = client.q.get().split("#")
				if cmd[0] == "quit":
					pygame.quit()
					sys.exit()
				elif cmd[0] == "move":
					yourship.move(int(cmd[1]))
				elif cmd[0] == "rotate":
					yourship.rotate(int(cmd[1]))
				elif cmd[0] == "shot":
					yourship.shot(int(cmd[1]))
				elif cmd[0] == "lose":
					yourship.explosion()
					myship.shots.clear()
					message = "あなたの勝ち" if myship.alive else "相打ち"
					myship.point += 1
			for shot in yourship.shots:
				if myship.alive and myship.rect.colliderect(shot.rect):
					myship.explosion()
					yourship.shots.clear()
					message = "あなたの負け" if yourship.alive else "相打ち"
					yourship.point += 1
					client.c2s("lose")
					break
			surface.fill((255,255,255))
			text = numfont.render("{:06d}".format(myship.point), True, (0,0,255))
			surface.blit(text, (10, 10))
			text = numfont.render("{:06d}".format(yourship.point), True, (0,0,255))
			surface.blit(text, (740, 10))
			myship.draw()
			yourship.draw()
			if message is not None:
				text = sysfont.render(message, True, (255,0,0))
				surface.blit(text, (300, 250))
			pygame.display.update()
			fpsclock.tick(15)
			if not myship.alive or not yourship.alive:
				if wait == 0:
					wait = 100
				else:
					wait -= 1
					if wait == 0:
						break

if __name__ == '__main__':

	if len(sys.argv) != 3:
		print("usage: python pygame_shot2.py ipaddress name")
		sys.exit()

	ipaddress = sys.argv[1]
	port = 8000
	hostname = platform.uname()[1]
	name = sys.argv[2]

	url = "http://{}:{}/pygame_shot2/{}".format(ipaddress, port, hostname)

	q = queue.Queue()
	client = Client(q, url)
	if not client.com_init(name):
		sys.exit()
	time.sleep(0.1)
	server = Server(q, url)
	main(client)