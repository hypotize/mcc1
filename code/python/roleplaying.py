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
				n = int(input(s + "のどれを選びますか？ -> "))
				clearConsole()
				if n >= 1 and n <= len(items):
					break
				print("1～{}のいずれかを入力してください。".format(len(items)))
		else:
			n = random.randint(1, len(items))
		item = items[n-1]
		print("{}は{}を使った。".format(self.name, item.name))
		time.sleep(1)
		if len(item.effect) == 1:
			return item.effect[0]
		else:
			return item.effect[random.randint(0, len(item.effect)-1)]
	
players = []
default_hp = 100

while True:
	n = int(input("何人で対戦しますか？（1人の時はコンピュータと対戦します） -> "))
	if n > 0:
		break
	print("1以上の値を入れて下さい。")

for i in range(n):
	name = input("プレイヤーの名前を入れて下さい。 -> ")
	players.append(Player(name, default_hp))
if n == 1:
	players.append(Player(None, default_hp))
	n = 2

turns = list(range(n))
random.shuffle(turns)
turn = 0

while len(turns) > 1:
	for i in range(n):
		if i in turns:
			players[i].show()
	print("{}さんの番です。 ".format(players[turns[turn]].name), end="")
	j = turns[turn]
	b = players[j].battle()
	if b > 0:
		for i in range(n):
			if i != j and i in turns:
				if players[i].damage(b):
					print("{}さんは死にました。".format(players[i].name))
					turns.remove(i)
	elif b < 0:
		players[j].heal(-b)
	else:
		print("何も起こらなかった。")
		time.sleep(1)
	turn = (turn + 1) % len(turns)
print("{}さんの勝ちです。".format(players[turns[0]].name))