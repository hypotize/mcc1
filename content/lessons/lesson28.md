+++
title = "レッスン 28"
date = "2024-02-04T9:00:00+09:00"
author = "小野寺 健"
description = "HTMLでスライドショーを作ろう" 
showFullContent = false
readingTime = false
tags = ["HTML", "スライドショー", "CSS", "中級"]
+++
# レッスンの目標
HTMLでスライドショーを作ろう
## ファイルをコピーする
コマンドラインから以下のコマンドでindex.htmlとstylesheet.cssをそれぞれindex2.html、stylesheet2.cssにコピーします。
```
cp index.html index2.html
cp stylesheet.css stylesheet2.css
```
## index2.htmlの書き換え
`index2.html`を以下のように書き換えます。
### header部分の変更
参照するスタイルシートを`stylesheet.css`から`stylesheet2.css`に書き換えます。
```html
	<link rel="stylesheet" href="stylesheet2.css">
```
### `<table></table>`の書き換え
`<table>...</table>`を`<div class="slider">...</div>`に書き換えます。
### `<tr></tr>`の削除と`<td></td>`の書き換え
`<tr>...</tr>`は不要なので削除します。
`<td>...</td>`を`<div class="slider-item">...</div>`に書き換えます。
その際、テキストファイルは`<br>をつけてイメージファイルの直後に書くように変更します。
```html
index.html
	<tr>
		<td>
			<img src="photo/azusa01.jpeg">
		</td>
		<td>
				<img src="photo/azusa02.jpeg">
		</td>
		<td>
			<img src="photo/azusa03.jpeg">
		</td>
	</tr>
	<tr>
		<td>
			アルマジロ
		</td>
		<td>
			フェネック
		</td>
		<td>
			カワウソ
		</td>
	</tr>
```
```html
index2.html
	<div class="slider-item">
		<img src="photo/azusa01.jpeg"><br>
		アルマジロ
	</div>
	<div class="slider-item">
		<img src="photo/azusa02.jpeg"><br>
		フェネック
	</div>
	<div class="slider-item">
		<img src="photo/azusa03.jpeg"><br>
		カワウソ
	</div>
```
すべての画像について上記のように変更しましょう。
以上で`index2.html`ファイルの書き換えは終了です。
## stylesheet2.cssの書き換え
`stylesheet2.css`を以下のように書き換えます。
### imgのwidthの変更
1枚ずつ画像を表示する場合、今の画像幅はちょっと小さいので`300px`から`400px`に変更します。
```css
img {
	width: 400px;
}
```
### .sliderの追加
以下のようにスライドショーの画面設定を追加します。
```css
.slider {
	width: 400px;
	text-align: center;
	display: flex;
	overflow: hidden;
	margin: 0 auto;
}
```
`width`は画像の幅と同じサイズにすることで画像幅ちょうどに表示されます。
`td`の部分に設定してあった文字の配置(text-align）を`.slider`にも追加します。ちなみに`td`の部分は今回は使用しないので削除しても構いません。
この値を例えば2倍の`800px`にすると次の画像が並んで2枚ずつ表示されるようになります。
この際、画像が並んで表示されるのは`display`を`flex`に設定しているからです。
また、`overflow`を`hidden`にすることで画像が終了したら何も表示されなくなります。
### .slider > :first-childの追加
スライドショーのアニメーション設定を追加します。
```css
.slider > :first-child {
  animation-name: scroll;
  animation-duration: 100s;
  animation-delay: 5s;
  animation-iteration-count: infinite;
}
```
`animation-name`では後で設定する`@keyframes`のどれを使用するかを指定します。ここでが`scroll`という名前の`@keyframes`を使用するので`scroll`を指定しています。
`animation-duration`では何秒間かけて全体のアニメーションを行うかを指定します。ここでは`100s`に指定しています。
`animation-delay`では何秒後にアニメーションを開始するかを指定します。ここでは`5s`を指定しています。
`animation-iteration-count`ではアニメーションを何回繰り返すかを指定します。
ここでは`infinite`（無限）を指定しています。
### @keyframe（アニメーションの変化）の追加
スライドショーのアニメーションの変化を追加します。
```css
@keyframes scroll {
0% {
  margin-left: 0;
}

4% {
  margin-left: -100%;
}

8% {
  margin-left: -200%;
}
...
96% {
  margin-left: -2400%;
}
}
```
%の部分は100%の時間に対してどの時間にどのような画面を表示するかを指定します。
今回画像は24枚あるので、各画像に4%ずつ表示時間を割り当てています。
また画像は横に繋がっているので`-100%`ずつ値を増やすことで1枚ずつ画像が左にずれていくようになります。

すべての画像分(0%から96%まで4%おきに-100%ずつ増やして24個分作成）書き加えたら終了です。
## 画像の表示
index2.htmlをブラウザ(FireFox)で表示してみましょう。
正しく表示されましたか？
