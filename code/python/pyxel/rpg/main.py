import pyxel

class Nyokki:
	def __init__(self, app):
		self.app = app
		self.player_pos = [7*8+128, 11*8+128]
		pyxel.camera(16*8, 16*8)
		self.enemies = [[2*8+128, 3*8+128, pyxel.rndi(0, 15), 0],
			[7*8+128, 3*8+128, pyxel.rndi(0, 15), 0],
			[12*8+128, 3*8+128, pyxel.rndi(0, 15), 0],
			[2*8+128, 7*8+128, pyxel.rndi(0, 15), 0],
			[7*8+128, 7*8+128, pyxel.rndi(0, 15), 0],
			[12*8+128, 7*8+128, pyxel.rndi(0, 15), 0]]
		self.player_num = -1
		self.num = 0
		self.no = 0
		self.tcnt = 0
		self.sec = -4
		self.game_over = None
		self.start = False
		self.update = self.update1
	def update1(self):
		if pyxel.btnp(pyxel.KEY_RETURN):
			self.start = True
			self.update = self.update2
			self.tcnt = 0
	def update2(self):
		if self.sec > -1 and self.player_num < 0 and pyxel.btnp(pyxel.KEY_SPACE):
			self.player_num = self.sec+1
		self.tcnt += 1
		if self.tcnt % 30 == 0:
			self.sec += 1
			if self.sec < 0:
				return
			if self.sec == 16:
				self.game_over = False
				self.tcnt = 0
				self.update = self.update3
				return
			if self.sec == self.player_num or self.sec in [enemy[2] for enemy in self.enemies]:
				self.no += 1
				cnt = 0
				if self.sec == self.player_num:
					self.num = self.no
					cnt += 1
				for enemy in self.enemies:
					if enemy[2] == self.sec:
						enemy[3] = self.no
						cnt += 1
				if cnt > 1:
					self.game_over = self.sec != self.player_num
					self.tcnt = 0
					self.update = self.update3
				else:
					if self.sec == self.player_num:
						self.tcnt = 0
						self.game_over = True
						self.update = self.update3
					elif all([enemy[3] != 0 for enemy in self.enemies]):
						self.tcnt = 0
						self.game_over = False
						self.update = self.update3

	def update3(self):
		self.tcnt += 1
		if self.tcnt == 90:
			if self.game_over:
				self.app.level += 1
			self.app.game = None
			self.app.player_pos = [16, 16]
			pyxel.tilemaps[0].pset(11, 12, (0, 4))
			pyxel.tilemaps[0].pset(7, 9, (0, 3))
			pyxel.tilemaps[0].pset(8, 9, (1, 3))
			self.app.message = None
			self.app.message_y = None
			self.app.answer = None
			pyxel.camera(0, 0)
		
	def draw(self):
		if self.start:
			pyxel.text(7*8+4+128, 10+128, "{:2d}".format(self.sec+1), pyxel.COLOR_LIGHT_BLUE if self.sec >= -1 else pyxel.COLOR_RED)
		for enemy in self.enemies:
			if enemy[3] > 0:
				pyxel.text(enemy[0]-8, enemy[1]-8, "{} Nyokki!".format(enemy[3]), pyxel.COLOR_WHITE)
				pyxel.blt(enemy[0], enemy[1], 1, 0, 8, 16, 16, pyxel.COLOR_WHITE)
			else:
				pyxel.blt(enemy[0], enemy[1], 1, 16, 8, 16, 16, pyxel.COLOR_WHITE)
		if self.player_num >= 0 and self.num > 0:
			pyxel.text(self.player_pos[0]-8, self.player_pos[1]-8, "{} Nyokki!".format(self.num), pyxel.COLOR_WHITE)
			pyxel.blt(self.player_pos[0], self.player_pos[1], 1, 0, 8, 16, 16, pyxel.COLOR_WHITE)
		else:
			pyxel.blt(self.player_pos[0], self.player_pos[1], 1, 16, 8, 16, 16, pyxel.COLOR_WHITE)
		if self.game_over is not None:
			if self.game_over:
				pyxel.text(4*8+128, 14*8+128, "You Win!! Level Up!!", pyxel.COLOR_DARK_BLUE)
			else:
				pyxel.text(4*8+128, 14*8+128, "You Lose!! Try Again!!", pyxel.COLOR_RED)
		elif not self.start:
			pyxel.text(6*8+128, 10+128, "Nyokki Game", pyxel.COLOR_BLACK)
			pyxel.text(2*8+128, 14*8+128, "Please Press ENTER Key", pyxel.COLOR_BLACK)
		elif self.player_num < 0:
			pyxel.text(2*8+128, 14*8+128, "Please Press SPACE Key", pyxel.COLOR_BLACK)
			
class Memorize:
	def __init__(self, app):
		self.app = app
		pyxel.camera(32*8, 16*8)
		self.number = []
		for _ in range(7):
			self.number.append(pyxel.rndi(0, 9))
		self.update = self.update1
		self.draw = self.draw1
		self.index = -1
		self.tcnt = 60
		self.game_over = None
		self.display_num = None

	def update1(self):
		if pyxel.btnp(pyxel.KEY_RETURN):
			self.update = self.update2
			self.draw = self.draw2

	def update2(self):
		self.tcnt -= 1
		if self.tcnt == 0:
			self.tcnt = 60
			if self.display_num is None:
				self.index += 1
				if self.index == len(self.number):
					self.update = self.update3
					self.draw =self.draw3
					self.index = -1
					return
				self.display_num = self.number[self.index]
			else:
				self.display_num = None 

	def update3(self):
		if self.game_over is not None:
			self.tcnt -= 1
			if self.tcnt == 0:
				if self.game_over:
					self.app.level += 1
				self.app.game = None
				self.app.player_pos = [16, 16]
				pyxel.tilemaps[0].pset(11, 12, (0, 4))
				pyxel.tilemaps[0].pset(7, 9, (0, 3))
				pyxel.tilemaps[0].pset(8, 9, (1, 3))
				self.app.message = None
				self.app.message_y = None
				self.app.answer = None
				pyxel.camera(0, 0)
			return		
		elif self.tcnt > 0:
			self.tcnt -= 1
			return		
				
		number = -1
		if pyxel.btnp(pyxel.KEY_0):
			number = 0
		elif pyxel.btnp(pyxel.KEY_1):
			number = 1
		elif pyxel.btnp(pyxel.KEY_2):
			number = 2
		elif pyxel.btnp(pyxel.KEY_3):
			number = 3
		elif pyxel.btnp(pyxel.KEY_4):
			number = 4
		elif pyxel.btnp(pyxel.KEY_5):
			number = 5
		elif pyxel.btnp(pyxel.KEY_6):
			number = 6
		elif pyxel.btnp(pyxel.KEY_7):
			number = 7
		elif pyxel.btnp(pyxel.KEY_8):
			number = 8
		elif pyxel.btnp(pyxel.KEY_9):
			number = 9
		if number >= 0:
			self.index += 1
			if self.number[self.index] != number:
				self.game_over = False
				self.tcnt = 90
			elif self.index == len(self.number) - 1:
				self.tcnt = 90
				self.game_over = True
			else:
				self.tcnt = 45

	def draw1(self):	
		pyxel.text(3*8+256, 2*8+128, "Number Memorize Game", pyxel.COLOR_WHITE)
		pyxel.text(3*8+256, 14*8+128, "Please Press Enter Key", pyxel.COLOR_WHITE)
		
	def draw2(self):
		if self.display_num is not None:
			pyxel.text(8*8+256, 5*8+128, "{}".format(self.display_num), pyxel.COLOR_WHITE)
		elif self.index < len(self.number) - 1:
			pyxel.text(2*8+256, 2*8+128, "Please Memorize Number!!", pyxel.COLOR_WHITE)
		
	def draw3(self):
		if self.tcnt == 0:
			pyxel.text(3*8+256, 2*8+128, "Please Answer (0-9 Key)", pyxel.COLOR_WHITE)
		elif self.index >= 0:
			pyxel.text(7*8+256, 5*8+128, "{}".format(self.number[self.index]), pyxel.COLOR_WHITE)
			if self.game_over is None or self.game_over:
				pyxel.text(8*8+256, 5*8+128, "o", pyxel.COLOR_GREEN)
			else:
				pyxel.text(8*8+256, 5*8+128, "x", pyxel.COLOR_RED)
		if self.game_over is not None:
			if self.game_over:
				pyxel.text(3*8+256, 14*8+128, "You Win!! Level Up!!", pyxel.COLOR_DARK_BLUE)
			else:
				pyxel.text(3*8+256, 14*8+128, "You Lose!! Try Again!!", pyxel.COLOR_RED)

class LightsOut:
	def __init__(self, app):
		self.app = app
		pyxel.camera(48*8, 16*8)
		self.update = self.update1
		self.draw = self.draw1
		self.lights = [[True] * 5 for _ in range(5)]
		self.cnt = 25
		self.tcnt = 0
		
	def light_turn(self, x, y, turn):
		px = 48 + 3 + 2 * x
		py = 16 + 3 + 2 * y		
		if x == 0:
			tx = 0 if turn else 6
		elif x == 4:
			tx = 4 if turn else 10
		else:
			tx = 2 if turn else 8
		if y == 0:
			ty = 12
		elif y == 4:
			ty = 16
		else:
			ty = 14
		pyxel.tilemaps[0].pset(px, py, (tx, ty))
		pyxel.tilemaps[0].pset(px+1, py, (tx+1, ty))
		pyxel.tilemaps[0].pset(px, py+1, (tx, ty+1))
		pyxel.tilemaps[0].pset(px+1, py+1, (tx+1, ty+1))
		
	def update1(self):
		if pyxel.btnp(pyxel.KEY_RETURN):
			v = [[0] * 5 for _ in range(5)]
			while True:
				for y in range(5):
					for x in range(5):
						v[y][x] = pyxel.rndi(0, 1)
						self.lights[y][x] = v[y][x] == 1
				A, B, C, D, E = v[0][0], v[0][1], v[0][2], v[0][3], v[0][4]
				F, G, H, I, J = v[1][0], v[1][1], v[1][2], v[1][3], v[1][4]
				K, L, M, N, O = v[2][0], v[2][1], v[2][2], v[2][3], v[2][4]
				P, Q, R, S, T = v[3][0], v[3][1], v[3][2], v[3][3], v[3][4]
				U, V, W, X, Y = v[4][0], v[4][1], v[4][2], v[4][3], v[4][4]
			
				a = (B+C+D+F+H+J+K+L+N+O+P+R+T+V+W+X) % 2 == 0
				b = (A+C+E+F+H+J+P+R+T+U+W+Y) % 2 == 0
				if a and b:
					break 				
		
			for y in range(5):
				for x in range(5):
					if not self.lights[y][x]:
						self.cnt -= 1
						self.light_turn(x, y, False)
			self.update = self.update2
			self.draw = self.draw2
	
	def update2(self):
		if self.tcnt > 0:
			self.tcnt -= 1
			if self.tcnt == 0:
				self.app.game = None
				if self.cnt == 0:
					self.app.level += 1
				self.app.player_pos = [16, 16]
				pyxel.tilemaps[0].pset(11, 12, (0, 4))
				pyxel.tilemaps[0].pset(7, 9, (0, 3))
				pyxel.tilemaps[0].pset(8, 9, (1, 3))
				self.app.message = None
				self.app.message_y = None
				self.app.answer = None
				pyxel.camera(0, 0)
			return
		if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
			if pyxel.mouse_x // 8 == 14 and pyxel.mouse_y // 8 == 1:
				self.tcnt = 1
				return
			x = (pyxel.mouse_x - 3*8) // 16
			y = (pyxel.mouse_y - 3*8) // 16
			for dx, dy in ((0, 0),(-1, 0), (0, -1), (1, 0), (0, 1)):
				nx, ny = x + dx, y + dy
				if 0 <= nx < 5 and 0 <= ny < 5:
					self.lights[ny][nx] = not self.lights[ny][nx]
					self.light_turn(nx, ny, self.lights[ny][nx])
					self.cnt += 1 if self.lights[ny][nx] else -1
			if self.cnt == 0:
				self.tcnt = 90
	
	def draw1(self):
		pyxel.text(4*8+384+4, 2*8+128, "Lights Out Game", pyxel.COLOR_WHITE)
		pyxel.text(3*8+384, 14*8+128, "Please Press Enter Key", pyxel.COLOR_WHITE)
	
	def draw2(self):
		if self.cnt > 0:
			pyxel.text(4*8+384, 14*8+128, "Please Press Light", pyxel.COLOR_WHITE)
		else:
			pyxel.text(4*8+384, 14*8+128, "You Win!! Level Up!!", pyxel.COLOR_WHITE)
			
class Slot:
	def __init__(self, app):
		self.app = app
		pyxel.camera(64*8, 16*8)
		self.update = self.update1
		self.slot_pos = ((0, 3), (2, 3), (4, 3), (0, 5), (2, 5), (4, 5))
		self.slots = [pyxel.rndi(0, 5), pyxel.rndi(0, 5), pyxel.rndi(0, 5)]
		self.tcnt = 60
		self.game_over = None
	
	def update1(self):
		if pyxel.btnp(pyxel.KEY_RETURN):
			self.update = self.update2
			self.tcnt = 0
			
	def update2(self):
		if self.tcnt >= 60 and pyxel.btnp(pyxel.KEY_RETURN):
			self.update = self.update3
			self.tcnt = 0
			return
		self.tcnt += 1
		if self.tcnt % 5 == 0:
			self.slots[0] = (self.slots[0] + 1) % 6
			self.slots[1] = (self.slots[1] + 1) % 6
			self.slots[2] = (self.slots[2] + 1) % 6
			
	def update3(self):
		if self.tcnt >= 60 and pyxel.btnp(pyxel.KEY_RETURN):
			self.update = self.update4
			self.tcnt = 0
			return
		self.tcnt += 1
		if self.tcnt < 60 and self.tcnt % 10 == 0:
			self.slots[0] = (self.slots[0] + 1) % 6
		if self.tcnt % 5 == 0:
			self.slots[1] = (self.slots[1] + 1) % 6
			self.slots[2] = (self.slots[2] + 1) % 6
			
	def update4(self):
		if self.tcnt >= 60 and pyxel.btnp(pyxel.KEY_RETURN):
			self.update = self.update5
			self.tcnt = 0
			return
		self.tcnt += 1
		if self.tcnt < 60 and self.tcnt % 10 == 0:
			self.slots[1] = (self.slots[1] + 1) % 6
		if self.tcnt % 5 == 0:
			self.slots[2] = (self.slots[2] + 1) % 6
			
	def update5(self):
		self.tcnt += 1
		if self.tcnt < 60 and self.tcnt % 10 == 0:
			self.slots[2] = (self.slots[2] + 1) % 6
		if self.tcnt == 60:
			if self.slots[0] == self.slots[1] == self.slots[2]:
				if self.slots[0] == 5:
					self.game_over = 2
				else:
					self.game_over = 1
			else:
				self.game_over = 0
		if self.tcnt == 150:
			if self.game_over > 0:
				self.app.game = None
				if self.game_over == 1:
					self.app.level += 1
				else:
					self.app.level = 7
				self.app.player_pos = [16, 16]
				pyxel.tilemaps[0].pset(11, 12, (0, 4))
				pyxel.tilemaps[0].pset(7, 9, (0, 3))
				pyxel.tilemaps[0].pset(8, 9, (1, 3))
				self.app.message = None
				self.app.message_y = None
				self.app.answer = None
				pyxel.camera(0, 0)	
			else:
				self.game_over = None
				self.update = self.update1
		
	def draw(self):
		pyxel.text(5*8+512, 2*8+128, "SLOT MACHINE", pyxel.COLOR_WHITE)
		if self.game_over is None and self.tcnt >= 60:
			pyxel.text(3*8+512, 12*8+128, "Please Press Enter Key", pyxel.COLOR_WHITE)
		elif self.game_over == 0:
			pyxel.text(3*8+512, 12*8+128, "You Lose!! Try Ageain!!", pyxel.COLOR_RED)
		elif self.game_over == 1:
			pyxel.text(4*8+512, 12*8+128, "You Win!! Level Up!!", pyxel.COLOR_GREEN)
		elif self.game_over == 2:
			pyxel.text(2*8+512, 12*8+128, "Conguratulation!! Game Clear!!", pyxel.COLOR_WHITE)
		for i, j in enumerate(self.slots):
			pos = self.slot_pos[j]
			x = (64 + 5)*8 + i * 16
			y = (16 + 5)*8
			pyxel.blt(x, y, 1, pos[0]*8, pos[1]*8, 16, 16)

class DodgeBall:
	def __init__(self, app):
		self.app = app
		self.player_pos = [2*8+128, 6*8+128]
		self.enemy_pos = [12*8+128, 6*8+128]
		self.ball_pos = [11*8+128, 6*8+128]
		pyxel.camera(16*8, 16*8)
		self.game_over = None
		self.update = self.update1
		self.tcnt = 0
		self.throw = False
		self.waitcnt = 0
		self.start = False
		
	def update1(self):
		if pyxel.btnp(pyxel.KEY_RETURN):
			self.update = self.update2
			self.tcnt = 0
			self.waitcnt = pyxel.rndi(1, 5)*30
			self.start = True
			
	def update2(self):
		if pyxel.btnp(pyxel.KEY_UP, repeat=5):
			if self.player_pos[1] > 3*8+128:
				self.player_pos[1] -= 1*8
		elif pyxel.btnp(pyxel.KEY_DOWN, repeat=5):
			if self.player_pos[1] < 9*8+128:
				self.player_pos[1] += 1*8
		self.tcnt += 1
		if self.tcnt < self.waitcnt:
			return
		if self.tcnt % 2 == 0:
			if self.ball_pos[0] > 1*8+128:
				self.ball_pos[0] -= 1*8
				self.ball_pos[1] += pyxel.rndi(-1, 1)*8
			else:
				self.update = self.update3
				self.player_pos[1] = 6*8+128
				self.ball_pos = [4*8+128, 6*8+128]
				self.tcnt = 0
				self.throw = False
				return
		if self.player_pos[0] <= self.ball_pos[0] < self.player_pos[0]+16 and \
			self.player_pos[1] <= self.ball_pos[1] < self.player_pos[1]+16:
			self.game_over = False
			self.tcnt = 0
			self.update = self.update4
			
	def update3(self):
		if not self.throw and pyxel.btnp(pyxel.KEY_SPACE):
			self.throw = True
		if pyxel.btnp(pyxel.KEY_UP, repeat=5):
			if self.player_pos[1] > 3*8+128:
				self.player_pos[1] -= 1*8
				self.ball_pos[1] -= 1*8
		elif pyxel.btnp(pyxel.KEY_DOWN, repeat=5):
			if self.player_pos[1] < 9*8+128:
				self.player_pos[1] += 1*8
				self.ball_pos[1] += 1*8
		self.tcnt += 1
		if self.tcnt % 2 == 0:
			d = pyxel.rndi(-1, 1)*8
			if 3*8+128 < self.enemy_pos[1]+d < 9*8+128:
				 self.enemy_pos[1] += d
			if self.throw:
				if self.ball_pos[0] < 15*8+128:
					self.ball_pos[0] += 1*8
					self.ball_pos[1] += pyxel.rndi(-1, 1)*8
				else:
					self.update = self.update2
					self.player_pos[1] = 6*8+128
					self.enemy_pos[1] = 6*8+128
					self.ball_pos = [11*8+128, 6*8+128]
					self.tcnt = 0
					self.throw = False
					self.waitcnt = pyxel.rndi(1, 5)*30
					return
			if self.enemy_pos[0] <= self.ball_pos[0] < self.enemy_pos[0]+16 and \
				self.enemy_pos[1] <= self.ball_pos[1] < self.enemy_pos[1]+16:
				self.game_over = True
				self.tcnt = 0
				self.update = self.update4
	
	def update4(self):
		self.tcnt += 1
		if self.tcnt == 90:
			self.app.game = None
			if self.game_over:
				self.app.level += 1
			self.app.player_pos = [16, 16]
			pyxel.tilemaps[0].pset(11, 12, (0, 4))
			pyxel.tilemaps[0].pset(7, 9, (0, 3))
			pyxel.tilemaps[0].pset(8, 9, (1, 3))
			self.app.message = None
			self.app.message_y = None
			self.app.answer = None
			pyxel.camera(0, 0)
						
	def draw(self):
		pyxel.text(4*8+128, 2*8+128, "DODGE BALL GAME", pyxel.COLOR_WHITE)
		if self.game_over is not None: 
			if self.game_over:
				pyxel.text(4*8+128, 12*8+128, "You Win!! Level UP!!", pyxel.COLOR_DARK_BLUE)
			else:
				pyxel.text(3*8+128, 12*8+128, "You Lose!! Try Again!!", pyxel.COLOR_RED)
		else:
			if not self.start:
				pyxel.text(3*8+128, 12*8+128, "Please Press Enter Key", pyxel.COLOR_WHITE)
			elif self.update == self.update3 and not self.throw:
				pyxel.text(3*8+128, 12*8+128, "Please Press Space Key", pyxel.COLOR_WHITE)
		
		pyxel.blt(self.player_pos[0], self.player_pos[1], 1, 32, 8, 16, 16, pyxel.COLOR_WHITE)
		pyxel.blt(self.enemy_pos[0], self.enemy_pos[1], 1, 48, 8, 16, 16, pyxel.COLOR_WHITE)
		pyxel.blt(self.ball_pos[0], self.ball_pos[1], 1, 8, 0, 8, 8, pyxel.COLOR_WHITE)
		
class Fighter:
	def __init__(self, app):
		self.app = app
		pyxel.camera(80*8, 16*8)
		self.box = None
		self.player_pos = ((2+80)*8, (11+16)*8)
		self.enemy_pos = ((11+80)*8, (11+16)*8)
		self.player_hp = 10
		self.enemy_hp = 10
		self.turn = True
		self.update = self.update1
		self.tcnt = 0
		self.update = self.update1
		self.effect = None
		self.boxes = (((5+80)*8, (4+16)*8, 0), ((5+80)*8, (7+16)*8, 1), ((8+80)*8, (4+16)*8, 2), ((8+80)*8, (7+16)*8, 3))
		self.game_over = None
		
	def set_effect(self, item, level):
		if item == 0:
			if level == 0:
				self.effect = (-5, 0, 0) if self.turn else (0, -5, 0)
			elif level == 1:
				self.effect = (0, 0, 0)
			else:
				self.effect =  (0, -5, 0) if self.turn else (-5, 0, 0)
		elif item == 1:
			if level == 0:
				self.effect = (0, -2, 1) if self.turn else (-2, 0, 1)
			else:
				self.effect = (0, -1, 1) if self.turn else (-1, 0, 1)
		elif item == 2:
			if level == 0:
				self.effect = (2, 0, 2) if self.turn else (0, 2, 2)
			else:
				self.effect = (1, 0, 2) if self.turn else (0, 1, 2)
		else:
			if level == 0:
				self.effect = (0, 0, 3)
			elif level == 1:
				self.effect = (0, -2, 3) if self.turn else (-2, 0, 3)
			else:
				self.effect = (0, -4, 3) if self.turn else (-4, 0, 3)
		self.player_hp += self.effect[0]
		if self.player_hp < 0:
			self.player_hp = 0
		self.enemy_hp += self.effect[1]
		if self.enemy_hp < 0:
			self.enemy_hp = 0			
		
	def update1(self):
		x = (pyxel.mouse_x-5*8) // 8
		y = (pyxel.mouse_y-4*8) // 8
		if 0 <= x < 2 and 0 <= y < 2:
			self.box = self.boxes[0]
		elif 0 <= x < 2 and 3 <= y < 5:
			self.box = self.boxes[1]
		elif 3 <= x < 5 and 0 <= y < 2:
			self.box = self.boxes[2]
		elif 3 <= x < 5 and 3 <= y < 5:
			self.box = self.boxes[3]
		else:
			self.box = None
		if self.box is not None and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
			self.set_effect(self.box[2], pyxel.rndi(0,2))
			self.tcnt = 90
			self.update = self.update2
	
	def update2(self):
		self.tcnt -= 1
		if self.tcnt == 0:
			if self.player_hp == 0:
				self.game_over = False
			elif self.enemy_hp == 0:
				self.game_over = True
			if self.game_over is not None:
				self.update = self.update3
				self.tcnt = 90
				return
			self.effect = None
			self.box = None
			self.turn = not self.turn
			if self.turn:
				self.update = self.update1
			else:
				self.tcnt = 90
				select = pyxel.rndi(0,3)
				self.set_effect(select, pyxel.rndi(0,2))
				self.box = self.boxes[select]
				
	def update3(self):
		self.tcnt -= 1
		if self.tcnt == 0:
			self.app.game = None
			if self.game_over:
				self.app.level += 1
			self.app.player_pos = [16, 16]
			pyxel.tilemaps[0].pset(11, 12, (0, 4))
			pyxel.tilemaps[0].pset(7, 9, (0, 3))
			pyxel.tilemaps[0].pset(8, 9, (1, 3))
			self.app.message = None
			self.app.message_y = None
			self.app.answer = None
			pyxel.camera(0, 0)			
		
	def draw(self):
		pyxel.text(4*8+640, 2*8+128, "STREET FIGHTER", pyxel.COLOR_WHITE)
		if self.box is not None:
			pyxel.blt(self.box[0], self.box[1], 1, 64, 8, 16, 16)
		pyxel.blt((5+80)*8, (4+16)*8, 1, 48, 24, 16, 16, pyxel.COLOR_WHITE)
		pyxel.blt((8+80)*8, (4+16)*8, 1, 64, 24, 16, 16, pyxel.COLOR_WHITE)
		pyxel.blt((5+80)*8, (7+16)*8, 1, 48, 40, 16, 16, pyxel.COLOR_WHITE)
		pyxel.blt((8+80)*8, (7+16)*8, 1, 64, 40, 16, 16, pyxel.COLOR_WHITE)	
		pyxel.blt(self.player_pos[0], self.player_pos[1], 1, 32, 8, 16, 16, pyxel.COLOR_WHITE)
		pyxel.blt(self.enemy_pos[0], self.enemy_pos[1], 1, 48, 8, 16, 16, pyxel.COLOR_WHITE)
		items = ["BOMB", "FIST", "DUMBBELL", "PISTOL"]
		if self.game_over is not None:
			if self.game_over:
				pyxel.text(3*8+640, 13*8+128, "You Win!! Level Up!!", pyxel.COLOR_GREEN)
			else:
				pyxel.text(3*8+640, 13*8+128, "You Lose!! Try Again!!", pyxel.COLOR_RED)
		elif self.turn:
			pyxel.text(5*8+640, 11*8+128, "Your Turn", pyxel.COLOR_WHITE)
			if self.effect is None:
				pyxel.text(5*8+640, 12*8+128, "Press Item", pyxel.COLOR_WHITE)
		else:
			pyxel.text(5*8+640, 11*8+128, "Enemy Turn", pyxel.COLOR_WHITE)
		if self.game_over is None and self.effect is not None:
			pyxel.text(5*8+640, 12*8+128, "Use {}".format(items[self.effect[2]]), pyxel.COLOR_WHITE)
			if self.effect[0] == 0 and self.effect[1] == 0:
				pyxel.text(5*8+640, 13*8+128, "Nothing Happen!!", pyxel.COLOR_BLACK)
			elif self.effect[0] > 0:
				pyxel.blt((3+80)*8, (11+16)*8, 1, 24, 0, 8, 8, pyxel.COLOR_WHITE)
				pyxel.text(5*8+640, 13*8+128, "Your HP {} Up".format(self.effect[0]), pyxel.COLOR_GREEN)
			elif self.effect[0] < 0:
				pyxel.blt((3+80)*8, (11+16)*8, 1, 16, 0, 8, 8, pyxel.COLOR_WHITE)
				pyxel.text(5*8+640, 13*8+128, "Your HP {} Down".format(-self.effect[0]), pyxel.COLOR_RED)
			elif self.effect[1] > 0:
				pyxel.blt((12+80)*8, (11+16)*8, 1, 24, 0, 8, 8, pyxel.COLOR_WHITE)
				pyxel.text(5*8+640, 13*8+128, "Enemy HP {} Up".format(self.effect[1]), pyxel.COLOR_GREEN)
			elif self.effect[1] < 0:
				pyxel.blt((12+80)*8, (11+16)*8, 1, 16, 0, 8, 8, pyxel.COLOR_WHITE)
				pyxel.text(5*8+640, 13*8+128, "Enemy HP {} Down".format(self.effect[1]), pyxel.COLOR_RED)					
		pyxel.text(2*8+640, 14*8+128, "HP: {}".format(self.player_hp), pyxel.COLOR_BLACK)
		pyxel.text(11*8+640, 14*8+128, "HP: {}".format(self.enemy_hp), pyxel.COLOR_BLACK)

class App:
	def __init__(self, level=1):
		pyxel.init(128, 128)
		pyxel.mouse(True)
		pyxel.load("./my_resource.pyxres")
		self.player_pos = [16, 16]
		self.message = None
		self.message_y = None
		self.answer = None
		self.money = 100
		self.level = level
		self.game = None
		pyxel.run(self.update, self.draw)
		
	def update(self):
		if self.game is not None:
			self.game.update()
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
					if self.level == 1:
						self.game = Nyokki(self)
					elif self.level == 2:
						self.game = Memorize(self)
					elif self.level == 3:
						self.game = LightsOut(self)
					elif self.level == 4:
						self.game = Slot(self)
					elif self.level == 5:
						self.game = DodgeBall(self)
					elif self.level == 6:
						self.game = Fighter(self)
					else:
						self.game = None
				else:
					self.message = None
					self.answer = None
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
			self.message = ["Do you play game?", "> yes", " no "]
			self.answer = True
		
	def draw(self):
		pyxel.cls(0)
		pyxel.bltm(0, 0, 0, 0, 0, 768, 256)
		if self.game is not None:
			self.game.draw()
			return
		pyxel.blt(self.player_pos[0], self.player_pos[1], 1, 0, 0, 8, 8, 14)
		if self.level < 7:
			pyxel.text(48, 26, "Level {}".format(self.level), pyxel.COLOR_WHITE) 
		else:
			pyxel.text(32, 26, "Congratulation!!", pyxel.COLOR_YELLOW) 
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

App(3)
