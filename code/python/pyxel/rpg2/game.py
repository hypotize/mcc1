import pyxel
from abc import ABC, abstractmethod

class Game(ABC):
	def __new__(cls, *args, **kargs):
		if not hasattr(cls, "_instance"):
			cls._instance = super(Game, cls).__new__(cls)
		return cls._instance
	def __init__(self, xoffset, yoffset, state=None):
		self.state = state
		self.xoffset = xoffset
		self.yoffset = yoffset
		pyxel.camera(xoffset, yoffset)
		self.change = False
	def set_state(self, state):
		self.state = state
		self.change = True
	def update(self):
		if self.change:
			self.change = False
		if self.state is not None:
			state = self.state.update()
			if state is not None:
				if isinstance(state, int):
					return state
				self.set_state(state)
		return None
	def draw(self):
		if self.change:
			self.change = False
			return
		pyxel.cls(0)
		pyxel.bltm(0, 0, 0, 0, 0, 1024, 256)
		if self.state is not None:
			self.state.draw(self.xoffset, self.yoffset)
	@abstractmethod
	def __str__(self):
		return None
