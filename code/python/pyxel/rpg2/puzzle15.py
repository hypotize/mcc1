import pyxel
import game
import state
import random

class Puzzle15(game.Game):
	class Tile:
		EMPTY = 15
		def __init__(self, x=None, y=None):
			self.isMovable = False
			self.tile = [[None] * 4 for _ in range(4)]
			if x == None and y == None:
				self.x = 3
				self.y = 3
				self.id = Puzzle15.Tile.EMPTY
				for y in range(4):
					for x in range(4):
						self.tile[y][x] = (0, 6)	
			else:
				self.x = x
				self.y = y
				self.id = y*4+x
				for i in range(4):
					for j in range(4):
						self.tile[i][j] = pyxel.tilemaps[0].pget(x*4 + j, y*4 + i)
		def set(self, x, y):
			for i in range(4):
				for j in range(4):
					pyxel.tilemaps[0].pset(x*4 + j, y*4 + i, self.tile[i][j])
		def __str__(self):
			return "({}, {}, {}, {})".format(self.id, self.x, self.y, self.isMovable)
				
	class PlayState(state.State):
		def __init__(self, game):
			self.game = game
			self.tiles = [[None] * 4 for _ in range(4)]	
			self.arr = []	
			for y in range(4):
				for x in range(4):
					self.arr.append(Puzzle15.Tile(x, y))
			self.save, self.arr[15] = self.arr[15], Puzzle15.Tile()
			self.empty = None
			self.start = False
		def setMovable(self):
			for y in range(4):
				for x in range(4):
					if self.tiles[y][x].id == Puzzle15.Tile.EMPTY:
						self.tiles[y][x].isMovable = False
						self.empty = (x, y)
						continue
					if y > 0 and self.tiles[y-1][x].id == Puzzle15.Tile.EMPTY:
						self.tiles[y][x].isMovable = True
					elif y < 3 and self.tiles[y+1][x].id == Puzzle15.Tile.EMPTY:
						self.tiles[y][x].isMovable = True
					elif x > 0 and self.tiles[y][x-1].id == Puzzle15.Tile.EMPTY:
						self.tiles[y][x].isMovable = True
					elif x < 3 and self.tiles[y][x+1].id == Puzzle15.Tile.EMPTY:
						self.tiles[y][x].isMovable = True
					else:
						self.tiles[y][x].isMovable = False
		def checkComplete(self):
			for y in range(4):
				for x in range(4):
					if self.tiles[y][x].x != x or self.tiles[y][x].y != y:
						return False
			return True
		def countInversions(self):
			inversions = 0
			for i in range(16):
				if self.arr[i].id == Puzzle15.Tile.EMPTY:
					continue
				for j in range(i+1, 16):
					if self.arr[j].id == Puzzle15.Tile.EMPTY:
						continue
					if self.arr[i].id > self.arr[j].id:
						inversions += 1
			return inversions
		def isSolvable(self):
			inversions = self.countInversions()
			emptyIndex = [i for i, x in enumerate(self.arr) if x.id == Puzzle15.Tile.EMPTY][0]
			emptyRowFromBottom = 4 - (emptyIndex // 4)
			if emptyRowFromBottom % 2 == 0:
				return inversions % 2 == 1
			else:
				return inversions % 2 == 0
		def update(self):
			if not self.start:
				while True:
					random.shuffle(self.arr)
					if self.isSolvable():
						break
				for y in range(4):
					for x in range(4):
						tile = self.arr.pop(0)
						self.tiles[y][x] = tile
						tile.set(x, y)
				self.setMovable() 
				self.start = True
			if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
				x, y = pyxel.mouse_x // 32, pyxel.mouse_y // 32
				if x < 0 or x > 3 or y < 0 or y > 3:
					return None
				if not self.tiles[y][x].isMovable:
					return None
				ex, ey = self.empty
				self.tiles[ey][ex], self.tiles[y][x] = self.tiles[y][x], self.tiles[ey][ex] 
				self.tiles[ey][ex].set(ex, ey)
				self.tiles[y][x].set(x, y)
				self.setMovable()
				if self.checkComplete():
					for y in range(4):
						for x in range(4):
							pyxel.tilemaps[0].pset(3*4+x, 3*4+y, self.save.tile[y][x])
					return state.GameOverState(True, 90, 8)
			return None
		def draw(self, xoffset, yoffset):
			pass
	def __init__(self):
		super().__init__(0, 0, state.TitleState("Puzzle15 Game", state.WaitState(60, Puzzle15.PlayState(self))))
	def __str__(self):
		return "Puzzle15"
		
