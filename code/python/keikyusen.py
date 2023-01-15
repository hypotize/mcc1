import os
from inputimeout import inputimeout, TimeoutOccurred
from sys import platform

def clearConsole():
        if platform == "win32":
                os.system('cls')
        else:
                os.system('clear')

title = "快特京急久里浜行きの途中停車駅"
remain = [ "みうらかいがん","つくいはま","けいきゅうながさわ","YRPのび",]
consume = []

print(title,"をひらがなでタイムアウト時間以内に入力しね。タイムアウト時間以内に入力しないか、入力済の名前を入力するか、間違っていたらアウトだよ")
timeout = int(input("タイムアウト時間を入力したら開始だよ。　タイムアウト時間（秒）は: "))

while len(remain) > 0:
	try:
		station = inputimeout(prompt=title+"は？"+str(timeout)+"秒以内に答てね: ",timeout=timeout)
	except TimeoutOccurred:
		print("タイムオーバーです！")
		break
	if station in remain:
		clearConsole()
		print("正解です！")
		remain.remove(station)
		consume.append(station)
	elif station in consume:
		print("入力済の名前です、アウト！")
		break
	else:
		print("間違いです、アウト！")
		break
if len(remain) == 0:
	print("大正解です！")
else:
	print("正解は、",remain, "です。")

