import pyxel
import game
import state

class Fighter(game.Game):
	class PlayerState(state.State):
		def __init__(self, game):
			self.game = game
		def update(self):
			self.game.effect = None
			self.game.box = None
			if self.game.player_hp == 0:
				return state.GameOverState(False, 90, 6, self.game._draw)
			elif self.game.enemy_hp == 0:
				return state.GameOverState(True, 90, 6, self.game._draw)
			x = (pyxel.mouse_x-5*8) // 8
			y = (pyxel.mouse_y-4*8) // 8
			if 0 <= x < 2 and 0 <= y < 2:
				self.game.box = self.game.boxes[0]
			elif 0 <= x < 2 and 3 <= y < 5:
				self.game.box = self.game.boxes[1]
			elif 3 <= x < 5 and 0 <= y < 2:
				self.game.box = self.game.boxes[2]
			elif 3 <= x < 5 and 3 <= y < 5:
				self.game.box = self.game.boxes[3]
			else:
				self.game.box = None
			if self.game.box is not None and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
				self.game.set_effect(True, self.game.box[2], pyxel.rndi(0,2))
				return state.WaitState(90, Fighter.EnemyState(self.game), self._draw)
			return None
		def draw(self, xoffset, yoffset):
			pyxel.text(5*8+xoffset, 11*8+yoffset, "Your Turn", pyxel.COLOR_WHITE)
			pyxel.text(5*8+xoffset, 12*8+yoffset, "Press Item", pyxel.COLOR_WHITE)
			self.game._draw(xoffset, yoffset)
			pyxel.text(2*8+xoffset, 14*8+yoffset, "HP: {}".format(self.game.player_hp), pyxel.COLOR_BLACK)
			pyxel.text(11*8+xoffset, 14*8+yoffset, "HP: {}".format(self.game.enemy_hp), pyxel.COLOR_BLACK)
		def _draw(self, xoffset, yoffset):
			self.game._draw(xoffset, yoffset)
			self.game.draw_effect(xoffset, yoffset)
			pyxel.text(2*8+xoffset, 14*8+yoffset, "HP: {}".format(self.game.player_hp), pyxel.COLOR_BLACK)
			pyxel.text(11*8+xoffset, 14*8+yoffset, "HP: {}".format(self.game.enemy_hp), pyxel.COLOR_BLACK)
	class EnemyState(state.State):
		def __init__(self, game):
			self.game = game
			self.tcnt = 60
		def update(self):
			self.game.effect = None
			self.game.box = None
			if self.game.player_hp == 0:
				return state.GameOverState(False, 90, 6, self.game._draw)
			elif self.game.enemy_hp == 0:
				return state.GameOverState(True, 90, 6, self.game._draw)
			self.tcnt -= 1
			if self.tcnt == 0:
				select = pyxel.rndi(0,3)
				self.game.set_effect(False, select, pyxel.rndi(0,2))
				self.game.box = self.game.boxes[select]
				return state.WaitState(90, Fighter.PlayerState(self.game), self._draw)
			return None
		def draw(self, xoffset, yoffset):
			pyxel.text(5*8+xoffset, 11*8+yoffset, "Enemy Turn", pyxel.COLOR_WHITE)
			self.game._draw(xoffset, yoffset)
			self.game.draw_effect(xoffset, yoffset)	
			pyxel.text(2*8+xoffset, 14*8+yoffset, "HP: {}".format(self.game.player_hp), pyxel.COLOR_BLACK)
			pyxel.text(11*8+xoffset, 14*8+yoffset, "HP: {}".format(self.game.enemy_hp), pyxel.COLOR_BLACK)
		def _draw(self, xoffset, yoffset):
			self.game._draw(xoffset, yoffset)
			self.game.draw_effect(xoffset, yoffset)
			pyxel.text(2*8+xoffset, 14*8+yoffset, "HP: {}".format(self.game.player_hp), pyxel.COLOR_BLACK)
			pyxel.text(11*8+xoffset, 14*8+yoffset, "HP: {}".format(self.game.enemy_hp), pyxel.COLOR_BLACK)	
					 
	def __init__(self):
		super().__init__(80*8, 16*8, state.TitleState("Dodge Ball", Fighter.PlayerState(self), self._draw))
		self.box = None
		self.player_pos = (2*8, 11*8)
		self.enemy_pos = (11*8, 11*8)
		self.player_hp = 10
		self.enemy_hp = 10
		self.effect = None
		self.boxes = ((5*8, 4*8, 0), (5*8, 7*8, 1), (8*8, 4*8, 2), (8*8, 7*8, 3))
	def set_effect(self, turn, item, level):
		if item == 0:
			if level == 0:
				self.effect = (-5, 0, 0) if turn else (0, -5, 0)
			elif level == 1:
				self.effect = (0, 0, 0)
			else:
				self.effect =  (0, -5, 0) if turn else (-5, 0, 0)
		elif item == 1:
			if level == 0:
				self.effect = (0, -2, 1) if turn else (-2, 0, 1)
			else:
				self.effect = (0, -1, 1) if turn else (-1, 0, 1)
		elif item == 2:
			if level == 0:
				self.effect = (2, 0, 2) if turn else (0, 2, 2)
			else:
				self.effect = (1, 0, 2) if turn else (0, 1, 2)
		else:
			if level == 0:
				self.effect = (0, 0, 3)
			elif level == 1:
				self.effect = (0, -2, 3) if turn else (-2, 0, 3)
			else:
				self.effect = (0, -4, 3) if turn else (-4, 0, 3)
		self.player_hp += self.effect[0]
		if self.player_hp < 0:
			self.player_hp = 0
		self.enemy_hp += self.effect[1]
		if self.enemy_hp < 0:
			self.enemy_hp = 0
	def _draw(self, xoffset, yoffset):
		if self.box is not None:
			pyxel.blt(self.box[0]+xoffset, self.box[1]+yoffset, 1, 64, 8, 16, 16)
		pyxel.blt(5*8+xoffset, 4*8+yoffset, 1, 48, 24, 16, 16, pyxel.COLOR_WHITE)
		pyxel.blt(8*8+xoffset, 4*8+yoffset, 1, 64, 24, 16, 16, pyxel.COLOR_WHITE)
		pyxel.blt(5*8+xoffset, 7*8+yoffset, 1, 48, 40, 16, 16, pyxel.COLOR_WHITE)
		pyxel.blt(8*8+xoffset, 7*8+yoffset, 1, 64, 40, 16, 16, pyxel.COLOR_WHITE)	
		pyxel.blt(self.player_pos[0]+xoffset, self.player_pos[1]+yoffset, 1, 32, 8, 16, 16, pyxel.COLOR_WHITE)
		pyxel.blt(self.enemy_pos[0]+xoffset, self.enemy_pos[1]+yoffset, 1, 48, 8, 16, 16, pyxel.COLOR_WHITE)
	def draw_effect(self, xoffset, yoffset):
		if self.effect is not None:
			items = ["BOMB", "FIST", "DUMBBELL", "PISTOL"]	
			pyxel.text(5*8+xoffset, 12*8+yoffset, "Use {}".format(items[self.effect[2]]), pyxel.COLOR_WHITE)
			if self.effect[0] == 0 and self.effect[1] == 0:
				pyxel.text(5*8+xoffset, 13*8+yoffset, "Nothing Happen!!", pyxel.COLOR_BLACK)
			elif self.effect[0] > 0:
				pyxel.blt(3*8+xoffset, 11*8+yoffset, 1, 24, 0, 8, 8, pyxel.COLOR_WHITE)
				pyxel.text(5*8+xoffset, 13*8+yoffset, "Your HP {} Up".format(self.effect[0]), pyxel.COLOR_GREEN)
			elif self.effect[0] < 0:
				pyxel.blt(3*8+xoffset, 11*8+yoffset, 1, 16, 0, 8, 8, pyxel.COLOR_WHITE)
				pyxel.text(5*8+xoffset, 13*8+yoffset, "Your HP {} Down".format(-self.effect[0]), pyxel.COLOR_RED)
			elif self.effect[1] > 0:
				pyxel.blt(12*8+xoffset, 11*8+yoffset, 1, 24, 0, 8, 8, pyxel.COLOR_WHITE)
				pyxel.text(5*8+xoffset, 13*8+yoffset, "Enemy HP {} Up".format(self.effect[1]), pyxel.COLOR_GREEN)
			elif self.effect[1] < 0:
				pyxel.blt(12*8+xoffset, 11*8+yoffset, 1, 16, 0, 8, 8, pyxel.COLOR_WHITE)
				pyxel.text(5*8+xoffset, 13*8+yoffset, "Enemy HP {} Down".format(self.effect[1]), pyxel.COLOR_RED)	
	def __str__(self):
		return "Fighter"
