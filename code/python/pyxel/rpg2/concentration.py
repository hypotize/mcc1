import pyxel
import game
import state
import random

class Concentration(game.Game):
	class Card:
		Reverse = 0
		Open = 1
		Clear = 2
		def __init__(self, _id, x, y):
			self.x = x
			self.y = y
			self.id = _id
			self.state = Concentration.Card.Reverse
	class PlayState(state.State):
		def __init__(self, game):
			self.game = game
			self.cnt = 24
			self.rest = 10
			self.open = []
			random.shuffle(self.game.cards)
		def getCard(self, pos):
			return self.game.cards[pos[1]*6+pos[0]]
		def clear(self, pos):
			for i in range(2):
				for j in range(2):
					pyxel.tilemaps[0].pset(pos[0]*2+self.game.xoffset//8+2+j, pos[1]*2+self.game.yoffset//8+4+i, (1, 0))
			self.cnt -= 1
		def update(self):
			if len(self.open) == 2:
				card1 = self.getCard(self.open[0])
				card2 = self.getCard(self.open[1]) 
				if card1.id == card2.id:
					card1.state = Concentration.Card.Clear
					self.clear(self.open[0])
					card2.state = Concentration.Card.Clear
					self.clear(self.open[1])
					self.open.clear()
					if self.cnt == 0:
						return state.GameOverState(True, 60, 9, col=(pyxel.COLOR_DARK_BLUE, pyxel.COLOR_RED))
				else:
					card1.state = Concentration.Card.Reverse
					card2.state = Concentration.Card.Reverse
					self.open.clear()
					self.rest -= 1
					if self.rest == 0:
						return state.GameOverState(False, 60, 9)
				return None
			if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
				x, y = (pyxel.mouse_x - 2*8) // 16, (pyxel.mouse_y - 4*8) // 16
				if 0 <= x < 6 and 0 <= y < 4:
					card = self.game.cards[y*6+x]
					if card.state == Concentration.Card.Reverse:
						card.state = Concentration.Card.Open
						self.open.append((x, y))
						if len(self.open) == 2:
							return state.WaitState(60, self, self.draw)
				
		def draw(self, xoffset, yoffset):
			pyxel.text(xoffset+6*8, yoffset+2*8, "Rest: {}".format(self.rest), pyxel.COLOR_WHITE)
			pyxel.text(xoffset+4*8, yoffset+14*8, "Plese Select Card", pyxel.COLOR_WHITE)
			for y in range(4):
				for x in range(6):
					card =self.game.cards[y*6+x]
					if card.state == Concentration.Card.Open:
						pyxel.blt(x*16+xoffset+2*8, y*16+yoffset+4*8, 1, card.x*8, card.y*8, 16, 16)
			
	def __init__(self):
		cardlist = (Concentration.Card(0, 0, 3), Concentration.Card(1, 2, 3), Concentration.Card(2, 4, 3), Concentration.Card(3, 0, 5), Concentration.Card(4, 2, 5), Concentration.Card(5, 4, 5))
		self.cards = [None] * 24
		k = 0
		for y in range(4):
			for x in range(6):
				card = cardlist[k % len(cardlist)]
				self.cards[y*6+x] = Concentration.Card(card.id, card.x, card.y)
				k += 1
				for i in range(2):
					for j in range(2):
						pyxel.tilemaps[0].pset(x*2+112+2+j, y*2+16+4+i, (6+j, 3+i))
		super().__init__(112*8, 16*8, state.TitleState("Concentration Game", state.WaitState(30, Concentration.PlayState(self))))
	def __str__(self):
		return "Concentration"
		
