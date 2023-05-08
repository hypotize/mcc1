import time
import random

class Player:
	def __init__(self, name, dice):
		self.name = name
		self.dice = dice
	def drawDice(self):
		self.dice -= 1
		return random.randrange(6) + 1
	def drawAll(self):
		diceList = []
		for _ in range(self.dice):
			 diceList.append(self.drawDice())
		return diceList
	def __str__(self):
		return self.name + "(" + str(self.dice) + "個)"
	def setSeed(self):
		random.seed(time.time_ns())
		
class Arena:
	def __init__(self):
		self.arena = []
	def drawDice(self, dice):
		if not self.empty():
			n = random.randrange(len(self.arena)+1)
			random.shuffle(self.arena)
			for i in range(n):
				self.arena[i] = random.randrange(6) + 1
		self.arena.append(dice)
	def drawAll(self, diceList):
		self.arena = diceList
	def order(self):
		n = len(self.arena) - self.arena.count(1)
		self.arena = [i for i in self.arena if i != 1 and self.arena.count(i) == 1]
		return n - len(self.arena)
	def empty(self):
		return len(self.arena) == 0
	def __str__(self):
		return "[" + ",".join([str(i) if i != 1 else "X" for i in self.arena]) + "]"

diceTbl = [8, 7, 6, 5]
arena = Arena()
players = []
n = int(input("何人で遊びますか(2〜5)？ "))
for i in range(n):
	name = input("{}番目のプレイヤーの名前：".format(i+1))
	players.append(Player(name, diceTbl[n-2]))
	
isFirst = True
i = 0
while len(players) > 1:
	player = players[i]
	if isFirst or not arena.empty():
		input("{}さんサイコロを振ってください(enterキーを押す)".format(player))
		player.setSeed()
		dice = player.drawDice()
		arena.drawDice(dice)
		print("アリーナの状態:", arena)
		n = arena.order()
		print("整理後のアリーナの状態:", arena)
		if n > 0:
			print("サイコロの目が揃ったので{}個のサイコロをゲットしました".format(n))
			player.dice += n
		elif not isFirst and player.dice > 0:
			if int(input("もう一度振りますか？(Yes:1, No:0) ")) != 0:
				continue
		if isFirst and not arena.empty():
			isFirst = False
	else:
		input("{}さんサイコロを全部振ってください(enterキーを押す)".format(player))
		player.setSeed()
		diceList = player.drawAll()
		arena.drawAll(diceList)
		print("アリーナの状態:", arena)
		n = arena.order()
		print("整理後のアリーナの状態:", arena)
		if n > 0:
			print("ゾロ目のサイコロ{}個をゲットしました".format(n))
		player.dice = n
	if player.dice == 0:
		print("{}さんのサイコロがなくなったので負けです".format(player))
		players.remove(player)
	else:
		i += 1
	if i == len(players):
		i = 0
print("{}さんの勝ちです".format(players[0]))
