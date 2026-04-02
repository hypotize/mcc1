import pyxel
import state
import game
import nyokki
import memorize
import lightsout
import slot
import dodgeball
import fighter
import typinggame
import puzzle15
import concentration

class Main(game.Game):
	class CommonState(state.State):
		def __init__(self, pos, level, event_check):
			self.player_pos = pos
			self.level = level
			self.event_check = event_check
			self.game = None
			self.state = None
		
		def update(self):
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
			return self.state

		def move_check(self, x, y):
			if pyxel.tilemaps[0].pget(x//8, y//8)[1] == 0:
				return True
			self.event_check(x, y)
			return False
			
		def draw(self, xoffset, yoffset):
			pyxel.blt(self.player_pos[0], self.player_pos[1], 1, 0, 0, 8, 8, 14)
			
	class FieldState(CommonState):
		def __init__(self, level):
			super().__init__([16, 16], level, self._event_check)
			pyxel.camera(0, 0)
		def _event_check(self, x, y):
			t = pyxel.tilemaps[0].pget(x//8, y//8)
			if t == (0, 4):
				pyxel.tilemaps[0].pset(11, 12, (1, 4))
				pyxel.tilemaps[0].pset(7, 9, (2, 0))
				pyxel.tilemaps[0].pset(8, 9, (3, 0))
			elif t == (2, 3) or t == (3, 3):
				self.state = Main.RoomState(self.level)
		def draw(self, xoffset, yoffset):
			super().draw(xoffset, yoffset)
			if self.level < 10:
				pyxel.text(48, 26, "Level {}".format(self.level), pyxel.COLOR_WHITE) 
			else:
				pyxel.text(32, 26, "Congratulation!!", pyxel.COLOR_YELLOW) 			
				
	class RoomState(CommonState):
		def __init__(self, level):
			super().__init__([7*8, 22*8], level, self._event_check)
			self.message = None
			self.answer = None
			pyxel.camera(0, 16*8)
		def _event_check(self, x, y):
			t = pyxel.tilemaps[0].pget(x//8, y//8)
			if t == (4, 3) or t == (5, 3):
				self.state = Main.FieldState(self.level)
			elif t == (4, 5):
				self.message = ["Do you play next game?", "> yes", " no "]
				self.answer = True
		def update(self):
			if self.message is not None and self.answer is not None:
				if pyxel.btnp(pyxel.KEY_DOWN):
					if type(self.answer) != bool:
						if self.answer < 9:
							self.answer += 1
							self.message[1] = "> {}".format(self.answer)
					elif self.answer:
						self.answer = False
						self.message[1] = "  yes"
						self.message[2] = "> no "
				elif pyxel.btnp(pyxel.KEY_UP):
					if type(self.answer) != bool:
						if self.answer > 1:
							self.answer -= 1
							self.message[1] = "> {}".format(self.answer)
					elif not self.answer:
						self.answer = True
						self.message[1] = "> yes"
						self.message[2] = "  no "
				elif pyxel.btnp(pyxel.KEY_RETURN):
					if type(self.answer) != bool:
						self.level = self.answer
						self.answer = True
					if self.answer:
						if self.level == 1:
							App.set_game(nyokki.Nyokki())
						elif self.level == 2:
							App.set_game(memorize.Memorize())
						elif self.level == 3:
							App.set_game(lightsout.LightsOut())
						elif self.level == 4:
							App.set_game(slot.Slot())
						elif self.level == 5:
							App.set_game(dodgeball.DodgeBall())
						elif self.level == 6:
							App.set_game(fighter.Fighter())
						elif self.level == 7:
							App.set_game(typinggame.TypingGame())
						elif self.level == 8:
							App.set_game(puzzle15.Puzzle15())
						elif self.level == 9:
							App.set_game(concentration.Concentration())
						else:
							App.set_game(None)
					else:
						self.message = ["Do you play game?", "> 1"]
						self.answer = 1
				return None
			return super().update()
		def draw(self, xoffset, yoffset):
			if self.message is not None:
				cnt = len(self.message)		
				l = max([len(x) for x in self.message]) * 4 + 8
				pyxel.rect(128 - l, 208, l, 10*cnt, pyxel.COLOR_BLACK)
				pyxel.rectb(128 - l, 208, l, 10*cnt, pyxel.COLOR_WHITE)
				i = 0
				for text in self.message:
					l = len(text) * 4 + 8
					pyxel.text(128 - l + 4, 208 + 2 + i * 10, text, pyxel.COLOR_WHITE)
					i += 1	
			super().draw(xoffset, yoffset)

	def __init__(self, level):
		super().__init__(0, 0, Main.FieldState(level))
		pyxel.tilemaps[0].pset(11, 12, (0, 4))
		pyxel.tilemaps[0].pset(7, 9, (0, 3))
		pyxel.tilemaps[0].pset(8, 9, (1, 3))
		
	def __str__(self):
		return "Main"
		
class App:
	game = None
	@classmethod
	def set_game(cls, game):
		App.game = game
	def __init__(self, level=1):
		pyxel.init(128, 128)
		pyxel.mouse(True)
		pyxel.load("./my_resource.pyxres")
		App.set_game(Main(level))
		pyxel.run(self.update, self.draw)
	def update(self):
		if App.game is not None:
			level = App.game.update()
			if level is not None:
				App.set_game(Main(level))
				
	def draw(self):
		if App.game is not None:
			App.game.draw()

if __name__ == "__main__":
	App()
			
		
