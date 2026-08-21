+++
title = "レッスン112"
date = "2026-08-02T10:00:00+09:00"
author = "小野寺　健"
description = "論理演算入門"
showFullContent = false
readingTime = false
tags = ["論理演算", "コンピュータ", "プログラミング"]
+++

# 論理演算入門

「論理演算」とは「命題」を対象とした演算です。
「命題」とは、真（正しいこと、True）か偽（間違っていること、False）かを判断できる文や式のことです。

例えば「5は3より大きい」（正しい＝真）や「3は5より大きい」（間違っている＝偽）などが命題です。

## 論理演算の種類

よく使われる論理演算の種類は、以下の4つです。
- and（かつ、論理積）
- or（または、論理和）
- not（でない、否定）
- xor（排他的にまたは、排他的論理和）

## 各演算の結果

### A and B

「AかつB」という意味なので、AとBの両方が真(True)のとき真(True)となり、その他の場合は偽(False)になります。

### A or B

「AまたはB」という意味なので、AとBのいずれかが真(True)あるいは両方とも真(True)のときに真（True）となり、両方とも偽（False）の場合は偽（False）となります。

### not A

「Aでない」という意味なので、Aが真(True)なら偽(False)になり、Aが偽(False)なら真(True)になります。

### A xor B

「A排他的にまたはB」という意味です。
ここで「排他的（他を排除する）」というのはAかBの一方だけという意味なので、AとBのいずれか一方だけが真(True)のときだけ真(True)となり、その他の場合（両方とも真(True)か両方とも偽(False)の場合）は偽(False)になります。

### 各演算結果の一覧

以下にand、or、not、xorの演算結果を一覧表で示します。

1. and（論理積、かつ）

| A \ B | 真(True) | 偽(False) |
|:--:|:--:|:--:|
| <font color="lime">**真(True)**</font> | **真(True)** | **偽(False)** |
| <font color="lime">**偽(False)**</font> | **偽(False)** | **偽(False)** |

2. or（論理和、または）

| A \ B | 真(True) | 偽(False) |
|:--:|:--:|:--:|
| <font color="lime">**真(True)**</font> | **真(True**) | **真(True)** |
| <font color="lime">**偽(False)**</font> | **真(True)** | **偽(False)** |

3. not（否定、でない）

| 真(True) | 偽(False) |
|:--:|:--:|
| **偽(False)** | **真(True)** |

4. xor（排他的論理和、排他的にまたは）

| A \ B | 真(True) | 偽(False) |
|:--:|:--:|:--:|
| <font color="lime">**真(True)**</font> | **偽(False)** | **真(True)** |
| <font color="lime">**偽(False)**</font> | **真(True)** | **偽(False)** |
	
論理演算は、プログラムの分岐処理（`if`や`while`など）で、いくつかの条件（条件は命題の一種です）を結びつけたり、条件を否定したりするときに使われます。

真(True)と偽(False)を`1`と`0`の数値に対応させると、論理演算は2進数の演算であるとみなせます。
例えば、真(True) and 真(True)は、`1 and 1 = 1`という2進数の演算とみなせます。
コンピュータの内部では、電気信号で表された2進数を演算する仕組みとして、論理演算が使われています。

## ド・モルガンの法則

<b>ド・モルガンの法則</b>は、論理式を変形する法則です。
以下にド・モルガンの法則を示します。

### 法則１

`not (A and B) = (not A) or (not B)`

「A and Bの結果をnotした論理式は、not Aとnot Bをorした論理式と等しい」

これを図で示します。
なお、図の中でandは`∩`、orは`∪`、notは`ー`で表します。

- 左辺の `not (A and B)`から考えます
- まず、`A and B`を図で表すと、下の図４の左のようになります
- したがって、`not (A and B)`は図４の右のようになります

![図４](/images/D4.jpg)

- 一方右辺の`(not A) or (not B)`は
- 下の図５の左上の`(not A)`と左下の`(not B)`を`or`したものなので
- `(not A) or (not B)`は図５の右のようになります

![図５](/images/D5.jpg)

図４の右側と、図５の右側は等しいので、法則１が成り立つことがわかります。

### 法則２

`not (A or B) = (not A) and (not B)`

「A or Bの結果をnotした論理式は、not Aとnot Bをandした論理式と等しい」

- 左辺の`not (A or B)`から考えます
- まず、`A or B`を図で表すと、下の図１の左のようになります
- したがって、`not (A or B)`は図１の右のようになります

![図４](/images/D1.jpg)

- 一方右辺の`(not A) and (not B)`は
- 下の図２の左上の`(not A)`と左下の`(not B)`を`and`したものなので
- `(not A) and (not B)`は図２の右のようになります

![図５](/images/D2.jpg)

図１の右側と、図２の右側は等しいので、法則２が成り立つことがわかります。

## 問題１

`P`、`Q`、`R`は`真(True)`か`偽(False)`の値を持つ命題です。
- `P = 真(True)`
- `(not P) or Q = 真(True)`
- `(not Q) or R = 真(True)`

のとき、`Q`と`R`はそれぞれ`真(True)`、`偽(False)`のどちらでしょうか？

<details><summary>答え</summary>

- `P = 真(True)`なので`(not P) = 偽(False)`です。
- したがって、`(not P) or Q = 真(True)`は`偽(False) or Q = 真(True)`です。
- `偽(False)`と`or`した結果が`真(True)`ということは、`Q = 真(True)`になります。
- `Q = 真(True)`とわかったので、`(not Q) = 偽(False)`です。
- したがって、`(not Q) or R = 真(True)`は`偽(False) or R = 真(True)`です。
- `偽(False)`と`or`した結果が`真(True)`ということは、`R = 真(True)`になります。

以上のことから、`R`と`Q`はどちらも`真(True)`になります。

</details>

## 問題２

この問題はド・モルガンの法則を使って複雑な論理式をシンプルに変形する問題です。

論理式`not (((not A) or B) and (A or (not C)))`と等しいのはどの論理式でしょうか。
1. `(A and (not B)) or ((not A) and C)`
2. `((not A) and B) or (A and (not C))`
3. `(A or (not B)) and ((not A) or C)`
4. `((not A) or B) and (A or (not C))`

 <details><summary>答え</summary>

- `not (((not A) or B) and (A or (not C)))`

	`((not A) or B)`を`X` 、`(A or (not C))`を`Y`にそれぞれ置き換えると `not (X and Y)`となります。
	これを`(not X) or (not Y)`に変形し、`X`、`Y`を元に戻すと以下のようになります。
- `(not((not A) or B)) or (not(A or (not C)))`

	式の前半で`(not A)`を`X`、`B`を`Y`にそれぞれ置き換えると`not (X or Y)`となります。
	これを`(not X) and (not Y)`に 変形し、`X`、`Y`を元に戻すと以下のようになります。
- `(not(not(A)) and (not B)) or (not(A or (not C)))`

	`not(not(A)) = A`なので`A`に変形すると以下のようになります。
	
- `(A and (not B)) or (not(A or (not C)))`

	式の後半で`A`を`X`、`(not C)`を`Y`にそれぞれ置き換えると`not (X or Y)`となります。
	これを`(not X) and (not Y)`に 変形し、`X`、`Y`を元に戻すと以下のようになります。
	
- `(A and (not B)) or (not(A) and not(not(C)))`

	`not(not(C)) = C`なので`C`に変形すると以下のようになり、1の式と一致します。
	
- `(A and (not B)) or (not(A) and C)`

	したがって、正解は1となります。
	
</details>

　 
