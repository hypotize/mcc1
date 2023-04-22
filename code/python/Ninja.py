import random

print("ニンジャがあらわれた。ニンジャは分身した")

soldier = []
for _ in range(4):
	soldier.append(random.randrange(1,5))

while True:
	damage = 0
	sign = 0
	ans = int(input("どうする? 1:戦う 2:終了 >>"))
	if ans == 2:
		print("実体は{}だった。戦士達は力尽きた".format(soldier))
		break
	for i in range(4):
		n = int(input("戦士{}の攻撃は?:ニンジャ(1~4)>>".format(i+1)))
		if soldier[i] == n:
			damage += 1
		elif n in soldier:
			sign += 1
	print("{}体にダメージを与えた！{}体の気配を感じる".format(damage, sign))
	if damage == 4:
		print("ニンジャの討伐に成功した！！")
		break
