import random
import time
import os
import copy
import platform

input("enterキーを押して下さい")

print("3秒間5つの数字を表示しますので、記憶してください")

numbers = []
for i in range(5):
	numbers.append(random.randrange(1, 100))

print(" ".join(list(map(str, numbers))))

time.sleep(3)

if platform.system() == 'Linux':
	os.system('clear')
elif platform.system() == 'Windows':
	os.system('cls')

print("5つの数字をすべて入力してください")

answer = copy.copy(numbers)

while len(answer) > 0:
	n = int(input())
	if n in answer:
		print("正解")
		answer.remove(n)
	else:
		print("不正解")
		break
		
if len(answer) == 0:
	print("全問正解です")
else:
	print("正解は", numbers)
	
