import pyxel
import game
import state

class Nyokki(game.Game):
	class PlayState(state.State):
		def __init__(self, game):
			self.game = game
			self.player_num = -1
			self.num = 0
			self.no = 0
			self.tcnt = 0
			self.sec = -4
			self.game_over = None
		def update(self):
			if self.sec > -1 and self.player_num < 0 and pyxel.btnp(pyxel.KEY_SPACE):
				self.player_num = self.sec+1
			self.tcnt += 1
			if self.game_over is not None:
				if self.tcnt == 90:
					return state.GameOverState(self.game_over, 90, 1, self.game._draw, col=(pyxel.COLOR_DARK_BLUE, pyxel.COLOR_RED))
				return None
			if self.tcnt % 30 == 0:
				self.sec += 1
				if self.sec < 0:
					return None
				if self.sec == 16:
					self.game_over = False
					self.tcnt = 0
					return None
				if self.sec == self.player_num or self.sec in [enemy[2] for enemy in self.game.enemies]:
					self.no += 1
					cnt = 0
					if self.sec == self.player_num:
						self.num = self.no
						cnt += 1
					for enemy in self.game.enemies:
						if enemy[2] == self.sec:
							enemy[3] = self.no
							cnt += 1
					if cnt > 1:
						self.game_over = self.sec != self.player_num
						self.tcnt = 0
						return None
					else:
						if self.sec == self.player_num:
							self.game_over = True
						elif all([enemy[3] != 0 for enemy in self.game.enemies]):
							self.game_over = False
						self.tcnt = 0
						return None
			return None
		def draw(self, xoffset, yoffset):
			pyxel.text(7*8+4+xoffset, 10+xoffset, "{:2d}".format(self.sec+1), pyxel.COLOR_LIGHT_BLUE if self.sec >= -1 else pyxel.COLOR_RED)
			for enemy in self.game.enemies:
				if enemy[3] > 0:
					pyxel.text(enemy[0]+xoffset-8, enemy[1]+yoffset-8, "{} Nyokki!".format(enemy[3]), pyxel.COLOR_WHITE)
					pyxel.blt(enemy[0]+xoffset, enemy[1]+yoffset, 1, 0, 8, 16, 16, pyxel.COLOR_WHITE)
				else:
					pyxel.blt(enemy[0]+xoffset, enemy[1]+yoffset, 1, 16, 8, 16, 16, pyxel.COLOR_WHITE)
			if self.player_num >= 0 and self.num > 0:
				pyxel.text(7*8+xoffset-8, 11*8+yoffset-8, "{} Nyokki!".format(self.num), pyxel.COLOR_WHITE)
				pyxel.blt(7*8+xoffset, 11*8+yoffset, 1, 0, 8, 16, 16, pyxel.COLOR_WHITE)
			else:
				pyxel.blt(7*8+xoffset, 11*8+yoffset, 1, 16, 8, 16, 16, pyxel.COLOR_WHITE)
			if self.sec >= -1 and self.player_num < 0:
				pyxel.text(2*8+xoffset, 14*8+yoffset, "Please Press SPACE Key", pyxel.COLOR_BLACK)
				
	def __init__(self):
		super().__init__(16*8, 16*8, state.TitleState("Nyokki", Nyokki.PlayState(self), self._draw))
		self.randlist = []
		self.enemies = [[2*8, 3*8, self.getRandom(), 0],
			[7*8, 3*8, self.getRandom(), 0],
			[12*8, 3*8, self.getRandom(), 0],
			[2*8, 7*8, self.getRandom(), 0],
			[7*8, 7*8, self.getRandom(), 0],
			[12*8, 7*8, self.getRandom(), 0]]
	def getRandom(self):
		while True:
			i = pyxel.rndi(0, 15)
			if i not in self.randlist:
				self.randlist.append(i)
				return i
	def _draw(self, xoffset, yoffset):
		for enemy in self.enemies:
			pyxel.blt(enemy[0]+xoffset, enemy[1]+yoffset, 1, 16, 8, 16, 16, pyxel.COLOR_WHITE)
		pyxel.blt(7*8+xoffset, 11*8+yoffset, 1, 16, 8, 16, 16, pyxel.COLOR_WHITE)
		
	def __str__(self):
		return "Nyokki"
