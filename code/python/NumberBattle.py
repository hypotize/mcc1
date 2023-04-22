import random

print("*****数字バトルゲーム*****")

pc = []
you = []
for i in range(1, 6):
	pc.append(i)
	you.append(i)
	
win = 0
lose = 0
for i in range(1, 6):
	while True:
		print("{}回戦目。1~5の数字を入力>".format(i), end="")
		your_number = int(input())
		if your_number < 1 or your_number > 5:
			print("1~5の数字を入力してください")
		elif your_number not in you:
			print("一度使った数字は使えません")
		else:
			break
	you.remove(your_number)
	pc_number = pc.pop(random.randrange(len(pc)))
	print("PCの数字:{}".format(pc_number))
	if pc_number > your_number:
		print("あなたの負け")
		lose += 1
	elif pc_number < your_number:
		print("あなたの勝ち")
		win += 1
	else:
		print("引き分け")

if win > lose:
	print("{}対{}であなたの勝ち".format(win, lose))
elif win < lose:
	print("{}対{}であなたの負け".format(win, lose))
else:
	print("{}対{}で引き分け".format(win, lose))
