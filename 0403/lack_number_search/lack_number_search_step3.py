# 回答する時間を計測する

import random
import time

limit = 8
num_list = list(range(1, limit))
answer = random.choice(num_list)
num_list.remove(answer)
random.shuffle(num_list)
print(f'1から{limit - 1}まで')
print(num_list)
start_time = time.time()

user_answer = int(input())
if user_answer == answer:
    end_time = time.time()
    print('正解です。')
    print(round(end_time - start_time, 1), '秒で正解しました。')
else:
    print('違います。')
    print(f'正解は{answer}です。')
