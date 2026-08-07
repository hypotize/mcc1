+++
title = "レッスン116"
date = "2026-08-06T10:00:00+09:00"
author = "小野寺　健"
description = "テスト駆動開発とユニットテスト"
showFullContent = false
readingTime = false
tags = ["テスト駆動開発", "ユニットテスト", "Python"]
+++

# テスト駆動開発とユニットテスト

従来のプログラムの開発方法は「ウォーターフォール」と呼ばれ、「設計（アルゴリズムなどプログラムの手順を考える）」 → 「実装（実際にプログラムを作る）」 → 「テスト（テストプログラムやテストデータでテストする）」という手順で行われていました。

この方法の問題点は、以下のようなものがあります。
- 実装の段階で設計のもれが見つかることがあり、設計からやり直すと手間がかかる
- 実装が終わってもテストの段階で、設計もれ・実装もれが見つかることがあり、やり直しでさらに手間がかかる
- テストが不十分だと、テストもれが発生し、プログラムのバグが後で発覚することがある

テスト駆動開発（Test Driven Development: TDD）では、これらの問題点を解決するため、「テスト」 → 「実装」 → 「リファクタリング」を何回も繰り返して、開発を進めていくという開発方法です。

## テスト駆動開発(TDD)の基本サイクル

テスト起動開発の基本サイクルは、主に「レッド・グリーン・リファクタリング」から構成されています。

1. レッド：　プログラムの仕様（プログラムに求まられるもの）に対してテストを書く、プログラムは空なので、エラーになる。
2. グリーン：　テストが成功するようにプログラムを書く。（余計なプログラムがあっても構わない）
3. リファクタリング：　出来たプログラムに対して余分な部分を削除し、きれいなプログラミングにする。ただし、テストは成功させる。

動作する（テストが成功する）きれいなプログラムを書くことが目的ですが、いきなりきれいなプログラムを書くことはむずかしいので「動作するプログラムを書きながら、きれいに直していく」というのがテスト駆動の考え方です。

## テスト駆動開発の種類

テスト駆動開発には4種類のテストがあります。

- ユニットテスト（単体テスト、関数単位でテストする）
- 統合テスト（全体テスト、プログラム全体をテストする）
- 回帰テスト（修正テスト、プログラムの修正で他の機能に悪影響が出ていないかテストする）
- 受け入れテスト（完了テスト、プログラム完了時に最終的なテストを行う）

今回は、ユニットテストを通じて、テスト駆動開発を体験してみましょう。

## ユニットテストとは

ユニットテスト(unit test)とは、単体テストとも呼ばれ、プログラムを構成する比較的小さな単位（ユニット）が個々の機能を正しく果たしているかを検証するテストです。

通常、関数やメソッドが単体テストの単位（ユニット）となります。

## Pythonでユニットテストを行ってみよう

今回は、Pythonでユニットテストを行ってみます。
Pythonには`unittest`というユニットテストを行うモジュールが予め用意されています。

レッスン115で習った統合開発環境spyderを使って、試してみましょう。

### 2つの値を加える関数(add)を作る（中身は空）

まず、例として2つの値を加える関数(add)を作ることにします。

addは引数（関数に与える変数）を2つ持っているので以下のようなプログラムになります。
```python

def add(x, y):
	return
```

最初はプログラムは空なので、何も返さず`return`にしてあります。


### 2つの値を加えた結果をテストするテストプログラムを作る（レッド）

2つの値を加える関数(add)をテストするテストプログラムを作ります。

```python

import unittest		# 最初にこの行を入れて、unittestモジュールを呼びます

# 先程のテスト対象のプログラム
def add(x, y):
	return
	
# テストコード
class TestAddFunction(unittest.TestCase):	# classの後にテストごとに異なるTestで始まる名前を付け、後ろに(unittest.Test):を付けます。
	def test_add_int(self):	# 実際のテストプログラム、頭にtest_を付けて、最後に(self):を付けます。
		result = add(2, 3)		# テストしたい関数を呼びます。
		self.assertEqual(result, 5)	# assertEqual(結果、期待する値)で、期待する値と等しいか確認します。
		
	def test_add_float(self):
		result = add(2.5, 3.5)
		self.assertAlmostEqual(result, 6.0)
		
	def test_add_string(self):
		result = add("Hello, ", "world")
		self.assertEqual(result, "Hello, world")
		
if __name__ == '__main__':	# ここでテストプログラムを実行します。
	unittest.main()
```

ここで、`AssertEqual`というのは結果と期待値が等しいかを確認する関数です。
`AssertAlmostEqual`というのは結果と期待値がほぼ等しいかを確認する関数で、整数ではない小数点の付いた値を比較する場合、計算誤差を無視するために使用します。

### テストプログラムを実行する（レッド）

それでは、このプログラムを実行してみましょう。
spyderなら「▶アイコン」をクリックすれば簡単に実行できます。

コンソールに以下のような表示が行われます。

```
EFF
======================================================================
ERROR: test_add_float (__main__.TestAddFunction.test_add_float)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/onodera/python/タイトル無し1.py", line 16, in test_add_float
    self.assertAlmostEqual(result, 6.0)
  File "/root/.local/spyder-6/envs/spyder-runtime/lib/python3.12/unittest/case.py", line 916, in assertAlmostEqual
    diff = abs(first - second)
               ~~~~~~^~~~~~~~
TypeError: unsupported operand type(s) for -: 'NoneType' and 'float'

======================================================================
FAIL: test_add_int (__main__.TestAddFunction.test_add_int)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/onodera/python/タイトル無し1.py", line 12, in test_add_int
    self.assertEqual(result, 5)	# assertEqual(結果、期待する値)で、期待する値と等しいか確認します。
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: None != 5

======================================================================
FAIL: test_add_string (__main__.TestAddFunction.test_add_string)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/onodera/python/タイトル無し1.py", line 20, in test_add_string
    self.assertEqual(result, "Hello, world")
AssertionError: None != 'Hello, world'

----------------------------------------------------------------------
Ran 3 tests in 0.008s

FAILED (failures=2, errors=1)
```

テストするプログラムが空なので当然エラーになります。

最初の`EFF`というのはERROR（エラー）、FAIL（失敗）、FAIL（失敗）という意味です。
ERROR（エラー）とFAIL（失敗）の違いはERROR（エラー）はプログラムの書き方がおかしいことを意味し、FAIL（失敗）はプログラムの結果がおかしいことを意味します。

その後に、各テストプログラムごとの詳細なエラー情報が書かれています。

`test_add_float`関数はERROR（エラー）で、理由はテスト関数の出力結果（空なのでNone）と期待値が比較できないためと言っています。

`test_add_int`関数と`test_add_string`関数はFAIL（失敗）で、理由はテスト関数の出力結果（空なのでNone）と期待値が等しくないためと言っています。

最後に、テストの実行時間と最終結果がFAILED（失敗）で、その内訳（失敗=2、エラー1）が記載されています。

### 動作するプログラムを書く（グリーン）

それでは`add`関数を修正して正しく動作するようにしてみましょう。

以下のように修正します。

```python
def add(x, y):
	return x + y
```

### テストプログラムを実行する（グリーン）

もう一度、このプログラムを実行し直してみましょう。

今度は、コンソールに以下のような表示が行われます。

```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

`.`はテストプログラムが成功したことを意味し、これが3個あるので、3つのプログラムが全て成功したことになります。

最後に、テストの実行時間と最終結果がOK（成功）であったことが記載されています。

### プログラムにバグを入れてみる（リファクタリング）

本来はここで、動作したプログラムの無駄な部分を削除したり、整理したりしてプログラムをきれいにし、再度プログラムをテストします。

今回のプログラムはこれ以上きれいにできないので、逆に、試しに、プログラムにバグを入れてみましょう。
何かの理由でプログラムを修正した場合、バグが入って、本来の動作がうまく動かなくなることはよくある話です。

```
def add(x, y):
	return x + y + 1
```

実行すると、コンソールに以下のような表示が行われます。

```
FFE
======================================================================
ERROR: test_add_string (__main__.TestAddFunction.test_add_string)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/onodera/python/タイトル無し1.py", line 19, in test_add_string
    result = add("Hello, ", "world")
             ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/onodera/python/タイトル無し1.py", line 6, in add
    return x + y + 1
           ~~~~~~^~~
TypeError: can only concatenate str (not "int") to str

======================================================================
FAIL: test_add_float (__main__.TestAddFunction.test_add_float)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/onodera/python/タイトル無し1.py", line 16, in test_add_float
    self.assertAlmostEqual(result, 6.0)
AssertionError: 7.0 != 6.0 within 7 places (1.0 difference)

======================================================================
FAIL: test_add_int (__main__.TestAddFunction.test_add_int)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/onodera/python/タイトル無し1.py", line 12, in test_add_int
    self.assertEqual(result, 5)	# assertEqual(結果、期待する値)で、期待する値と等しいか確認します。
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 6 != 5

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=2, errors=1)
```

今度は「FFE」でFAIL（失敗）、FAIL（失敗）、ERROR（エラー）になりました。

`test_add_int`と`test_add_float`は結果が期待値と異なる（+1されている）のでFAIL（失敗）、`test_add_string`は文字列と数値を足そうとしているのでERROR（エラー）になりました。

このようにリファクタリングでバグが混入してしまった場合、さらに修正を行い、テストプログラムが正しく動作するようにするということを繰り返します。

### テスト前後の処理を追加する

例えば、ファイルの読み込みや書き込みなどの関数をテストする場合、予めファイルをオープンしたり、最後にファイルをクローズしたりする必要があります。
このように、テストする関数を実行する前や実行後に何らかの処理を行わなければ行けない場合、`setUp()`および`tearDown()`という関数を定義することでテスト実行前後の処理を記述することができます。

先程のプログラムのバグを元にもどし、代わりに`setUp()`および`tearDown()`という関数を追加してみましょう。

`add`関数は特にテスト実行前後に行うべき処理はないので`setUp() called.`と`tearDown() called.`というコメントを出力してみます。
実行順番を確認するために、各テストプログラムにもコメント出力を追加します。

```
import unittest

# テスト対象のコード
def add(x, y):
    return x + y

# テストクラス
class TestAddFunction(unittest.TestCase):

    def setUp(self):
        print("setUP() called.")

    def test_add_integers(self):
        print("test_add_integers() called.")
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_floats(self):
        print("test_add_floats() called.")
        result = add(2.5, 3.5)
        self.assertAlmostEqual(result, 6.0, places=2)

    def test_add_strings(self):
        print("test_add_strings() called.")
        result = add("Hello, ", "world!")
        self.assertEqual(result, "Hello, world!")

    def tearDown(self):
        print("tearDown() called.")

if __name__ == '__main__':
    unittest.main()
```

実行すると、コンソールに以下のような表示が行われます。

```
...
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
setUP() called.
test_add_floats() called.
tearDown() called.
setUP() called.
test_add_integers() called.
tearDown() called.
setUP() called.
test_add_strings() called.
tearDown() called.
```

テスト成功の表示の後に、コメントが出力され、各テストプログラムがsetUp()とtearDown()の間に実行されていることがわかります。
`setUp()`および`tearDown()`は、テストプログラムの数だけ実行されることになります。

テストする関数を実行する前後に何らかの前処理、後処理が必要な場合、この仕組みを利用します。

### 実行プログラムとテストプログラムを分離する

今回は、同じファイルの中に実行プログラム（add関数）とテストプログラム(TestAddFunction)を書きましたが、実際のプログラムではテストプログラムは別のファイルに書きます。
こうすることで、テストが終了したら、実行プログラムのファイルだけ利用できるようになります。

先程のプログラムを以下のように分離します。
なお、テストプログラムはtest_XXX.pyという名前にします。

add.py
``` python
def add(x, y):
	return x + y
```

test_add.py
```
import unittest
from add import add

# テストコード
class TestAddFunction(unittest.TestCase):	# classの後にテストごとに異なるTestで始まる名前を付け、後ろに(unittest.Test):を付けます。
	def test_add_int(self):	# 実際のテストプログラム、頭にtest_を付けて、最後に(self):を付けます。
		result = add(2, 3)		# テストしたい関数を呼びます。
		self.assertEqual(result, 5)	# assertEqual(結果、期待する値)で、期待する値と等しいか確認します。
		
	def test_add_float(self):
		result = add(2.5, 3.5)
		self.assertAlmostEqual(result, 6.0)
		
	def test_add_string(self):
		result = add("Hello, ", "world")
		self.assertEqual(result, "Hello, world")
		
if __name__ == '__main__':	# ここでテストプログラムを実行します。
	unittest.main()
```

test_add.pyを実行すると、ファイルを分離する前と同様のテスト結果が出力されます。

### 実行プログラムととテストプログラムのディレクトリ（フォルダ）をわける

簡単なプログラムであれば、同じディレクトリ（フォルダ）に実行プログラムとテストプログラムがあってもあまり問題になりませんが、実行プログラムが複数のファイルにわかれているなどの本格的なプロジェクトでは、実行プログラムとテストプログラムが同じディレクトリ（フォルダ）にあるのはあまり好ましくありません。

そこでプロジェクトでテストを行う場合、実行プログラムとテストプログラムは以下のように、それぞれディレクトリ（フォルダ）を分けます。

```
プロジェクト
	├── src
	│   ├── add.py
	│   ├──   :
	│   └── xxx.py
	└── tests
	    ├── test_add.py
	    ├──   :
	    └── test_xxx.py
```

この際、各プログラムは以下のようになります。

add.py
```python
def add(x, y):
	return x + y
```

test_add.py

```
import unittest
from src.add import add

# テストクラス
class TestAddFunction(unittest.TestCase):

    def test_add_integers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_floats(self):
        result = add(2.5, 3.5)
        self.assertAlmostEqual(result, 6.0, places=2)

    def test_add_strings(self):
        result = add("Hello, ", "world!")
        self.assertEqual(result, "Hello, world!")

if __name__ == '__main__':
    unittest.main()
```

#### テストを実行する

残念ながら、通常のspyder環境ではディレクトリを分離したテストを直接実行することはできません。（ただし、別途ユニットテストのプラグインを入れれば、spyder環境でも実行可能になります）

今回は、テストの実行はコマンドラインから実行することとします。

- testsディレクトリ（フォルダ）内の全てのテストケースを実行する

	プロジェクトディレクトリ（フォルダ）に移動し、コマンドラインから`python3 -m unittest discover tests`を実行することで、testsディレクトリ（フォルダ）内のテストをまとめて実行することができます。

- 1つのテストプログラムだけ実行する

	プロジェクトディレクトリ（フォルダ）に移動し、コマンドラインから`python3 -m unittest tests.test_add`を実行することで、testsディレクトリ（フォルダ）内のtest_add.pyのテストプログラムだけを実行できます。
	なお、コマンドラインから直接`python3 tests/test_add.py`のように実行すると、add.pyをimportすることができずエラーになってしまうので注意してください。（spyder環境で直接実行しても同様にエラーになります）
	
	
## より実践的なユニットテストの例

「add」関数では、単純すぎるので、もっと実践的なプログラムでユニットテストを行ってみましょう。

レッスン104で学習した、「バブルソート」のプログラムを使ってユニットテストを行います。

まず、ユニットテストしやすいように「バブルソート」のプログラムを関数に整理します。
引数のaはソートする数列の入った配列、nは配列の長さです。

```python
def bubbleSort(a, n):
	k = n
	while k > 0:
		for i in range(k-1):
			if a[i] > a[i+1]:
				a[i], a[i+1] = a[i+1], a[i]
		k -= 1
	return
```

メインプログラムで以下のように「バブルソート関数」を呼ぶと、配列がソートされ、表示されます。

```python
if __name__ == '__main__':
	a = [8, 4, 3, 7, 6, 5, 2, 1]
	bubbleSort(a, len(a))		# len(a)は配列の長さで、8になります。
	print(a)
```

このプログラムを実行するとコンソールにソートされた配列`[1, 2, 3, 4, 5, 6, 7, 8]`が表示されます。

このプログラムを先程のsrcディレクトリ（フォルダ）の下に、「bubbleSort.py」という名前で保存します。

### ユニットテストを作成する。

上記のプログラムのユニットテストを作成してみましょう。

配列`[1, 2, 3, 4, 5, 6, 7, 8]`をランダムに並べ直して、「バブルソート関数」を呼ぶとソートされた配列`[1, 2, 3, 4, 5, 6, 7, 8]`に戻れば正解です。

先程のtestsディレクトリ（フォルダ）の下に、「test_bubbleSort.py」という名前で以下のファイルを作成します。

```
import unittest
from src.bubbleSort import bubbleSort
import random

class TestBubbleSort(unittest.TestCase):

	def setUp(self):
		self.expectedList = [1, 2, 3, 4, 5, 6, 7, 8]
		self.randomList = random.sample(self.expectedList, k=len(self.expectedList))
		
	def test_bubbleSort(self):
		bubbleSort(self.randomList, len(self.randomList))
		self.assertEqual(self.randomList, self.expectedList)
		
if __name__ == '__main__':
	unittest.main()
```

`setUp`関数の中でソートされた配列`[1, 2, 3, 4, 5, 6, 7, 8]`(expectedList)と、これをランダムに並び替えた新たな配列(randomList)を作成します。

`test_bubbleSort`関数で、randomList配列を`bubbleSort`関数でソートし、元のexpectedList配列と等しいかを`assertEqual`関数でチェックしています。

プロジェクトディレクトリ（フォルダ）から`python3 -m unittest tests.test_bubbleSort`を実行すると、
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

が表示されて、ユニットテストが成功したことがわかります。

レッスン104で学んだ、selection sortやinsertion sortも同様にselectionSort.py、insertionSort.pyとして作成し、テストファイル名を`test_sort.py`として、以下のようなテストプログラムを作成すれば、同じ`SetUp`関数で用意されたテストデータで、様々なソートが正しく動作するかをテストできます。

```
import unittest
from src.bubbleSort import bubbleSort
from src.selectionSort import selectionSort
from src.insertionSort import insertionSort
import random

class TestSort(unittest.TestCase):

	def setUp(self):
		self.expectedList = [1, 2, 3, 4, 5, 6, 7, 8]
		self.randomList = random.sample(self.expectedList, k=len(self.expectedList))
		
	def test_bubbleSort(self):
		bubbleSort(self.randomList, len(self.randomList))
		self.assertEqual(self.randomList, self.expectedList)
		
	def test_selectionSort(self):
		selectionSort(self.randomList, len(self.randomList))
		self.assertEqual(self.randomList, self.expectedList)
		
	def test_insertionSort(self):
		insertionSort(self.randomList, len(self.randomList))
		self.assertEqual(self.randomList, self.expectedList)
		
if __name__ == '__main__':
	unittest.main()
```
		
## まとめ

テスト駆動開発という方法を学び、その中でユニットテストについて体験してみました。
今後、プログラムを作成するときはテストの重要性を認識し、ユニットテストを行って、品質の高い（バグが少なく、きれいな）プログラムの作成を心がけましょう。
