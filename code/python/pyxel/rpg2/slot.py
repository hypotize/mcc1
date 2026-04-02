import pyxel
import game
import state

class Slot(game.Game):
	class PlayState(state.State):
		def __init__(self, game):
			self.game = game
			self.tcnt = 0
		def update(self):
			self.tcnt += 1
			if pyxel.btnp(pyxel.KEY_SPACE):
				return Slot.PauseState(self.game)
			if self.tcnt % 5 == 0:
				if self.game.index == 0:
					self.game.slots[0] = (self.game.slots[0] + 1) % 6
				if self.game.index <= 1:
					self.game.slots[1] = (self.game.slots[1] + 1) % 6
				self.game.slots[2] = (self.game.slots[2] + 1) % 6
			return None
		def draw(self, xoffset, yoffset):
			pyxel.text(3*8+xoffset, 12*8+yoffset, "Please Press Space Key", pyxel.COLOR_WHITE)
			self.game._draw(xoffset, yoffset)
	class PauseState(state.State):
		def __init__(self, game):
			self.game = game
			self.tcnt = 0
		def update(self):
			self.tcnt += 1
			if self.tcnt >= 60:
				self.game.index += 1
				if self.game.index == 3:
					if self.game.slots[0] == self.game.slots[1] == self.game.slots[2]:
						if self.game.slots[0] == 5:
							return state.GameOverState(True, 60, 9, self.game._draw, 2*8)
						else:
							return state.GameOverState(True, 60, 4, self.game._draw, 2*8)
					else:
						return state.GameOverState(False, 60, 4, self.game._draw, 2*8)
				return Slot.PlayState(self.game)
			if self.tcnt < 60 and self.tcnt % 10 == 0:
				if self.game.index == 0:
					self.game.slots[0] = (self.game.slots[0] + 1) % 6
				elif self.game.index == 1:
					self.game.slots[1] = (self.game.slots[1] + 1) % 6
				else:
					self.game.slots[2] = (self.game.slots[2] + 1) % 6
			if self.tcnt % 5 == 0:
				if self.game.index < 1:
					self.game.slots[1] = (self.game.slots[1] + 1) % 6
				if self.game.index < 2:
					self.game.slots[2] = (self.game.slots[2] + 1) % 6
			return None
		def draw(self, xoffset, yoffset):
			self.game._draw(xoffset, yoffset)		
			
	def __init__(self):
		super().__init__(64*8, 16*8, state.TitleState("Slot Machine", Slot.PlayState(self), self._draw))
		self.slot_pos = ((0, 3), (2, 3), (4, 3), (0, 5), (2, 5), (4, 5))
		self.slots = [pyxel.rndi(0, 5), pyxel.rndi(0, 5), pyxel.rndi(0, 5)]
		self.index = 0
	def _draw(self, xoffset, yoffset):
		for i, j in enumerate(self.slots):
			pos = self.slot_pos[j]
			x = 5*8 + i*16 + xoffset
			y = 5*8 + yoffset
			pyxel.blt(x, y, 1, pos[0]*8, pos[1]*8, 16, 16)
	def __str__(self):
		return "Slot"
	
