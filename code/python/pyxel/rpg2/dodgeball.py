import pyxel
import game
import state

class DodgeBall(game.Game):
	class EnemyState(state.State):
		def __init__(self, game):
			self.game = game
			self.game.player_pos = [2*8, 6*8]
			self.game.enemy_pos = [12*8, 6*8]
			self.game.ball_pos = [11*8, 6*8]
			self.tcnt = 0
			self.waitcnt = pyxel.rndi(1, 5)*30
		def update(self):
			if pyxel.btnp(pyxel.KEY_UP, repeat=5):
				if self.game.player_pos[1] > 3*8:
					self.game.player_pos[1] -= 1*8
			elif pyxel.btnp(pyxel.KEY_DOWN, repeat=5):
				if self.game.player_pos[1] < 9*8:
					self.game.player_pos[1] += 1*8
			self.tcnt += 1
			if self.tcnt < self.waitcnt:
				return None
			if self.tcnt % 2 == 0:
				if self.game.ball_pos[0] > 1*8:
					self.game.ball_pos[0] -= 1*8
					self.game.ball_pos[1] += pyxel.rndi(-1, 1)*8
				else:
					return DodgeBall.PlayerState(self.game)
			if self.game.player_pos[0] <= self.game.ball_pos[0] < self.game.player_pos[0]+16 and \
				self.game.player_pos[1] <= self.game.ball_pos[1] < self.game.player_pos[1]+16:
				return state.GameOverState(False, 60, 5)
			return None
		def draw(self, xoffset, yoffset):
			self.game._draw(xoffset, yoffset)
			
	class PlayerState(state.State):
		def __init__(self, game):
			self.game = game
			self.game.player_pos = [2*8, 6*8]
			self.game.enemy_pos = [12*8, 6*8]
			self.game.ball_pos = [4*8, 6*8]	
			self.throw = False
			self.tcnt = 0
		def update(self):
			if not self.throw and pyxel.btnp(pyxel.KEY_SPACE):
				self.throw = True		
			if pyxel.btnp(pyxel.KEY_UP, repeat=5):
				if self.game.player_pos[1] > 3*8:
					self.game.player_pos[1] -= 1*8
					self.game.ball_pos[1] -= 1*8
			elif pyxel.btnp(pyxel.KEY_DOWN, repeat=5):
				if self.game.player_pos[1] < 9*8:
					self.game.player_pos[1] += 1*8
					self.game.ball_pos[1] += 1*8
			self.tcnt += 1
			if self.tcnt % 2 == 0:
				d = pyxel.rndi(-1, 1)*8
				if 3*8 < self.game.enemy_pos[1]+d < 9*8:
					self.game.enemy_pos[1] += d
				if self.throw:
					if self.game.ball_pos[0] < 15*8:
						self.game.ball_pos[0] += 1*8
						self.game.ball_pos[1] += pyxel.rndi(-1, 1)*8
					else:
						return DodgeBall.EnemyState(self.game)
				if self.game.enemy_pos[0] <= self.game.ball_pos[0] < self.game.enemy_pos[0]+16 and \
					self.game.enemy_pos[1] <= self.game.ball_pos[1] < self.game.enemy_pos[1]+16:
					return state.GameOverState(True, 60, 5, col=(pyxel.COLOR_DARK_BLUE, pyxel.COLOR_RED))
			return None
		def draw(self, xoffset, yoffset):
			pyxel.text(3*8+xoffset, 12*8+yoffset, "Please Press Space Key", pyxel.COLOR_WHITE)
			self.game._draw(xoffset, yoffset)			
	
	def __init__(self):
		super().__init__(16*8, 16*8, state.TitleState("Dodge Ball", DodgeBall.EnemyState(self), self._draw))
		self.player_pos = [2*8, 6*8]
		self.enemy_pos = [12*8, 6*8]
		self.ball_pos = [11*8, 6*8]
	def _draw(self, xoffset, yoffset):
		pyxel.blt(self.player_pos[0]+xoffset, self.player_pos[1]+yoffset, 1, 32, 8, 16, 16, pyxel.COLOR_WHITE)
		pyxel.blt(self.enemy_pos[0]+xoffset, self.enemy_pos[1]+yoffset, 1, 48, 8, 16, 16, pyxel.COLOR_WHITE)
		pyxel.blt(self.ball_pos[0]+xoffset, self.ball_pos[1]+yoffset, 1, 8, 0, 8, 8, pyxel.COLOR_WHITE)		
	def __str__(self):
		return "Main"
