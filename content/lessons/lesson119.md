+++
title = "レッスン119"
date = "2026-08-10T09:00:00+09:00"
author = "小野寺　健"
description = "クラス入門その２　クラスを使ってゲームを作ろう"
showFullContent = false
readingTime = false
tags = ["クラス", "オブジェクト指向", "Python"]
+++

# クラス入門その２　クラスを使ってゲームを作ろう

レッスン118で習ったクラスを使って、Pythonで簡単なゲームを作ってみましょう。
最初はとてもシンプルなゲームですが、徐々に機能を追加していきます。

作成するゲームはポケモンバトルゲームです。
3匹のポケモンが登場し、そのうち2匹が戦います。

必要な「クラス」はPokemonクラスとBattle（戦闘）クラスです。
Battle（戦闘）クラスはあらかじめ用意してあるので、Pokemonクラスを作成していきます。

## 作成するクラス

Pokemonクラスを作成してください。
Pokemonクラスは以下のような仕組みを持っています。

1. コンストラクタ(__init__メソッド）

	```python
	def __init__(self, name, hp, attack):
		...
	```
	というメソッドを定義します。

	クラスからインスタンス（実体）を作成する時に呼ばれるメソッドを「コンストラクタ」と呼びます。
	Pythonでは`__init__(self, 引数)`という名前のメソッドが「コンストラクタ」です。
	
	以下の引数を設定し、属性(self.XXXXという変数）に設定します。
	
		- name （ポケモンの名前、文字列）
		- hp (ポケモンの体力、整数）
		- attack （ポケモンの攻撃力、整数）
	
1. take_damageメソッド

	```python
	def take_damage(self, damage):
		...
	```
	というメソッドを定義します。

	ポケモンがダメージを受けた時に呼ばれて、引数のdamage分、ポケモンのhpを減らします。
	ただし、hpは0より小さくは（マイナスには）なりません。

	同時に、以下のようなprint文を表示してください。
	{}の部分に具体的な文字列や数字が入ります。
	
	`{ポケモンの名前} は {ダメージの値} ダメージを受けた！（残りHP: {HPの値}）`
	
	print文で表示する文字列の中に変数（属性）の値を入れたい場合は、`f"文字列{変数名}文字列"`のような書き方をします。
	ポケモンの名前の属性は`self.name`、ダメージの変数は`damage`、HPの値の属性は`self.hp`なので以下のように記述します。
	
	```python
	print(f"{self.name} は {damage} ダメージを受けた！（残りHP: {self.hp}）")
	```
	
1. is_faintedメソッド

	```python
	def is_fainted(self):
		...
		return ...
	```
	というメソッドを定義します。

	ポケモンが戦闘不能（HPが0）かどうかを判定するメソッドです。
	
	戻り値（メソッドが`return`で返す値）はTrue（戦闘不能）かFalse（戦闘可能）です。
	
## 課題１

以下のサンプルコードをコピペして、Pokemon.pyというファイルを作成してください。
これにPokemonクラスを追加してプログラムを完成させてください。

```Python
# ここにポケモンクラスを追加してください。

class Battle:	#ポケモン同士が戦闘するクラス
	def __init__(self, pokemon1, pokemon2):	# 戦闘する２匹のポケモンを指定する
		self.pokemon1 = pokemon1
		self.pokemon2 = pokemon2
		
	def fight(self):	# ポケモン同士が戦闘する
		print(f"\n{self.pokemon1.name} vs {self.pokemon2.name} の戦闘開始！")
		turn = 0	# 交互に攻撃するためのターンの回数
		while True:	# 戦闘ループ
			if turn % 2 == 0:	# 偶数のターン回数だったら
				attacker = self.pokemon1		# 攻撃するのはポケモン１
				defender = self.pokemon2 	# 攻撃されるのはポケモン２
			else:	# 奇数のターン回数だったら
				attacker = self.pokemon2		# 攻撃するのはポケモン２
				defender = self.pokemon1 	# 攻撃されるのはポケモン１
			print(f"\n{attacker.name} の攻撃！")
			defender.take_damage(attacker.attack)	# 攻撃するポケモンの攻撃力で攻撃されるポケモンはダメージを受ける
			
			if defender.is_fainted():	# 攻撃されたポケモンが戦闘不能になったら
				print(f"\n{defender.name} は倒れた！ {attacker.name} の勝ち！")
				break	# 戦闘ループから抜ける
			
			turn += 1		# ターン回数を更新する
			
if __name__ == '__main__':	# メインプログラム
	charmander = Pokemon("ヒトカゲ", 100, 40)	# ヒトカゲポケモンを作成
	squirtle = Pokemon("ゼニガメ", 100, 40)	# ゼニガメポケモンを作成
	bulbasaur = Pokemon("フシギダネ", 100, 40)	# フシギダネポケモンを作成
	
	battle = Battle(charmander, squirtle)		# ヒトカゲとゼニガメがバトルフィールドへ
	battle.fight()	# 戦闘開始
```

１〜３のメソッドを持ったPokemonクラスを追加して、このプログラムを完成させ、実行するとコンソールに以下が表示されます。

```
ヒトカゲ vs ゼニガメ の戦闘開始！

ヒトカゲ の攻撃！
ゼニガメ は 40 ダメージを受けた！（残りHP: 60）

ゼニガメ の攻撃！
ヒトカゲ は 40 ダメージを受けた！（残りHP: 60）

ヒトカゲ の攻撃！
ゼニガメ は 40 ダメージを受けた！（残りHP: 20）

ゼニガメ の攻撃！
ヒトカゲ は 40 ダメージを受けた！（残りHP: 20）

ヒトカゲ の攻撃！
ゼニガメ は 40 ダメージを受けた！（残りHP: 0）

ゼニガメ は倒れた！ ヒトカゲ の勝ち！
```

<details><summary>回答例</summary>

```
class Pokemon:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"\n{self.name} は {damage} ダメージを受けた！（残りHP: {self.hp}）")
        
    def is_fainted(self):
        return self.hp == 0
```
</details>

## 課題２

ポケモンに「炎」、「水」、「草」などのポケモンタイプ(poke_type)を追加してください。

それぞれのポケモンタイプには弱点と強みがあります。

|ポケモンタイプ|弱点|強み|
|:--:|:--:|:--:|
|炎|水|草|
|水|草|炎|
|草|炎|水|

1. Pokemonクラスのコンストラクタの引数に「poke_type」を追加し、ポケモンの属性も追加して設定する

1. Pokemonクラスに「クラス変数」としてタイプの強みと弱みのテーブル（辞書）type_chartを追加する

	```python
	class Pokemon:
		type_chart = {
			"炎" : {"弱点" : "水", "強み" : "草"},		# 炎タイプの弱点は水、強みは草
			"水" : {"弱点" : "草", "強み" : "炎"},		# 水タイプの弱点は草、強みは炎
			"草" : {"弱点" : "炎", "強み" : "水"}		# 草タイプの弱点は炎、強みは水
		}
		def __init__(self, name, hp, attack, poke_type):
		...
	```
	このように、クラスのすぐ下に定義される変数を「クラス変数」と言い、クラス共通で使用する値を設定することができます。
	クラス変数はPokemon.type_chartのように{クラス名}.{クラス変数名}で参照することができます。
	
	自分のポケモンタイプから強み・弱点を取得するには、以下のようにして参照することができます。
	
	自分のポケモンタイプの強み： `Pokemon.type_chart[self.poke_type]['強み']`
	
	自分のポケモンタイプの弱点： `Pokemon.type_chart[self.poke_type]['弱点']`

1. ポケモンのタイプとそのタイプの強み・弱点を以下のように表示するshow_type_advantage()メソッドを追加する

	表示する内容の例は以下の通りです。
	
	```
	ヒトカゲ のタイプ: 炎
	 - 弱点: 水
	 - 強み: 草
	```
	
	ポケモン作成後に、このhow_type_advantage()メソッドを呼んで表示します。

1. 	take_damage()メソッドを変更する

	引数をダメージ(damage)から相手のポケモン(opponent)に変更し、ダメージ(damage)は相手のポケモンの攻撃力(attack)に設定します。
	さらに、ポケモン同士の相性にしたがい、相手のポケモンのタイプが自分の弱点であれば、ダメージ(damage)を1.5倍し、自分の強みであればダメージ(damage)を0.5倍にします。
	
これらの変更を行って、プログラムを実行すると以下のようにコンソールに表示されます。

```
ヒトカゲ のタイプ： 炎
 - 弱点： 水
 - 強み： 草
ゼニガメ のタイプ： 水
 - 弱点： 草
 - 強み： 炎
フシギダネ のタイプ： 草
 - 弱点： 炎
 - 強み： 水
 
ヒトカゲ vs ゼニガメ の戦闘開始！

ヒトカゲ の攻撃！
ゼニガメ は 20 ダメージを受けた！（残りHP: 80）

ゼニガメ の攻撃！
ヒトカゲ は 60 ダメージを受けた！（残りHP: 40）

ヒトカゲ の攻撃！
ゼニガメ は 20 ダメージを受けた！（残りHP: 60）

ゼニガメ の攻撃！
ヒトカゲ は 60 ダメージを受けた！（残りHP: 0）

ヒトカゲ は倒れた！ ゼニガメ の勝ち！
```

Pokemon.pyを修正して、実行結果が上記のようになるようにしてください。

<details><summary>回答例</summary>

```python
class Pokemon:
	type_chart = {	# タイプ同士の相性テーブル（クラス変数）
		"炎" : {"弱点" : "水", "強み" : "草"},
		"水" : {"弱点" : "草", "強み" : "炎"},
		"草" : {"弱点" : "炎", "強み" : "水"}
	}

	def __init__(self, name, hp, attack, poke_type):
		self.name = name
		self.hp = hp
		self.attack = attack
		self.poke_type = poke_type	# ポケモンのタイプを追加
		
	def show_type_advantage(self):	# ポケモンのタイプを表示するメソッド
		print(f"{self.name} のタイプ： {self.poke_type}")
		print(f" - 強み： {Pokemon.type_chart[self.poke_type]['強み']}")
		print(f" - 弱点： {Pokemon.type_chart[self.poke_type]['弱点']}")
    
	def take_damage(self, opponent):	# 引数を戦闘相手のポケモンに変更
		if Pokemon.type_chart[self.poke_type]['強み'] == opponent.poke_type:	# 戦闘相手のポケモンのタイプが「強み」なら
			damage = int(opponent.attack * 0.5)	# ダメージが半減
		elif Pokemon.type_chart[self.poke_type]['弱点'] == opponent.poke_type:	# 戦闘相手のポケモンのタイプが「弱点」なら
			damage = int(opponent.attack * 1.5)	# ダメージが1.5倍
		else:	# それ以外なら
			damage = opponent.attack	# 攻撃力がそのままダメージになる	
		self.hp -= damage
		if self.hp < 0:
			self.hp = 0
		print(f"\n{self.name} は {damage} ダメージを受けた！（残りHP: {self.hp}）")
        
	def is_fainted(self):
		return self.hp == 0
        
class Battle:	#ポケモン同士が戦闘するクラス
	def __init__(self, pokemon1, pokemon2):	# 戦闘する２匹のポケモンを指定する
		self.pokemon1 = pokemon1
		self.pokemon2 = pokemon2
		
	def fight(self):	# ポケモン同士が戦闘する
		print(f"\n{self.pokemon1.name} vs {self.pokemon2.name} の戦闘開始！")
		turn = 0	# 交互に攻撃するためのターンの回数
		while True:	# 戦闘ループ
			if turn % 2 == 0:	# 偶数のターン回数だったら
				attacker = self.pokemon1		# 攻撃するのはポケモン１
				defender = self.pokemon2 	# 攻撃されるのはポケモン２
			else:	# 奇数のターン回数だったら
				attacker = self.pokemon2		# 攻撃するのはポケモン２
				defender = self.pokemon1 	# 攻撃されるのはポケモン１
			print(f"\n{attacker.name} の攻撃！")
			defender.take_damage(attacker)	# 攻撃する相手のポケモンから攻撃されるポケモンはダメージを受ける
			
			if defender.is_fainted():	# 攻撃されたポケモンが戦闘不能になったら
				print(f"\n{defender.name} は倒れた！ {attacker.name} の勝ち！")
				break	# 戦闘ループから抜ける
			
			turn += 1		# ターン回数を更新する
			
if __name__ == '__main__':	# メインプログラム
	charmander = Pokemon("ヒトカゲ", 100, 40, "炎")	# ヒトカゲポケモンを作成
	charmander.show_type_advantage()	# ポケモンのタイプと特徴を表示
	squirtle = Pokemon("ゼニガメ", 100, 40, "水")	# ゼニガメポケモンを作成
	squirtle.show_type_advantage()	# ポケモンのタイプと特徴を表示
	bulbasaur = Pokemon("フシギダネ", 100, 40, "草")	# フシギダネポケモンを作成
	bulbasaur.show_type_advantage()		# ポケモンのタイプと特徴を表示
	
	battle = Battle(charmander, squirtle)		# ヒトカゲとゼニガメがバトルフィールドへ
	battle.fight()	# 戦闘開始
 
```
</details>

## 課題３

ポケモンが相手を攻撃するとき、本来は「わざ」を使います。
また、ポケモンの攻撃の威力はポケモン同士のタイプの相性によるのではなく、攻撃をうけたポケモンのタイプと攻撃の「わざ」のタイプの相性によります。

そこで、「Waza」というクラスを追加して、ポケモンが「わざ」を使って攻撃するようにしてみましょう。

1. Wazaクラスには以下の属性があります

		- 「わざ」の名前(name)
		- 「わざ」のタイプ(waza_type)
		- 「わざ」の威力(power)
	
	コンストラクタ(`__init__()`)でこれらを受け取って、属性に設定してください
	
1. Wazaクラスには、「わざ」の名前と威力を文字列で返す`__str__()`メソッドがあります

	戻り値（返す値）： {わざの名前} {わざの威力｝
	
	例：`ひのこ 40`
	
	クラスに`__str__()`メソッドがあると、クラスのオブジェクト（インスタンス）をprintしたとき、このメソッドの戻り値が表示されます。
	
1. 各ポケモンが持っている「わざ」は以下の通り

	メインプログラムの先頭でこれらの「わざ」を作成し、各ポケモンに設定します。
	
	<table>
	<thread>
		<tr align="center">
			<th>ポケモン</th>	<th>わざの名前</th>	<th>わざのタイプ</th>	<th>わざの威力</th>
		</tr>
	</thread>
	<tr align="center">
		<td>ヒトカゲ</td>	<td>ひのこ</td>	<td>炎</td>	<td>40</td>
	</tr>
	<tr align="center">
		<td>ゼニガメ</td>	<td>みずでっぽう</td>	<td>水</td>	<td>40</td>
	</tr>
	<tr align="center">
		<td>フシギダネ</td>	<td>はっぱカッター</td>	<td>草</td>	<td>40</td>
	</tr>
	</table>
	
1. Pokemonクラスの属性のうち、攻撃力(attack)を、「わざ」(waza)という属性に変えます

	コンストラクタで受け取るものもattackではなくwazaになります。
	
1. take_damageメソッドにおいて、ダメージ(damage)を相手の攻撃力(attack)ではなく、相手の「わざ」(waza)の威力(power)に変更します

	`damage = opponent.waza.power`になります
	
1. take_damageメソッドにおいて、ダメージ(damage)の効果に影響するのは相手のタイプ(opponent.poke_type)ではなく、相手の「わざ」のタイプに変更します

	相手の「わざ」のタイプ： `opponent.waza.waza_type`
	
1. show_type_advantageメソッドにおいて、以下のように「わざ」の名前と威力も表示します

	```
	ヒトカゲ のタイプ: 炎
	 - 弱点: 水
	 - 強み: 草
	 - わざ: ひのこ 40
	```
	
1. Battleクラスのfightメソッドにおいて、ポケモンの攻撃メッセージに「わざ」の名前と威力も追加します

	Pokemonクラスのwaza「わざ」も追加し、以下のように表示させます。
	
	例：　`ヒトカゲ の攻撃！ ひのこ 40!!`

これらの変更を行って、プログラムを実行すると以下のようにコンソールに表示されます。

```
ヒトカゲ のタイプ： 炎
 - 弱点： 水
 - 強み： 草
 - わざ： ひのこ 40
ゼニガメ のタイプ： 水
 - 弱点： 草
 - 強み： 炎
 - わざ： みずでっぽう 40
フシギダネ のタイプ： 草
 - 弱点： 炎
 - 強み： 水
 - わざ： はっぱカッター 40
 
ヒトカゲ vs ゼニガメ の戦闘開始！

ヒトカゲ の攻撃！ ひのこ 40!!
ゼニガメ は 20 ダメージを受けた！（残りHP: 80）

ゼニガメ の攻撃！ みずでっぽう 40!!
ヒトカゲ は 60 ダメージを受けた！（残りHP: 40）

ヒトカゲ の攻撃！ ひのこ 40!!
ゼニガメ は 20 ダメージを受けた！（残りHP: 60）

ゼニガメ の攻撃！みずでっぽう 40!!
ヒトカゲ は 60 ダメージを受けた！（残りHP: 0）

ヒトカゲ は倒れた！ ゼニガメ の勝ち！
```

Pokemon.pyを修正して、実行結果が上記のようになるようにしてください。

<details><summary>回答例</summary>

```python
class Waza:
	def __init__(self, name, power, waza_type):
		self.name = name
		self.power = power
		self.waza_type = waza_type
		
	def __str__(self):
		return f"{self.name} {self.power}"
		
class Pokemon:
	type_chart = {
		"炎" : {"弱点" : "水", "強み" : "草"},
		"水" : {"弱点" : "草", "強み" : "炎"},
		"草" : {"弱点" : "炎", "強み" : "水"}
	}

	def __init__(self, name, hp, waza, poke_type):
		self.name = name
		self.hp = hp
		self.waza = waza
		self.poke_type = poke_type
		
	def show_type_advantage(self):
		print(f"{self.name} のタイプ： {self.poke_type}")
		print(f" - 強み： {Pokemon.type_chart[self.poke_type]['強み']}")
		print(f" - 弱点： {Pokemon.type_chart[self.poke_type]['弱点']}")
		print(f" - わざ： {self.waza}")
    
	def take_damage(self, opponent):
		if Pokemon.type_chart[self.poke_type]['強み'] == opponent.waza.waza_type:
			damage = int(opponent.waza.power * 0.5)
		elif Pokemon.type_chart[self.poke_type]['弱点'] == opponent.waza.waza_type:
			damage = int(opponent.waza.power * 1.5)
		else:
			damage = opponent.waza.power
		self.hp -= damage
		if self.hp < 0:
			self.hp = 0
		print(f"\n{self.name} は {damage} ダメージを受けた！（残りHP: {self.hp}）")
        
	def is_fainted(self):
		return self.hp == 0
        
class Battle:	#ポケモン同士が戦闘するクラス
	def __init__(self, pokemon1, pokemon2):	# 戦闘する２匹のポケモンを指定する
		self.pokemon1 = pokemon1
		self.pokemon2 = pokemon2
		
	def fight(self):	# ポケモン同士が戦闘する
		print(f"\n{self.pokemon1.name} vs {self.pokemon2.name} の戦闘開始！")
		turn = 0	# 交互に攻撃するためのターンの回数
		while True:	# 戦闘ループ
			if turn % 2 == 0:	# 偶数のターン回数だったら
				attacker = self.pokemon1		# 攻撃するのはポケモン１
				defender = self.pokemon2 	# 攻撃されるのはポケモン２
			else:	# 奇数のターン回数だったら
				attacker = self.pokemon2		# 攻撃するのはポケモン２
				defender = self.pokemon1 	# 攻撃されるのはポケモン１
			print(f"\n{attacker.name} の攻撃！ {attacker.waza}!!")
			defender.take_damage(attacker)	# 攻撃するポケモンの攻撃力で攻撃されるポケモンはダメージを受ける
			
			if defender.is_fainted():	# 攻撃されたポケモンが戦闘不能になったら
				print(f"\n{defender.name} は倒れた！ {attacker.name} の勝ち！")
				break	# 戦闘ループから抜ける
			
			turn += 1		# ターン回数を更新する
			
if __name__ == '__main__':	# メインプログラム

	fire_waza = Waza("ひのこ", 40, "炎")				# 炎わざ「ひのこ」威力40
	water_waza = Waza("みずでっぽう", 40, "水")		# 水わざ「みずでっぽう」威力40
	grass_waza = Waza("はっぱカッター", 40, "草")		# 草わざ「はっぱカッター」威力40
	
	charmander = Pokemon("ヒトカゲ", 100, fire_waza, "炎")	# ヒトカゲポケモンを作成
	charmander.show_type_advantage()
	squirtle = Pokemon("ゼニガメ", 100, water_waza, "水")	# ゼニガメポケモンを作成
	squirtle.show_type_advantage()
	bulbasaur = Pokemon("フシギダネ", 100, grass_waza, "草")	# フシギダネポケモンを作成
	bulbasaur.show_type_advantage()
	
	battle = Battle(charmander, squirtle)		# ヒトカゲとゼニガメがバトルフィールドへ
	battle.fight()	# 戦闘開始
```

</details>

## 課題４

レッスン119で習ったクラスの「継承」「ポリモーフィズム」を使って、プログラムをリファクタリング（作り直し）してみましょう。

Pokemonクラスを抽象クラスにし、各ポケモンタイプごとに新たなクラスを作成します

1. abcライブラリをimportしてABC, abstractmethodが使えるようにし、Pokemonクラスを抽象クラスに設定します
	
	```python
	from abc import ABC, abstractmethod
	...
	class Pokemon(ABC):
		...
	``` 

1. Pokemonクラスからtype_chartクラス変数とポケモンタイプの属性を削除します

	```python
	class Pokemon(ABC):
		def __init__(self, name, hp, waza):
			...
	```

1. show_type_advantageメソッドを仮想メソッドにします

	```python
	@abstractmethod
	def show_type_advantage(self):
		pass
	```

1. get_damageという仮想メソッドを追加します

	```python
	@abstractmethod
	def get_damage(self, opponent):
		pass
	```
	
1. take_damageメソッドにおいて、damageを取得する部分を上記のget_damageメソッドから取得するように変更します

	```python
	def take_damage(self, opponent):
		damage = self.get_damage(opponent)
		self.hp -= damage
		...
	```
	
1. 炎ポケモンクラス(Fire_Pokemon)、水ポケモンクラス(Water_Pokemon)、草ポケモンクラス(Grass_Pokemon)を作成し、Pokemonクラスを継承します

	```python
	class Fire_Pokemon(Pokemon):
		...
	class Water_Pokemon(Pokemon):
		...
	class Grass_Pokemon(Pokemon):
		...
	```
	
1. 各クラスにshow_type_advantageメソッドと、get_damageメソッドを追加します

	type_charテーブルを削除したので、このテーブルを使わず、代わりに各クラスに対応した情報を直接書き込みます。
	
	例：Grass_Pokemonクラス
	
	```python
	class Grass_Pokemon(Pokemon):
	
		def show_type_advantage(self):
			print(f"{self.name} のタイプ： 草")
			print(" - 強み： 水")
			print(" - 弱点： 炎")
			print(f" - わざ： {self.waza}")
			
		def get_damage(self, opponent):
			if 	opponent.waza.waza_type == "水":	# 草タイプポケモンの強みは水タイプのわざ
				damage = int(opponent.waza.power * 0.5)
			elif opponent.waza.waza_type == "炎":	# 草タイプポケモンの弱点は炎タイプのわざ
				damage = int(opponent.waza.power * 1.5)
			else:
				damage = opponent.waza.power
			return damage
	```
	
1. ポケモンを作成する時、ポケモンのタイプに合わせてそれぞれのポケモンタイプクラスから作成するように変更します

	例：フシギダネポケモンの作成
	```python
	bulbasaur = Grass_Pokemon("フシギダネ", 100, grass_waza)    # フシギダネポケモンを作成
	```

Pokemon.pyを修正して、実行してみましょう。
出力結果は例題３と同じです。

<details><summary>回答例</summary>

```python
from abc import ABC, abstractmethod

class Waza:
    def __init__(self, name, power, waza_type):
        self.name = name
        self.power = power
        self.waza_type = waza_type
        
    def __str__(self):
        return f"{self.name} {self.power}"
        
class Pokemon(ABC):
    def __init__(self, name, hp, waza):
        self.name = name
        self.hp = hp
        self.waza = waza
        
    @abstractmethod
    def show_type_advantage(self):
        pass

    @abstractmethod    
    def get_damage(self, opponent):
        pass
    
    def take_damage(self, opponent):
        damage = self.get_damage(opponent)
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"\n{self.name} は {damage} ダメージを受けた！（残りHP: {self.hp}）")
        
    def is_fainted(self):
        return self.hp == 0
    
class Fire_Pokemon(Pokemon):   
    def show_type_advantage(self):
        print(f"{self.name} のタイプ： 炎")
        print(" - 強み： 草")
        print(" - 弱点： 水")
        print(f" - わざ： {self.waza}")
        
    def get_damage(self, opponent):
        if opponent.waza.waza_type == "草":
            damage = int(opponent.waza.power * 0.5)
        elif opponent.waza.waza_type == "水":
            damage = int(opponent.waza.power * 1.5)
        else:
            damage = opponent.waza.power
        return damage
    
class Water_Pokemon(Pokemon):   
    def show_type_advantage(self):
        print(f"{self.name} のタイプ： 水")
        print(" - 強み： 炎")
        print(" - 弱点： 草")
        print(f" - わざ： {self.waza}")
        
    def get_damage(self, opponent):
        if opponent.waza.waza_type == "炎":
            damage = int(opponent.waza.power * 0.5)
        elif opponent.waza.waza_type == "草":
            damage = int(opponent.waza.power * 1.5)
        else:
            damage = opponent.waza.power
        return damage
    
class Grass_Pokemon(Pokemon):
    def show_type_advantage(self):
        print(f"{self.name} のタイプ： 草")
        print(" - 強み： 水")
        print(" - 弱点： 炎")
        print(f" - わざ： {self.waza}")
        
    def get_damage(self, opponent):
        if opponent.waza.waza_type == "水":
            damage = int(opponent.waza.power * 0.5)
        elif opponent.waza.waza_type == "炎":
            damage = int(opponent.waza.power * 1.5)
        else:
            damage = opponent.waza.power
        return damage
        
class Battle:    #ポケモン同士が戦闘するクラス
    def __init__(self, pokemon1, pokemon2):    # 戦闘する２匹のポケモンを指定する
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        
    def fight(self):    # ポケモン同士が戦闘する
        print(f"\n{self.pokemon1.name} vs {self.pokemon2.name} の戦闘開始！")
        turn = 0    # 交互に攻撃するためのターンの回数
        while True:    # 戦闘ループ
            if turn % 2 == 0:    # 偶数のターン回数だったら
                attacker = self.pokemon1        # 攻撃するのはポケモン１
                defender = self.pokemon2     # 攻撃されるのはポケモン２
            else:    # 奇数のターン回数だったら
                attacker = self.pokemon2        # 攻撃するのはポケモン２
                defender = self.pokemon1     # 攻撃されるのはポケモン１
            print(f"\n{attacker.name} の攻撃！ {attacker.waza}!!")
            defender.take_damage(attacker)    # 攻撃するポケモンの攻撃力で攻撃されるポケモンはダメージを受ける
            
            if defender.is_fainted():    # 攻撃されたポケモンが戦闘不能になったら
                print(f"\n{defender.name} は倒れた！ {attacker.name} の勝ち！")
                break    # 戦闘ループから抜ける
            
            turn += 1        # ターン回数を更新する
            
if __name__ == '__main__':    # メインプログラム
    
    fire_waza = Waza("ひのこ", 40, "炎")                # 炎わざ「ひのこ」威力40
    water_waza = Waza("みずでっぽう", 40, "水")        # 水わざ「みずでっぽう」威力40
    grass_waza = Waza("はっぱカッター", 40, "草")        # 草わざ「はっぱカッター」威力40
    
    charmander = Fire_Pokemon("ヒトカゲ", 100, fire_waza)    # ヒトカゲポケモンを作成
    charmander.show_type_advantage()
    squirtle = Water_Pokemon("ゼニガメ", 100, water_waza)    # ゼニガメポケモンを作成
    squirtle.show_type_advantage()
    bulbasaur = Grass_Pokemon("フシギダネ", 100, grass_waza)    # フシギダネポケモンを作成
    bulbasaur.show_type_advantage()
    
    battle = Battle(charmander, squirtle)        # ヒトカゲとゼニガメがバトルフィールドへ
    battle.fight()    # 戦闘開始
```

</details>

## まとめ

レッスン118で学んだ「クラス」を使って、簡単なポケモンバトルゲームを作ることができました。
このように、クラスを使うと簡単に「わざ」を増やしたり、いろいろなタイプのポケモンたちを増やしたりすることができるようになります。
プログラムを改造し、好きなポケモンを増やして、バトルさせてみましょう。

もちろん、実際のポケモンバトルゲームはもっともっと複雑ですが、「クラス」を使って共通化するという基本的な考え方は同じです。
