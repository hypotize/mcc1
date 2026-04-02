import pyxel
import game
import state

class Memorize(game.Game):
	class DisplayState(state.WaitState):
		def __init__(self, game):
			super().__init__(60, state.WaitState(60, self, game.draw_memorize))
			self.game = game
			game.display_num = game.number[game.index]
		def update(self):
			rv = super().update()
			if rv is not None:
				self.game.index += 1
				if self.game.index == len(self.game.number):
					return state.WaitState(60, Memorize.InputState(self.game))
				self.game.display_num = self.game.number[self.game.index]
				rv.waittime = 60
				rv.state.waittime = 60
			return rv
		def draw(self, xoffset, yoffset):
			pyxel.text(8*8+xoffset, 5*8+yoffset, "{}".format(self.game.display_num), pyxel.COLOR_WHITE)
	class InputState(state.State):
		def __init__(self, game):
			self.game = game
			game.index = -1
		def update(self):
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
				self.game.index += 1
				if self.game.number[self.game.index] != number:
					self.same = False
					return state.GameOverState(False, 90, 2, self._draw)
				elif self.game.index == len(self.game.number) - 1:
					self.same = True
					return state.GameOverState(True, 90, 2, self._draw, col=(pyxel.COLOR_DARK_BLUE, pyxel.COLOR_RED))
				else:
					self.same = True
					return state.WaitState(60, self, self._draw)
		def draw(self, xoffset, yoffset):
			pyxel.text(3*8+xoffset, 2*8+yoffset, "Please Answer (0-9 Key)", pyxel.COLOR_WHITE)
		def _draw(self, xoffset, yoffset):
			pyxel.text(7*8+xoffset, 5*8+yoffset, "{}".format(self.game.number[self.game.index]), pyxel.COLOR_WHITE)
			if self.same:
				pyxel.text(8*8+xoffset, 5*8+yoffset, "o", pyxel.COLOR_GREEN)
			else:
				pyxel.text(8*8+xoffset, 5*8+yoffset, "x", pyxel.COLOR_RED)			
				
	def __init__(self):
		self.number = []
		for _ in range(7):
			self.number.append(pyxel.rndi(0, 9))
		self.index = 0
		self.display_num = None
		super().__init__(32*8, 16*8, state.TitleState("Memorize Number Game", state.WaitState(60, Memorize.DisplayState(self), self.draw_memorize)))
	def draw_memorize(self, xoffset, yoffset):
		pyxel.text(2*8+256, 2*8+128, "Please Memorize Number!!", pyxel.COLOR_WHITE)
	def __str__(self):
		return "Memorize"
		
