import pyxel
import game
import state
import random

class Puzzle15(game.Game):
	class Tile:
		def __init__(self, x, y):
			self.tile = [[None] * 4 for _ in range(4)]
			self.x = x
			self.y = y
			self.id = y*4+x
			for i in range(4):
				for j in range(4):
					self.tile[i][j] = pyxel.tilemaps[0].pget(x*4 + j, y*4 + i)
			self.isMovable = False
		def move(self, cb):
			if self.isMovable:
				for i in range(4):
					for j in range(4):
						pyxel.tilemaps[0].pset(cb.x*4 + j, cb.y*4 + i, self.tile[i][j])
						pyxel.tilemaps[0].pset(self.x*4 + j, self.y*4 + i, cb.tile[i][j])
				self.id, self.tile, cb.id, cb.tile = cb.id, cb.tile, self.id, self.tile
		def __str__(self):
			return "({}, {}, {}, {})".format(self.id, self.x, self.y, self.isMovable)
				
	class PlayState(state.State):
		def __init__(self, game):
			self.game = game
			self.tiles = [[None] * 4 for _ in range(4)]			
			for y in range(4):
				for x in range(4):
					self.tiles[y][x] = Puzzle15.Tile(x, y)
			self.empty = self.tiles[3][3]
			for y in range(4):
				for x in range(4):
					self.empty.tile[y][x] = (0, 6)			
			self.start = False
		def setMovable(self, empty=None):
			if empty is not None:
				ex, ey = empty.x, empty.y
			else:
				ex, ey = -1, -1
			self.randlist.clear()
			for y in range(4):
				for x in range(4):
					self.tiles[y][x].isMovable = False
			for y in range(4):
				for x in range(4):
					tile = self.tiles[y][x]
					if tile.id == 15:
						self.empty = tile
						if x > 0 and (ex != x-1 or ey != y):
							self.tiles[y][x-1].isMovable = True
							self.randlist.append(self.tiles[y][x-1])
						if x < 3 and (ex != x+1 or ey != y):
							self.tiles[y][x+1].isMovable = True
							self.randlist.append(self.tiles[y][x+1])
						if y > 0 and (ex != x or ey != y-1):
							self.tiles[y-1][x].isMovable = True
							self.randlist.append(self.tiles[y-1][x])
						if y < 3 and (ex != x or ey != y+1):
							self.tiles[y+1][x].isMovable = True
							self.randlist.append(self.tiles[y+1][x])
						break
		def checkComplete(self):
			for y in range(4):
				for x in range(4):
					if self.tiles[y][x].id % 4 != x or self.tiles[y][x].id // 4 != y:
						return False
			return True
		def update(self):
			if not self.start:
				self.randlist = []
				self.setMovable(self.empty)
				for i in range(50):
					random.choice(self.randlist).move(self.empty)
					self.setMovable(self.empty)
				self.start = True
			if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
				x, y = pyxel.mouse_x // 32, pyxel.mouse_y // 32
				tile = self.tiles[y][x]
				tile.move(self.empty)
				self.setMovable()
				if self.checkComplete():
					for y in range(4):
						for x in range(4):
							pyxel.tilemaps[0].pset(3*4+x, 3*4+y, self.game.save[y][x])
					return state.GameOverState(True, 90, 8)
			return None
		def draw(self, xoffset, yoffset):
			pass
	def __init__(self):
		self.save = [[None] * 4 for _ in range(4)]
		for y in range(4):
			for x in range(4):
				self.save[y][x] = pyxel.tilemaps[0].pget(3*4+x, 3*4+y)
		super().__init__(0, 0, state.TitleState("Puzzle15 Game", state.WaitState(60, Puzzle15.PlayState(self))))
	def __str__(self):
		return "Puzzle15"
		
