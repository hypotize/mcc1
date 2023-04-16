import json
import random

# 問題を読み込む
with open('quiz_data.json') as f:
    quiz_data = json.load(f)['questions']

# 問題をランダムにシャッフルする
random.shuffle(quiz_data)

# 正解の数を初期化する
num_correct = 0

# 各問題を処理する
for i, question in enumerate(quiz_data):
    # 空白行を表示する
    print()

    # 問題を表示する
    print(f'{i+1}. {question["question"]}')

    # 選択肢を表示する
    for j, choice in enumerate(question['choices']):
        print(f'{j+1}. {choice}')

    # ユーザーの答えを取得する
    user_answer = int(input('答えの番号を入力してください: '))

    # 答えを判定する
    if user_answer == question['answer']:
        print('正解！')
        num_correct += 1
    else:
        print('不正解...')
        print(f'正解は {question["choices"][question["answer"]]} でした。')

# 正解の数を表示する
print(f'\n正解数: {num_correct}')
