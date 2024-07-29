import random

class Alphabet:
	def __init__(self):
		self.chars = []
		for i in range(26):
			self.chars.append(chr(ord('A') + i))
	def __str__(self):
		return "".join(self.chars)
	def use(self, c):
		self.chars[ord(c) - ord('A')] = " "
		
class Word:
	animals = ["CAT", "DOG", "BEAR", "ELEPHANT", "PANDA", "LION", "PIG", "MONKEY",
		"MOUSE", "HORSE", "GORILLA", "SHEEP", "TIGER", "RABBIT",
		"KOALA", "FOX", "WOLF", "GOAT", "COW", "OX", "JAGUAR", "ZEBRA"]
	def __init__(self):
		self.answer = Word.animals.pop(random.randrange(len(Word.animals)))
		self.match = [False] * len(self.answer)
	def putchar(self, c):
		rv = -1
		for i in range(len(self.match)):
			if self.match[i]:
				continue
			if self.answer[i] == c:
				self.match[i] = True
				rv = 0
		if all(self.match):
			return 1
		return rv
	def show(self):
		print(self.answer)
	def __str__(self):
		s = ""
		for i, c in enumerate(self.answer):
			if self.match[i]:
				s += c + " "
			else:
				s += "_ "
		return s

def display(level):
	print(" +-----+")
	if level == 1:
		print(" |   (+_+;")
	else:
		print(" |     |")
	if level < 2:
		print(" |")
	elif level == 7: 
		print(" |   (@_@;")
	else:
		print(" |   (+_+;")
	if level < 0:
		print(" |   (^_^)")
	elif level < 3:
		print(" |")
	elif level == 3:
		print(" |    |Y|")
	elif level == 4:
		print(" | o／|Y|")
	elif level > 4:
		print(" | o／|Y|＼o")
	if level < 0:
		print(" | o／|Y|＼o")
	elif level < 6:
		print(" |")
	elif level == 6:
		print(" |   ／")
	else:
		print(" |   ／ ＼")
	if level < 0:
		print(" |   ／ ＼")
	elif level == 6:
		print(" | ~~")
	elif level == 7:
		print(" | ~~    ~~")
	else:
		print(" |")
	if level < 0:
		print("/| ~~    ~~")
	else:
		print("/|")

def main():
	print("--- HANGMAN ---")
	print()
	while True:
		level = 0
		alpha = Alphabet()
		answer = Word()
		while level >= 0 and level < 7:
			display(level)
			print(alpha)
			print(answer)
			c = '0'
			while ord(c) < ord('A') or ord(c) > ord('Z'):
				c = input("? ").upper()
			alpha.use(c)
			i = answer.putchar(c)
			if i < 0:
				level += 1
			elif i > 0:
				level = -1
		display(level)
		answer.show()
		if int(input("AGAIN (1=YES; 0=NO!)?")) == 0:
			break

if __name__ == "__main__":
	main()
	
