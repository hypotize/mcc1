import random

class Card(object):
	cards = None
	def __init__(self, name, value):
		self.name = name
		self.value = value
	def __eq__(self, other):
		if not isinstance(other, Card):
			return NotImplemented
		return self.value == other.value
	def __lt__(self, other):
		if not isinstance(other, Card):
			return NotImplemented
		return self.value < other.value
	def __ne__(self, other):
		return not self.__eq__(other)
	def __le__(self, other):
		return self.__lt__(other) or self.__eq__(other)
	def __gt__(self, other):
		return not self.__le__(other)
	def __ge__(self, other):
		return not self.__lt__(other)
	def __str__(self):
		return "| " + self.name + " |"
	@classmethod
	def set(cls):
		cls.cards = [cls("Ａ",1), cls("２",2), cls("３",3), cls("４",4), cls("５",5), cls("６",6),	cls("７",7), cls("８",8), cls("９",9), cls("10",10), cls("Ｊ",11), cls("Ｑ",12), cls("Ｋ",13)]
	@classmethod
	def get(cls):
		if cls.cards is None:
			cls.set()
		return cls.cards[random.randrange(len(cls.cards))]
		
def main():
	print("最初に１枚カードが出ますから掛け金を決めてください。")
	print("次に出るカードが前のカードと同じか大きければ、あなたの勝ちです。")
	print("掛け金が戻りますから、続けるかどうか決めてください。続けて勝てば掛け金は２倍になります。以降、４倍、８倍と戻るお金が増えます。ただし、負けるとそれまでの勝ちはなくなります。")
	print("所持金が無くなって破産するか、1000$を超えるとゲーム終了です。")
	print("-------------------------------------------")
	money = 100
	print("ゲームを開始します。所持金は {}$です。".format(money))
	while money > 0 and money <= 1000:
		print("最初のカードです。")
		card = Card.get()
		print(card)
		bet = int(input("いくら賭けますか？(1$〜{}$) ".format(money)))
		money -= bet
		odds = 1
		while True:
			card2 = Card.get()
			print(card2)
			if card2 < card:
				print("あなたの負け。所持金は {}$です。".format(money))
				break
			print("あなたの勝ち。 {}$の勝ちです。".format(bet * odds))
			if int(input("倍率は{}倍。続けますか？ (1=Yes; 0=No!) ".format(odds * 2))) == 0:
				money += bet * odds
				print("所持金は {}$です。".format(money))
				break
			odds *= 2
			card = card2
		print()
	if money <= 0:
		print("所持金がなくなったのでゲーム終了です。")
	else:
		print("所持金が {}$になったのでゲーム終了です。")
		
if __name__ == "__main__":
	main()
			
