import random
import os
from sys import platform
import time

class Item:
	def __init__(self, name, effect):
		self.name = name
		self.effect = effect
		
items = [Item("剣", [20]), Item("魔法の剣", [0,50]), \
	Item("盾", [-20]), Item("魔法の盾", [0,-50])]
	
def str_items():
	s = ""
	for i, e in enumerate(items):
		s += str(i+1) + ":" + e.name + " "
	return s

def clearConsole():
	if platform == "win32":
		os.system('cls')
	else:
		os.system('clear')

class Player:
	def __init__(self, name, hp):
		self.hp = hp
		if name is None:
			self.name = "コンピュータ"
			self.is_human = False
		else:
			self.name = name
			self.is_human = True
	def heal(self, hp):
		self.hp += hp
		print("{}さんのhpが、{}に回復した。".format(self.name, self.hp))
		time.sleep(1)
	def damage(self, hp):
		hp = min(hp, self.hp)
		self.hp -= hp
		print("{}さんのhpが、{}に減らされた。".format(self.name, self.hp))
		time.sleep(1)
		return self.hp == 0
	def show(self):
		print("{}さんのhpは、{}です。".format(self.name, self.hp))
	def battle(self):
		if self.is_human:
			while True:
				s = str_items()
				n = int(input(s + "のどれを選びますか -> "))
				clearConsole()
				if n >= 1 and n <= len(items):
					break
				print("1～{}のいずれかを入力してください".format(len(items)))
		else:
			n = random.randint(1, len(items))
		item = items[n-1]
		print("{}は{}を使った".format(self.name, item.name))
		time.sleep(1)
		if len(item.effect) == 1:
			return item.effect[0]
		else:
			return item.effect[random.randint(0, len(item.effect)-1)]
	
players = []
default_hp = 100

while True:
	n = int(input("人同士で対戦しますか(1)、コンピュータと対戦しますか(2) -> "))
	if n == 1 or n == 2:
		break
	print("1か2のいずれかを入力してください")

name = input("プレイヤーの名前を入れて下さい -> ")
players.append(Player(name, default_hp))
if n == 1:
	name = input("プレイヤーの名前を入れて下さい -> ")
	players.append(Player(name, default_hp))
else:
	players.append(Player(None, default_hp))

turn = random.randint(0, 1)

while True:
	players[0].show()
	players[1].show()
	print("{}さんの番です。".format(players[turn].name))
	n = players[turn].battle()
	next = 1 if turn == 0 else 0
	if n > 0:
		if players[next].damage(n):
			break
	elif n < 0:
		players[turn].heal(-n)
	else:
		print("何も起こらなかった")
		time.sleep(1)
	turn = next
print("{}さんの負けです".format(players[next].name))