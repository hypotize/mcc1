import random

limit = 8
num_list = list(range(1, limit))
answer = random.choice(num_list)
num_list.remove(answer)
print(f'1から{limit - 1}まで')
print(num_list)

user_answer = int(input())
if user_answer == answer:
    print('正解です。')
else:
    print('違います。')
    print(f'正解は{answer}です。')
