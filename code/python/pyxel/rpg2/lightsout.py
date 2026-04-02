import pyxel
import game
import state

class LightsOut(game.Game):
	class PlayState(state.State):
		def __init__(self):
			self.start = True
			self.lights = [[True] * 5 for _ in range(5)]
			for y in range(5):
				for x in range(5):
					self._turn(x, y, True)
			self.cnt = 25
		def init(self):
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
						self._turn(x, y, False)
		def _turn(self, x, y, turn):
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
		def update(self):
			if self.start:
				self.init()
				self.start = False
			if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
				if pyxel.mouse_x // 8 == 14 and pyxel.mouse_y // 8 == 1:
					return state.GameOverState(False, 60, 3)
				x = (pyxel.mouse_x - 3*8) // 16
				y = (pyxel.mouse_y - 3*8) // 16
				for dx, dy in ((0, 0),(-1, 0), (0, -1), (1, 0), (0, 1)):
					nx, ny = x + dx, y + dy
					if 0 <= nx < 5 and 0 <= ny < 5:
						self.lights[ny][nx] = not self.lights[ny][nx]
						self._turn(nx, ny, self.lights[ny][nx])
						self.cnt += 1 if self.lights[ny][nx] else -1
				if self.cnt == 0:
					return state.GameOverState(True, 60, 3)
			return None
		def draw(self, xoffset, yoffset):
			pyxel.text(4*8+xoffset, 14*8+yoffset, "Please Press Light", pyxel.COLOR_WHITE)
	def __init__(self):
		super().__init__(48*8, 16*8, state.TitleState("Lights Out", LightsOut.PlayState()))
	def __str__(self):
		return "LightsOut"
