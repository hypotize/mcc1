import pyxel

class App:
	def __init__(self):
		pyxel.init(128, 128)
		pyxel.load("./my_resource.pyxres")
		self.player_pos = [16, 16]
		self.message = None
		self.message_y = None
		self.answer = None
		self.message_time = 0
		self.money = 100
		self.weapons = []
		self.weapon_list = [("sword", 10), ("ax", 20), ("gun", 50)]
		pyxel.run(self.update, self.draw)
		
	def update(self):
		if self.message_time > 0:
			self.message_time -= 1
			if self.message_time == 0:
				self.message = None
				self.answer = None
			return
		if self.message is not None and self.answer is not None:
			if pyxel.btnp(pyxel.KEY_DOWN) and self.answer:
				self.answer = False
				self.message[1] = "  yes"
				self.message[2] = "> no "
			elif pyxel.btnp(pyxel.KEY_UP) and not self.answer:
				self.answer = True
				self.message[1] = "> yes"
				self.message[2] = "  no "
			elif pyxel.btnp(pyxel.KEY_RETURN):
				if self.answer:
					weapon = self.weapon_list[pyxel.rndi(0, len(self.weapon_list)-1)]
					if self.money >= weapon[1]:
						self.money -= weapon[1]
						self.weapons.append(weapon[0])
						self.message = ["You spent {} coins".format(weapon[1]), "You got {}".format(weapon[0])]
					else:
						self.message = ["You don't have enough money"]
					self.message_time = 90
				else:
					self.message = None
					self.answer = None
			return
		if pyxel.btnp(pyxel.KEY_P):
			self.message_y = 133 if self.player_pos[1] > 128 else 5
			self.message = ["Money: {} coins".format(self.money), "Wepons: {}".format(",".join(self.weapons))]
			self.message_time = 90
			return
		x, y = self.player_pos
		if pyxel.btnp(pyxel.KEY_RIGHT):
			if self.move_check(x+8, y):
				self.player_pos[0] += 8
		elif pyxel.btnp(pyxel.KEY_LEFT):
			if self.move_check(x-8, y):
				self.player_pos[0] -= 8
		elif pyxel.btnp(pyxel.KEY_UP):
			if self.move_check(x, y-8):
				self.player_pos[1] -= 8
		elif pyxel.btnp(pyxel.KEY_DOWN):
			if self.move_check(x, y+8):
				self.player_pos[1] += 8
			
	def move_check(self, x, y):
		if pyxel.tilemaps[0].pget(x//8, y//8)[1] == 0:
			return True
		self.event_check(x, y)
		return False
		
	def event_check(self, x, y):
		t = pyxel.tilemaps[0].pget(x//8, y//8)
		if t == (0, 4):
			pyxel.tilemaps[0].pset(11, 12, (1, 4))
			pyxel.tilemaps[0].pset(7, 9, (2, 0))
			pyxel.tilemaps[0].pset(8, 9, (3, 0))
		elif t == (2, 3) or t == (3, 3):
			self.player_pos = [7*8, 22*8]
			pyxel.camera(0, 16*8)
		elif t == (4, 3) or t == (5, 3):
			self.player_pos = [7*8, 7*8]
			pyxel.camera(0, 0)
		elif t == (4, 5):
			self.message_y = 208
			self.message = ["Do you buy weapon?", "> yes", " no "]
			self.answer = True
		
	def draw(self):
		pyxel.cls(0)
		pyxel.bltm(0, 0, 0, 0, 0, 128, 256)
		pyxel.blt(self.player_pos[0], self.player_pos[1], 1, 0, 0, 8, 8, 14)
		if self.message is not None:
			cnt = len(self.message)		
			l = max([len(x) for x in self.message]) * 4 + 8
			pyxel.rect(128 - l, self.message_y, l, 10*cnt, pyxel.COLOR_BLACK)
			pyxel.rectb(128 - l, self.message_y, l, 10*cnt, pyxel.COLOR_WHITE)
			i = 0
			for text in self.message:
				l = len(text) * 4 + 8
				pyxel.text(128 - l + 4, self.message_y + 2 + i * 10, text, pyxel.COLOR_WHITE)
				i += 1
		
App()
