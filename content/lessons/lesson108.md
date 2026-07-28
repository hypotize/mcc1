+++
title = "レッスン108"
date = "2026-07-28T15:00:00+09:00"
author = "橋本　吉生"
description = "いいまちがいクイズをつくろう"
showFullContent = false
readingTime = false
tags = ["クイズ", "プログラミング", "Python"]
+++

# Pythonで いいまちがいクイズをつくろう

## ステップ1：たいとるを がめんに だす

まずは、クイズの だいめいを がめんに だしてみよう。

```python
# がめんに だす
print("いいまちがいクイズ")

```

---

## ステップ2：クイズの ルールを がめんに だす

クイズの あそびかたを おしえて あげる ぶんしょうを つけたそう。

```python
# がめんに だす
print("いいまちがいクイズ")

# ルールを だす
print("わたしが、まちがったことばをいうので、ただしいことばを、こたえてください。")
print()  # 1ぎょう あける

```

---

## ステップ3：まちがえた ことば（もんだい）を だす

クイズの もんだいを がめんに だしてみよう。

```python
print("いいまちがいクイズ")
print("わたしが、まちがったことばをいうので、ただしいことばを、こたえてください。")
print()

# もんだいを だす
print("もんだい：スラムイオ")

```

---

## ステップ4：こたえを いれてもらう

キーボードから こたえを うちこんでもらおう。

```python
print("いいまちがいクイズ")
print("わたしが、まちがったことばをいうので、ただしいことばを、こたえてください。")
print()

print("もんだい：スラムイオ")

# こたえを いれてもらい、はこ（へんすう）に いれる
kotae = input("こたえを いれてね：")

```

---

## ステップ5：あっているか どうか しらべる

うった こたえが 「オムライス」と おなじか どうか しらべよう。

```python
print("いいまちがいクイズ")
print("わたしが、まちがったことばをいうので、ただしいことばを、こたえてください。")
print()

print("もんだい：スラムイオ")
kotae = input("こたえを いれてね：")

# あっているか しらべる
if kotae == "オムライス":
    print("せいかい")
else:
    print("ちがいます")

```

---

## ステップ6：もんだいを 2もん ふやす

おなじ かきかたで、もんだいを 3もんまで ふやしてみよう。

```python
print("いいまちがいクイズ")
print("わたしが、まちがったことばをいうので、ただしいことばを、こたえてください。")
print()

# --- 1もんめ ---
print("もんだい1：スラムイオ")
kotae1 = input("こたえを いれてね：")

if kotae1 == "オムライス":
    print("せいかい")
else:
    print("ちがいます")

print()

# --- 2もんめ ---
print("もんだい2：ルアンゼンチ")
kotae2 = input("こたえを いれてね：")

if kotae2 == "アルゼンチン":
    print("せいかい")
else:
    print("ち发います")

print()

# --- 3もんめ ---
print("もんだい3：きけんびょう")
kotae3 = input("こたえを いれてね：")

if kotae3 == "けんびきょう":
    print("せいかい")
else:
    print("ちがいます")

```

---

## ステップ7：もんだいと こたえを まとめる（リスト）

「もんだい」と「こたえ」の ペアを、リスト（まとめの はこ）にして せいりしよう。

```python
print("いいまちがいクイズ")
print("わたしが、まちがったことばをいうので、ただしいことばを、こたえてください。")
print()

# もんだいと こたえを リストに まとめる
mondai1 = ["スラムイオ", "オムライス"]
mondai2 = ["ルアンゼンチ", "アルゼンチン"]
mondai3 = ["きけんびょう", "けんびきょう"]

# リストを 1つの おおきな リストに まとめる
mondai_list = [mondai1, mondai2, mondai3]


# --- 1もんめ ---
print("もんだい1：" + mondai_list[0][0])
kotae1 = input("こたえを いれてね：")

if kotae1 == mondai_list[0][1]:
    print("せいかい")
else:
    print("ちがいます")

print()

# --- 2もんめ ---
print("もんだい2：" + mondai_list[1][0])
kotae2 = input("こたえを いれてね：")

if kotae2 == mondai_list[1][1]:
    print("せいかい")
else:
    print("ちがいます")

print()

# --- 3もんめ ---
print("もんだい3：" + mondai_list[2][0])
kotae3 = input("こたえを いれてね：")

if kotae3 == mondai_list[2][1]:
    print("せいかい")
else:
    print("ちがいます")

```

---

## ステップ8：まちがえた ときに ただしい こたえを おしえる

まちがえてしまった とき、ほんとうの こたえを おしえて あげよう。

```python
print("いいまちがいクイズ")
print("わたしが、まちがったことばをいうので、ただしいことばを、こたえてください。")
print()

mondai1 = ["スラムイオ", "オムライス"]
mondai2 = ["ルアンゼンチ", "アルゼンチン"]
mondai3 = ["きけんびょう", "けんびきょう"]
mondai_list = [mondai1, mondai2, mondai3]


# --- 1もんめ ---
print("もんだい1：" + mondai_list[0][0])
kotae1 = input("こたえを いれてね：")

if kotae1 == mondai_list[0][1]:
    print("せいかい")
else:
    print("ちがいます")
    # ただしい こたえを だす
    print("ただしい こたえは 「" + mondai_list[0][1] + "」 でした")

print()

# --- 2もんめ ---
print("もんだい2：" + mondai_list[1][0])
kotae2 = input("こたえを いれてね：")

if kotae2 == mondai_list[1][1]:
    print("せいかい")
else:
    print("ちがいます")
    print("ただしい こたえは 「" + mondai_list[1][1] + "」 でした")

print()

# --- 3もんめ ---
print("もんだい3：" + mondai_list[2][0])
kotae3 = input("こたえを いれてね：")

if kotae3 == mondai_list[2][1]:
    print("せいかい")
else:
    print("ちがいます")
    print("ただしい こたえは 「" + mondai_list[2][1] + "」 でした")

```

---

## ステップ9：くりかえし（for）を つかって みじかくする

なんども おなじ コードを かかないように、`for` を つかって スッキリさせよう。

```python
print("いいまちがいクイズ")
print("わたしが、まちがったことばをいうので、ただしいことばを、こたえてください。")
print()

mondai1 = ["スラムイオ", "オムライス"]
mondai2 = ["ルアンゼンチ", "アルゼンチン"]
mondai3 = ["きけんびょう", "けんびきょう"]
mondai_list = [mondai1, mondai2, mondai3]

# ばんごうを かぞえる はこ
bangou = 1

# リストの なかを じゅんばんに くりかえす
for mondai in mondai_list:
    print("もんだい" + str(bangou) + "：" + mondai[0])
    kotae = input("こたえを いれてね：")
    
    if kotae == mondai[1]:
        print("せいかい")
    else:
        print("ちがいます")
        print("ただしい こたえは 「" + mondai[1] + "」 でした")
    
    print()
    # ばんごうを 1つ ふやす
    bangou = bangou + 1

```

---

## ステップ10：もじを シャッフルして じどうで もんだいを つくる

「ただしい こたえ」の もじを バラバラに シャッフルして、もんだいを じどうで つくろう。

```python
import random  # シャッフルする どうぐを よびだす

print("いいまちがいクイズ")
print("わたしが、まちがったことばをいうので、ただしいことばを、こたえてください。")
print()

# ただしい こたえだけの リスト
kotae_list = ["オムライス", "アルゼンチン", "けんびきょう"]

bangou = 1

for kotae in kotae_list:
    # 1. もじの かずを かぞえる
    nagasa = len(kotae)
    # 2. もじを バラバラにして シャッフルする
    moji_list = random.sample(kotae, nagasa)
    # 3. バラバラの もじを 1つの つなげる
    mondai = "".join(moji_list)
    
    print("もんだい" + str(bangou) + "：" + mondai)
    nyuuryoku = input("こたえを いれてね：")
    
    if nyuuryoku == kotae:
        print("せいかい")
    else:
        print("ちがいます")
        print("ただしい こたえは 「" + kotae + "」 でした")
    
    print()
    bangou = bangou + 1

```

---

## ステップ11：つぎの もんだいの まえに 2びょう まつ

こたえが でたあとに 2びょう まつようにして、がめんを 見やすくしよう。

```python
import random  # シャッフルする どうぐを よびだす
import time    # じかんをまつ どうぐを よびだす

print("いいまちがいクイズ")
print("わたしが、まちがったことばをいうので、ただしいことばを、こたえてください。")
print()

kotae_list = ["オムライス", "アルゼンチン", "けんびきょう"]

bangou = 1

for kotae in kotae_list:
    nagasa = len(kotae)
    moji_list = random.sample(kotae, nagasa)
    mondai = "".join(moji_list)
    
    print("もんだい" + str(bangou) + "：" + mondai)
    nyuuryoku = input("こたえを いれてね：")
    
    if nyuuryoku == kotae:
        print("せいかい")
    else:
        print("ちがいます")
        print("ただしい こたえは 「" + kotae + "」 でした")
    
    print()
    
    # 2びょう まつ
    time.sleep(2)
    
    bangou = bangou + 1

```

---

## ステップ12：すきな もんだいを つくろう

プログラムのつぎのところをかえてすきなもんだいをつくろう。

kotae_list = ["オムライス", "アルゼンチン", "けんびきょう"]

たとえばこんなふうに。

kotae_list = ["ちょうほうけい", "すいじょうき", "とどうふけん", "がっしょうコンクール", "せいりせいとん", "どんぐりのせいくらべ"]

---

## ステップ13：もんだいを だすじゅんばんを かえる

まいかい もんだいが でるじゅんばんが かわるようにしよう。

```python
import random  # シャッフルする どうぐをよびだす
import time    # じかんをまつ どうぐをよびだす

print("いいまちがいクイズ")
print("わたしが、まちがったことばをいうので、ただしいことばを、こたえてください。")
print()

kotae_list = ["ちょうほうけい", "すいじょうき", "とどうふけん", "がっしょうコンクール", "せいりせいとん", "どんぐりのせいくらべ"]

# もんだいのじゅんばんをかえる
random.shuffle(kotae_list)

bangou = 1

for kotae in kotae_list:
    nagasa = len(kotae)
    # 問題の文字をバラバラにする
    moji_list = random.sample(kotae, nagasa)
    mondai = "".join(moji_list)
    
    print("もんだい" + str(bangou) + "：" + mondai)
    nyuuryoku = input("こたえを いれてね：")
    
    if nyuuryoku == kotae:
        print("せいかい！")
    else:
        print("ちがいます")
        print("ただしい こたえは 「" + kotae + "」 でした")
    
    print()
    
    # 2びょう まつ
    time.sleep(2)
    
    bangou = bangou + 1
