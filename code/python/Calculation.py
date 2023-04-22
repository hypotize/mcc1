import random
import sys
import time

n = 9 if len(sys.argv) == 1 else int(sys.argv[1])

print("***暗算ゲーム***")
print("Xに何が入るかな？全部で１０問でるよ！")

start = time.time()
correct = 0
total = 0
for _ in range(10):
	x = []
	for _ in range(2):
		x.append(random.randrange(1, n+1))
	x.append(x[0] * x[1])
	i = random.randrange(3)
	q = x[i]
	x[i] = "X"
	print("{}*{}={}".format(x[0], x[1], x[2]))
	print("X>", end="")
	ans = int(input())
	total += 1
	if q == ans:
		correct += 1
		print("正解！({}/{})".format(correct, total))
	else:
		print("不正解({}/{})".format(correct, total))

print("{}問正解でした。（かかった時間{}秒）".format(correct, time.time() - start))
