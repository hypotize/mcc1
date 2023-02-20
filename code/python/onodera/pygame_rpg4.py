import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
import requests
import sys
import platform
import time
import queue
import threading
import math
import random
import copy
#from win32gui import SetForegroundWindow

surface = None
fpsclock = None
sysfont = None

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
					self.opponent = result["value"]
					self.sid = False
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
		
	def play(self, offense, defense, id):
		console = Console((20, 280), sysfont)
	
		def draw():
			surface.fill((255,255,255))
			offense.draw(surface)
			defense.draw(surface)
			console.draw(surface)
			pygame.display.update()
			if console.waittime == 0:
				fpsclock.tick(10)
			else:
				fpsclock.tick(console.waittime)
				console.clear()		
	
		while True:
			offense.setcheck(True)
			defense.setcheck(False)
			item = None
			while item is None:
				offense.setmode()
				defense.setmode()
				if offense.id == id:
					if console.text is None:
						console.settext("{}さんの番です。アイテムを選び、クリックして下さい。".format(offense.name), 0)
					for event in pygame.event.get():
						if event.type == QUIT:
							self.c2s("quit")
							return
						elif event.type == MOUSEBUTTONDOWN:
							pos = event.pos						
							for i, it in enumerate(offense.items):
								if check_rect(it.rect, pos):
									if offense.select == i:
										item = offense.items[i]
										console.settext("{}は{}を使った。".format(offense.name, item.name), 0.3)
										if len(item.effect) == 1:
											effect = item.effect[0]
										else:
											effect = random.choice(item.effect)
										self.c2s("item","{}#{}".format(i, effect))
									else:
										offense.selectitem(i)
									break
				elif offense.select is None:
					console.settext("{}さんの番です".format(offense.name), 0)
					while self.q.empty():
						for event in pygame.event.get():
							if event.type == QUIT:
								self.c2s("quit")
								return
						draw()
					msg = self.q.get().split("#")
					if msg[0] == "quit":
						pygame.quit()
						sys.exit()
					elif msg[0] == "item":
						offense.selectitem(int(msg[1]))
						effect = int(msg[2])
				else:
					item = offense.items[offense.select]
					console.settext("{}は{}を使った。".format(offense.name, item.name), 0.3)
				draw()
			offense.clearselect()
			if effect > 0:
				defense.damage(effect)
				console.settext("{}のHPが{}に減った。".format(defense.name, defense.hp), 0.5)
			elif effect < 0:
				offense.damage(effect)
				console.settext("{}のHPが{}に回復した。".format(offense.name, offense.hp), 0.5)
			else:
				console.settext("何もおこならなった", 0.5)
			draw()
			if defense.hp == 0:
				pygame.event.clear()
				defense.setmode(5)
				console.settext("{}は死んでしまった。".format(defense.name), 0.3)
				draw()
				offense.setmode(6)
				console.settext("{}が{}に勝ちました。".format(offense.name, defense.name), 0.3)
				draw()
				break
			offense, defense = defense, offense
		
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

def check_rect(rect, pos):
	x, y, w, h = rect
	mx, my = pos
	return x <= mx and mx <= x+w and y <= my and my <= y+h
	
class Player:
	def __init__(self, name, hp, images, size, id):
		self.name = name
		self.id = id
		self.hp = hp
		self.images = []
		for fn in images:
			image = pygame.image.load(fn)
			self.images.append(pygame.transform.scale(image, (size, size)))
		self.checked = False
		self.mode = 0
		self.size = size
		self.items = []
		self.select = None
	def selectitem(self, i):
		for j, item in enumerate(self.items):
			if i == j:
				item.setcheck(True)
			elif item.checked:
				item.setcheck(False)
		self.select = i
	def clearselect(self):
		for item in self.items:
			if item.checked:
				item.setcheck(False)
		self.select = None
	def setpos(self, pos):
		self.rect = (pos[0], pos[1], self.size, self.size)
		x, y = pos[0], pos[1]+self.size+20
		for item in self.items:
			item.setpos((x, y))
			y += item.rect[3]
	def damage(self, hp):
		if hp > 0:
			self.mode = 4
			hp = min(hp, self.hp)
		else:
			self.mode = 3
		self.hp -= hp
	def setfont(self, font):
		self.font = font
		for item in self.items:
			item.setfont(font)
	def setcheck(self, checked):
		self.checked = checked
	def setmode(self, mode=None):
		if mode is None:
			if self.hp > 100:
				self.mode = 1
			elif self.hp <= 50:
				self.mode = 2
			else:
				self.mode = 0
		else:
			self.mode = mode
	def additem(self, item):
		self.items.append(copy.copy(item))
	def draw(self, surface):
		surface.blit(self.images[self.mode], (self.rect[0], self.rect[1]))
		if self.checked:
			pygame.draw.rect(surface, (255,0,0), self.rect, 3)
		profile = self.font.render("{} HP:{}".format(self.name, self.hp), True, (0,0,0))
		surface.blit(profile, (self.rect[0], self.rect[1]+self.size))
		for item in self.items:
			item.draw(surface)
		
class Item:
	def __init__(self, name, imagefile, effect, size):
		self.name = name
		self.effect = effect
		self.imagefile = imagefile
		image = pygame.image.load(imagefile)
		self.image = pygame.transform.scale(image, (size, size))
		self.size = size
		self.checked = False
	def setpos(self, pos):
		self.rect = (pos[0], pos[1], 150, self.size)
	def setcheck(self, checked):
		self.checked = checked
	def setfont(self, font):
		self.font = font
	def draw(self, surface):
		surface.blit(self.image, (self.rect[0], self.rect[1]))
		if self.checked:
			pygame.draw.rect(surface, (0,0,255), self.rect, 3)
		profile = self.font.render("{} 効果:{}".format(self.name, str(self.effect)), True, (0,0,0))
		surface.blit(profile, (self.rect[0]+self.size+10, self.rect[1]+self.size//4))
	def __copy__(self):
		return Item(self.name, self.imagefile, self.effect, self.size)
		
items = [Item("剣", "png/game_ken.png", [20], 25),\
	Item("魔剣", "png/game_ken_maken.png", [0, 50], 25),\
	Item("薬", "png/medical_kusuri_bin.png", [-20], 25),
	Item("謎の薬", "png/medical_bannouyaku.png", [0, -50], 25)]
	
class Console:
	def __init__(self, pos, font):
		self.pos = pos
		self.font = font
		self.waittime = 0
		self.text = None
	def settext(self, text, waittime):
		self.text = text
		self.waittime = waittime
	def clear(self):
		self.waittime = 0
		self.text = None
	def draw(self, surface):
		if self.text is not None:
			text = self.font.render(self.text, True, (0,0,0))
			surface.blit(text, self.pos)

def main(client):
	global surface, fpsclock, sysfont
	pygame.init()
	surface = pygame.display.set_mode((400,300))
	pygame.display.set_caption("RPG4")
#	SetForegroundWindow(pygame.display.get_wm_info()['window'])
	fpsclock = pygame.time.Clock()
	sysfont = pygame.font.Font("ipaexg.ttf", 12)
	
	if client.sid:
		sid = 0
		eid = 1
		player1 = client.name
		player2 = client.opponent
		turn = random.choice([True, False])
		client.c2s("turn", str(turn))
	else:
		sid = 1
		eid = 0
		player1 = client.opponent
		player2 = client.name
		while client.q.empty():
			time.sleep(0.1)
		command = client.q.get().split("#")
		if command[0] != "turn":
			print("initialize error:", command)
			sys.exit()
		turn = command[1] == "False"
		
	players = [Player(player1, 100, ["png/stand1_front05_man.png", "png/pose_genki03_man.png", \
		"png/shinpai_man.png", "png/yaruki_moeru_man.png", "png/pose_shock_man.png",\
		"png/sick_kaoiro_man.png", "png/seikou_banzai_man.png"], 150, 0), \
		Player(player2, 100, ["png/stand1_front06_woman.png", "png/pose_genki04_woman.png",\
		"png/shinpai_woman.png", "png/yaruki_moeru_woman.png", "png/pose_shock_woman.png",\
		"png/sick_kaoiro_woman.png", "png/seikou_banzai_woman.png"], 150, 1)]
	x = 30
	for player in players:
		for item in items:
			player.additem(item)
		player.setfont(sysfont)
		player.setpos((x,0))
		x += 200
	
	offense = players[sid if turn else eid]
	defense = players[eid if turn else sid]

	client.play(offense, defense, sid)

if __name__ == '__main__':

	if len(sys.argv) != 3:
		print("usage: python pygame_rpg4.py ipaddress name")
		sys.exit()

	ipaddress = sys.argv[1]
	port = 8000
	hostname = platform.uname()[1]
	name = sys.argv[2]

	url = "http://{}:{}/pygame_rpg4/{}".format(ipaddress, port, hostname)

	q = queue.Queue()
	client = Client(q, url)
	if not client.com_init(name):
		sys.exit()
	time.sleep(0.1)
	server = Server(q, url)
	main(client)
	pygame.quit()
	sys.exit()