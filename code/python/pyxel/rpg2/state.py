import pyxel
from abc import ABC, abstractmethod

class State(ABC):
	def __new__(cls, *args, **kargs):
		if not hasattr(cls, "_instance"):
			cls._instance = super(State, cls).__new__(cls)
		return cls._instance
	@abstractmethod
	def update(self):
		return None
	@abstractmethod
	def draw(self, xoffset, yoffset):
		pass
		
class TitleState(State):
	def __init__(self, title, state, draw=None):
		self.title = title
		self.state = state
		self._draw = draw
	def update(self):
		if pyxel.btnp(pyxel.KEY_RETURN):
			return self.state
		return None
	def draw(self, xoffset, yoffset):
		if self._draw is not None:
			self._draw(xoffset, yoffset)
		l = len(self.title) * 4
		pyxel.text((128-l)//2+xoffset, 10+yoffset, self.title, pyxel.COLOR_BLACK)
		pyxel.text(2*8+xoffset, 14*8+yoffset, "Please Press ENTER Key", pyxel.COLOR_BLACK)
		
class WaitState(State):
	def __init__(self, waittime, state, draw=None):
		self.waittime = waittime
		self.state = state
		self._draw = draw
	def update(self):
		self.waittime -= 1
		if self.waittime <= 0:
			return self.state
		return None
	def draw(self, xoffset, yoffset):
		if self._draw is not None:
			self._draw(xoffset, yoffset)
		
class GameOverState(State):
	def __init__(self, result, waittime, level, draw=None, yoffset=0, col=(pyxel.COLOR_GREEN, pyxel.COLOR_RED)):
		self.waittime = waittime
		self.result = result
		self.level = level
		self._draw = draw
		self.yoffset = yoffset
		self.col = col
	def update(self): 
		self.waittime -= 1
		if self.waittime <= 0:
			return self.level+1 if self.result else self.level
		return None
	def draw(self, xoffset, yoffset):
		if self._draw is not None:
			self._draw(xoffset, yoffset)
		if self.result:
			pyxel.text(4*8+xoffset, 7*8+yoffset+self.yoffset, "You Win!! Level Up!!", self.col[0])
		else:
			pyxel.text(3*8+xoffset, 7*8+yoffset+self.yoffset, "You Lose!! Try Again!!", self.col[1])		
		
