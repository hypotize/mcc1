+++
title = "レッスン130"
date = "2026-10-27T09:00:00+09:00"
author = "小野寺　健"
description = "Python演習ドリル200 基礎練習165〜172"
showFullContent = false
readingTime = false
tags = ["Python", "プログラミング演習", "Jupyter" ]
+++

# Python演習ドリル200 基礎練習165〜172

Pythonプログラムを学び始めた方向けの演習ドリルです。

今回は、順番が前後しますが、基礎練習の165〜172です。

## jupyterとjupyter notebook

本演習では**jupyter notebook**を使用します。
インストールされているか確認してください。
インストールされていない場合、**jupyter**と**jupyter notebook**のインストール方法については、[レッスン33](https://miura.io/lessons/lesson33)を参照してください。

## 演習前の基礎学習

実際に**jupyter notebook**を使用して演習を行う前に、演習の中で使用するPythonの機能について学習しましょう。

- GUI(Graphic User Interface)

	以下のように`tkinter`というライブラリを`import`することでGUIを利用することができるようになります。
	
	```python
	import tkinter as tk
	```
	
	`tkinter`という名前はちょっと長いので`as tk`で`tk`という名前に置き換えています。
	
	- ウィンドウの作成
	
		`tk.Tk()`を実行することでメインウィンドウを作成し、作成したウィンドウを`root`という変数に設定します。
	
		```python
		root = tk.Tk()
		```
	
		`geometry`メソッドを実行することでウィンドウのサイズを指定することができます。
		サイズは引数の文字列で`"横x縦"`（例えば`"300x200"`)と指定します。
	
		```python
		root.geometry("300x200")
		```
	
		`title`メソッドを実行することで表示するウィンドウ名を設定することができます。
	
		```python
		root.title("こんにちはアプリ")
		```
	
		最後に`mainloop`メソッドを実行するとウィンドウが起動され、表示されます。
	
	- ラベルの作成
	
		ウィンドウに文字を表示させるために「ラベル(Label)」という部品（ウィジェット）を作成します。
		
		引数の`text`に表示したい文字列を指定して、`tk.Label()`でラベルを作成し、`lbl`という変数に設定します。
		
		```python
		lbl = tk.Label(text="ラベル")
		```
		
		作成したラベルをウィンドウに配置するには`place`メソッドで引数`x`、`y`により位置を指定します。
		
		```python
		lbl.place(x=120, y=120)
		```
		
	- ボタンの作成
	
		ウィンドウにボタンを追加するには「ボタン(Button)」という部品（ウィジェット）を作成します。
		
		引数の`text`にボタンに表示したい文字列を指定して、`tk.Button()`でラベルを作成し、`btn`という変数に設定します。
		
		```python
		btn = tk.Button(text="押してください")
		```
		
		作成したボタンをウィンドウに配置するには`place`メソッドで引数`x`、`y`により位置を指定します。
		
		```python
		btn.place(x=100, y=50)
		```
		
	- テキストボックスの作成
	
		ウィンドウに文字列を入力するためのテキストボックスを追加するには「エントリー(Entry)」という部品（ウィジェット）を作成します。
		
		引数の`width`にテキストボックスの幅を指定して、`tk.Entry()`でラベルを作成し、`txtbox`という変数に設定します。
		
		```python
		txtbox = tk.Entry(width=10)
		```
		
		作成したテキストボックスをウィンドウに配置するには`place`メソッドで引数`x`、`y`により位置を指定します。
		
		```python
		txtbox.place(x=100, y=100)
		```		
	
	- ボタンを押したときの処理
	
		`tk.Button()`に`command`という引数を追加することでボタンを押したときの処理を設定することができます。
		
		具体的には以下のように関数`sub`を作成し、その関数名`sub`を`command`引数に設定します。
		
		```python
		def sub():
			print("ボタンが押されたよ")
			
			...
			
		btn = tk.Button(text="押してください", command=sub)
			
			...
		```
		
	- テキストボックスの入力内容の取得
	
		テキストボックスに対して`get`メソッドを実行することにより、テキストボックスに入力した文字列を取得することができます。
		
		```python
		a = txtbox.get()
		```
		
		これを先程のボタン処理時の関数`sub`内で行うことで、ボタン押下によってテキストボックスに入力した文字列を取得することができるようになります。
		
		```python
		def sub():
			a = txtbox.get()
			print(a)
		```
		
		
	- ラベルの文字列の変更
	
		ラベルに対して`configure`メソッドで`text`引数を設定することにより、ラベルの文字列を変更することができます。
		
		```python
		lbl.configure(text="変更後のラベル")
		```
		
		以下のようにして、ボタン処理時の関数`sub`内で取得したテキストボックスに入力した文字列を使ってラベルを書き換えることができます。
		
		```python
		def sub():
			a = txtbox.get()
			lbl.configure(text=a)
		```
		
- その他のGUI部品（ウィジェット）

	演習には使われていないGUI部品（ウィジェット）をいくつか紹介します。
	
	- チェックボックス
	
		- [ ]チェック1
		- [x]チェック2
		
		ウィンドウに上記のようなチェックボックスを追加するには「チェックボタン(Checkbutton)」という部品（ウィジェット）を作成します。
		
		引数の`text`にチェックボックスに表示したい文字列を指定して、`tk.Checkbutton()`でチェックボックスを作成し、`checkbox`という変数に設定します。
		
		その際、チェックされているか否かの状態を保持する変数`check`を設定し、引数の`variable`に指定します。
		
		```python
		check = tk.BooleanVar()
		checkbox = tk.CheckBox(text="チェック", variable=check) 
		```
		
		作成したチェックボックスをウィンドウに配置するには`place`メソッドで引数`x`、`y`により位置を指定します。
		
		```python
		checkbox.place(x=100, y=200)
		```
		
		また、ボタンが押された際に、チェックボックスがチェックされているかどうかは変数`check`の`get`メソッドを呼ぶことで取得できます。
		
		```python
		def sub():
			if check.get():
				print("チェックされています")
			else:
				print("チェックされていません")
		```
		
	- ラジオボタン
	
		いくつかの選択肢から１つの値を選ぶラジオボタンをウィンドウに追加するには「ラジオボタン(Radiobutton)」という部品（ウィジェット）を作成します。
		
		引数の`text`にラジオボックスに表示したい文字列を指定して、`tk.Radiobutton()`でラジオボックスを作成し、`radiobutton1`という変数に設定します。
		
		複数のラジオボックスを作成し、`radiobutton2`、`radiobutton3`などの異なる変数に設定します。
		
		その際、どのラジオボタンが選択されているかを保持する共通の変数`radio`を設定し、引数の`variable`に指定します。
		さらに、選択された際に変数`radio`に設定する値を引数の`value`に指定します。
		なお、変数`radio`には`set`メソッドで初期値を設定しておきます。
		
		```python
		radio = tk.StringVar()
		radio.set("選択肢1")
		
		radiobutton1 = tk.Radiobutton(text="選択肢1", variable=radio, value="選択肢1")
		radiobutton2 = tk.Radiobutton(text="選択肢2", variable=radio, value="選択肢2")
		radiobutton3 = tk.Radiobutton(text="選択肢3", variable=radio, value="選択肢3")
		```
		
		作成したチェックボックスをウィンドウに配置するには`place`メソッドで引数`x`、`y`により位置を指定します。
		
		```python
		radiobutton1.place(x=100, y=200)
		radiobutton2.place(x=100, y=220)
		radiobutton3.place(x=100, y=240)
		```
		
		上記のようにラジオボタンを個別にウィンドウを配置することもできますが、以下のようにラジオボタンをまとめてフレーム(Frame)部品（ウィジェット）にまとめて格納し、このフレームをウィンドウに配置する方が一般的です。
		
		```python
		radioframe = tk.Frame()
		
		radio = tk.StringVar()
		radio.set("選択肢1")
		
		radiobutton1 = tk.Radiobutton(radioframe, text="選択肢1", variable=radio, value="選択肢1")
		radiobutton2 = tk.Radiobutton(radioframe, text="選択肢2", variable=radio, value="選択肢2")
		radiobutton3 = tk.Radiobutton(radioframe, text="選択肢3", variable=radio, value="選択肢3")
		
		radiobutton1.pack()
		radiobutton2.pack()
		radiobutton3.pack()
		
		radioframe.place(x=100, y=200)
		```	
		
		さらに以下のようにフレーム(Frame)部品（ウィジェット）の代わりにラベルフレーム(LabelFrame)部品（ウィジェット）を使用し、`txt`引数に文字列を指定すると、まとめたラジオボタンの名称を表示させることができます。
		
		```python
		radioframe = tk.LabelFrame(text="選択肢一覧")
		
		radio = tk.StringVar()
		radio.set("選択肢1")
		
		radiobutton1 = tk.Radiobutton(radioframe, text="選択肢1", variable=radio, value="選択肢1")
		radiobutton2 = tk.Radiobutton(radioframe, text="選択肢2", variable=radio, value="選択肢2")
		radiobutton3 = tk.Radiobutton(radioframe, text="選択肢3", variable=radio, value="選択肢3")
		
		radiobutton1.pack()
		radiobutton2.pack()
		radiobutton3.pack()
		
		radioframe.place(x=100, y=200)
		```			
		
		ボタンが押された際に、どのラジオボタンが選択されているかどうかは変数`radio`の`get`メソッドを呼ぶことで取得できます。
		
		```python
		def sub():
			print(f"{radio.get()}が選択されています")
		```	
		
	- リストボックス
	
		複数の選択文字列のリストを作成し、データを選択する部品（ウェジェット）をリストボックスといいます。
		
		ウィンドウにリストボックスを追加するには「リストボックス(ListBox)」という部品（ウィジェット）を作成します。
		
		まず、選択文字列のリストをリストまたはタプルで作成します。
		次に、そのリストまたはタプルを引数`value`に指定して、`tk.StringValue()`を実行し変数`listvar`に設定します。
		この変数`listvar`を`tk.Listbox()`の引数`listvariable`に指定して実行し、変数`listbox`に設定します。
		
		```python
		items = ['りんご', 'いちご', 'バナナ']
		listvar = tk.StringVar(value=items)
		listbox = tk.Listbox(listvariable=listvar)
		```
		
		作成したリストボックスをウィンドウに配置するには`place`メソッドで引数`x`、`y`により位置を指定します。
		
		```python
		listbox.place(x=100, y=200)
		```
		
		ボタンが押された際に、どのリストが選択されているかどうかは、`listbox`の`curselection`メソッドで取得できます。
		この際、戻り値は選択番号が入ったタプルになり、選択されてない場合は空、リストボックス作成時に`selectmode`を"multiple"に設定した場合は複数の値が入ります。
		`selectmode`を指定しなければ、1個しか選択できないのでタプルの先頭の値になります。
		
		リストの内容は`listbox`の`get`メソッドで取得できるので、選択されている文字列は`listbox.get(listbox.curselection[0])`で取得できることになります。
		
		選択されていない場合も考慮すると、ボタンを押されたら選択内容を表示するには以下のようなコードになります。
		
		```python
		def sub():
    		selected = listbox.curselection()
    		if len(selected) == 0:
        		print("選ばれていません")
    		else:
        		print(f"{listbox.get(selected[0])}が選択されています")
        ```
        
        リストの高さのデフォルトは10なので、例えばリストの数に合わせるには`tk.Listbox()`の引数`に`height=len(items)`を追加する必要があります。
        
        リストの幅のデフォルトは20なので、例えばリストの一番大きい文字列の文字数に合わせるには、tk.Listbox()`の引数`に`height=max([len(i)*2 for i in items])`を追加する必要があります。（日本語の場合、2倍する必要があります）
        
        リストの数が多すぎる場合、スクロールバーを設定し、リストボックスとフレームにまとまることで、スクロールバーが設定されたリストボックスを設定することもできます。
        以下にリストボックスに縦スクロールバーを設置したプログラムの例を記載します。
        
		```python
		import tkinter as tk
		from tkinter import ttk
		
		root = tk.Tk()
		root.title("GUIテスト")
		root.geometry("500x300")
		
		def sub():
    		selected = listbox.curselection()
    		if len(selected) == 0:
        		print("選ばれていません")
    		else:
        		print(f"{listbox.get(selected[0])}が選択されています")
        
		btn = tk.Button(text="押してください", command=sub)
		btn.place(x=100, y=50)

		items = ['北海道', '青森', '岩手', '秋田', '宮城', '山形', '福島', '茨城', '栃木', '群馬', '埼玉', '千葉', '東京', '神奈川']
		listvar = tk.StringVar(value=items)

		listframe = tk.Frame()
		listbox = tk.Listbox(listframe, listvariable=listvar, height=6)

		scrollbar = ttk.Scrollbar(listframe, orient='vertical', command=listbox.yview)
		listbox['yscrollcommand'] = scrollbar
		
		listbox.pack(side='left')
		scrollbar.pack(side='right', fill='both')
		listframe.place(x=100, y=100)
		
		root.mainloop()
		```
		
## 演習

それでは実際に**jupyter notebook**を使用して、演習を行います。

コマンドラインから`git pull`を実行して`mcc1`フォルダに最新のファイルをダウンロードしてください。

ターミナルのコマンドラインから`cd mcc1/code/jupyter`を実行して、`jupyter`フォルダに移動し、`jupyter notebook`を実行してください。

すると、ブラウザが起動し、**jupyter**のホーム画面が表示されます。

その中から**Python演習ドリル200基礎練習165〜172.ipynb**をクリックしてください。

そうすると**Python演習ドリル200基礎練習165〜172**というタイトルの演習問題が表示されます。

課題165から課題172までありますので、課題の内容にしたがって、<b>In[]:</b>の部分にPythonプログラムを書いてください。
書き終わったら、画面上の <b>▶| Run</b> というアイコンをクリックすると、今書いたPythonプログラムが実行されます。

出力結果が課題の（実行画面）と一致するか確認してください。

どうしても正解がわからないときは、**▶プログラム例** をクリックすると、正解例のPythonプログラムが表示されます。

## まとめ

今回はPython演習として、GUIの演習を行いました。

チェックボックスやラジオボックスを使えば、以下のように4択のクイズ問題アプリなどを簡単に作ることができます。

```python
import tkinter as tk

root = tk.Tk()
root.title("４択クイズ")
root.geometry("400x150")

def sub():
	if radio.get() == "岩手県":
		label2.configure(text="結果は正解！！")
	else:
		label2.configure(text="結果は不正解")
	
label = tk.Label(text="ドジャースの大谷選手の出身都道府県はどこでしょう")
label.place(x=10, y=10)
       
radioframe = tk.Frame()
radio = tk.StringVar()
		
radiobutton1 = tk.Radiobutton(radioframe, text="北海道", variable=radio, value="北海道")
radiobutton2 = tk.Radiobutton(radioframe, text="青森県", variable=radio, value="青森県")
radiobutton3 = tk.Radiobutton(radioframe, text="岩手県", variable=radio, value="岩手県")
radiobutton4 = tk.Radiobutton(radioframe, text="宮城県", variable=radio, value="宮城県")
		
radiobutton1.pack(side="left")
radiobutton2.pack(side="left")
radiobutton3.pack(side="left")
radiobutton4.pack(side="left")
		
radioframe.place(x=10, y=40)
		
btn = tk.Button(text="答え合わせ", command=sub)
btn.place(x=100, y=70)
		
label2 = tk.Label(text="結果は")
label2.place(x=100, y=120)	
		
root.mainloop()
```

演習の内容と、演習で使わなかったGUI部品も組み合わせていろいろなアプリを作ってみましょう。

今後も新しい演習問題を追加していきますので、演習を通じてPythonを学んでいきましょう。
