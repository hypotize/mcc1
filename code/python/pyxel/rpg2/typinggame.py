import requests
import PyxelUniversalFont as puf
import pyxel
import game
import state
import sys

def getChar():
	keydict = {\
		pyxel.KEY_A : 'a',	pyxel.KEY_B : 'b', pyxel.KEY_C : 'c', pyxel.KEY_D : 'd',\
		pyxel.KEY_E : 'e', pyxel.KEY_F : 'f', pyxel.KEY_G : 'g', pyxel.KEY_H : 'h',\
		pyxel.KEY_I : 'i', pyxel.KEY_J : 'j', pyxel.KEY_K : 'k', pyxel.KEY_L : 'l',\
		pyxel.KEY_M : 'm', pyxel.KEY_N : 'n', pyxel.KEY_O : 'o', pyxel.KEY_P : 'p',\
		pyxel.KEY_Q : 'q', pyxel.KEY_R : 'r', pyxel.KEY_S : 's', pyxel.KEY_T : 't',\
		pyxel.KEY_U : 'u',	pyxel.KEY_V : 'v', pyxel.KEY_W : 'w', pyxel.KEY_X : 'x',\
		pyxel.KEY_Y : 'y', pyxel.KEY_Z : 'z', pyxel.KEY_BACKSPACE : '', pyxel.KEY_DELETE : '',\
		pyxel.KEY_SPACE : ' '}
	for key, val in keydict.items():
		if pyxel.btnp(key):
			return val
	return None

class TypingGame(game.Game):
	class InputState(state.State):
		def __init__(self, game):
			self.game = game
			self.rest = 5
			self.writer = puf.Writer("IPA_Gothic.ttf")
			self.input_word = ""
			self.start = True
		def init(self):
			url = "https://random-words-api.kushcreates.com/api?words=1&language=en"
			try:
				while True:
					response = requests.get(url, timeout=(3.0, 7.5))
					response.raise_for_status()
					self.word = response.json()[0]["word"]
					if len(self.word) <= 10:
						break
			except requests.exceptions.RequestException as e:
				print(f"エラーが発生しました: {e}")
				sys.exit()
			self.sec = len(self.word)
			self.tcnt = 0
			self.input_word = ""
		def update(self):
			if self.start:
				self.init()
				self.start = False
			self.tcnt += 1
			if self.tcnt % 30 == 0:
				self.sec -= 1
				if self.sec == 0:
					return state.GameOverState(False, 90, 7, self._draw, yoffset=-5*8)
			c = getChar()
			if c is not None:
				if c == '' and len(self.input_word) > 0:
					self.input_word = self.input_word[0:-1]
				else:
					self.input_word += c		
					if self.word == self.input_word:
						self.rest -= 1
						if self.rest == 0:
							return state.GameOverState(True, 90, 7, self._draw, yoffset=-5*8)
						self.start = True
						return state.WaitState(60, self, self._draw)
			return None
		def draw(self, xoffset, yoffset):
			pyxel.text(8*8+xoffset, 2*8+yoffset, "{}".format(self.sec), pyxel.COLOR_WHITE)
			pyxel.text(10*8+xoffset, 2*8+yoffset, "Rest : {}".format(self.rest), pyxel.COLOR_WHITE)
			self._draw(xoffset, yoffset)
		def _draw(self, xoffset, yoffset):
			offset = 48+(32-len(self.word)*8)//2 
			self.writer.draw(offset+xoffset, 5*8+yoffset, self.word.upper(), 15, pyxel.COLOR_WHITE)
			offset = 48+(32-len(self.input_word)*8)//2 
			self.writer.draw(offset+xoffset, 13*8+yoffset, self.input_word.upper(), 15, pyxel.COLOR_WHITE)
	def __init__(self):
		super().__init__(96*8, 16*8, state.TitleState("Typing Game", state.WaitState(60, TypingGame.InputState(self), self.draw_typing)))
	def draw_typing(self, xoffset, yoffset):
		pyxel.text(4*8+256, 2*8+128, "Please Type Word", pyxel.COLOR_WHITE)
	def __str__(self):
		return "Typing"
		
