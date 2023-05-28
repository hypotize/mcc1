+++
title = "レッスン 24"
date = "2023-05-28T08:30:00+09:00"
author = "小野寺 健"
description = "プロセッシングで遊んでみよ" 
showFullContent = false
readingTime = false
+++

# レッスンの目標
プロセッシング(Processing)であそんでみよう。

プロセッシングについては、このウェブサイトとか参照してください。 [www.d-improvement.jp/learning/processing/](https://www.d-improvement.jp/learning/processing/)

# Processingの基礎
## ウィンドウを作成
### size(w, h): 幅w, 高さh のウィンドウを作成する
  * w: 整数値, 幅（ピクセル）
  * h: 整数値, 高さ（ピクセル）
### Processingの座標系
  * ウィンドウの左上: 原点(0,0)
  * 横方向: X軸方向、右向きが正方向
  * 縦方向: Y軸方向、下向きが正方向
## Processingでの描画方法
### 関数を実行することで、Processingで描画できる
1. 点を描く、線を描く、図形を描く関数
2. 線の色・太さ、塗りつぶしなどのオプションを決める関数
### ウィンドウの大きさを指定して、オプションを決めた後、描画するプログラムを書くのが、Processingの基本
### 線を描くサンプルプログラム
```
size(600, 400)                      # ウィンドウの大きさ
strokeWeight(4.5)                   # 線の太さ
stroke(50.0, 60.0, 200.0)           # 線の色
line(100.0, 100,0, 300.0, 200.0)    # 線を描画
```
## 基本的な描画関数の紹介
### strokeWiegth(w): 線（枠線）の太さをwに設定する
### noStroke(): 線（枠線）を描画しない設定にする
### line(x0, y0, x1, y1): 直線を引く
  * 座標(x0, y0)から、座標(x1, y1)へ線を描画
### rect(x, y, w, h): 長方形を描く
  * 四角形の左上頂点(x, y)とし、幅w、高さhの長方形
### ellipse(x, y, w, h): 楕円を描く
  * 中心座標(x, y)とし、幅w、高さhである楕円を描画
  * 幅と高さを同じ値にすると円となる
### stroke(r, g, b): 線（枠線）の色を設定
### fill(r, g, b): 塗りつぶしの色を設定
  * 赤成分r、緑成分g、青成分bは0から255の値とする
### background(r, g, b): 背景色を設定
  * 赤成分r、緑成分g、青成分bは0から255の値とする
### background(w): 背景色を設定
  * １つの値しか指定しない場合、0（黒）〜255（白）の範囲でグレースケールの背景となる
## 描画の注意
### プログラムは上から下に順番に実行されるため、最初に描いた図形が最背面、最後に描いた図形が最前面となる
### 設定した線の太さ、線の色、塗りつぶし色に関しては、設定を変更しない限り、状態が継続される
### ウィンドウを作成した後、ウィンドウの幅は変数width、ウィンドウの高さは変数heightとして利用できる
  * これらの変数は、Processingが定義している変数なので宣言することなく利用できる
  * ウィンドウの中心の座標は(width/2, height/2)となる
## 練習問題
1. 日本の国旗を描いてください
    * 幅：高さ　＝　３：２
2. オランダの国旗を描いてください
    * 幅：高さ　＝　３：２
3. スイスの国旗を描いてください
    * 幅：高さ　＝　１：１
## 繰り返し処理との融合
### グラデーションの描画例
```
size(810, 300)      # 画面の大きさ
noStroke()          # 枠線を消す
# 色を青色から赤色に変えながら81個の長方形を描画する
for i in range(81):
    fill(i * 255 / 80.0, 0, 255 - i * 255 / 80)
    rect(i * 10, 0, 10, 300)
```
## アニメーションの基礎
### 静止画を高速に切り替えることでアニメーションが実現できる
  * アニメーションにおいて、１秒間あたりに処理させる静止画像（フレーム）数のことをフレームレートとよぶ
  * 単位: fps (60fpsは1秒間に60フレーム切り替えている）
### Processingも同様に、各フレームを高速に切り替えることで、アニメーションを実現する
  * 初期化を行うsetupブロック（setup関数）と、フレームを描画するdrawブロック（draw関数）を定義する
## アニメーションプログラム概要
### setup: 最初に１度だけ実行される
  * ウィンドウのサイズ設定など１度だけ必要な処理をこの中に記述する
## draw: フレームを表示するたびに実行される
  * ここで記載していることがアニメーションで表示される
  * デフォルトでは1秒間に60回実行される
```
def setup():
    # 初期化処理をここに書く
def draw():
    # フレームごとの処理をここに書く
```
## アニメーション例１
```        
def setup():    # 1回だけ実行される
    size(255, 255)          # ウィンドウのサイズ

def draw():     # setupを終えた後、繰り返し実行される
    background(192)         # 背景色で塗りつぶす
    z = frameCount % 256
    fill(z, 255 - z, 255)   # 円の塗りつぶしの色を決める
    ellipse(z, z, 30, 30)   # 円を描画する
```
### frameCount: Processingが用意している特別な変数
  * プログラムが開始されてから表示されたフレーム数を格納
  * 0から始まり、drawが終わると１つ増える
  * 剰余を利用して、変数zの値が0から255となるように設定
## アニメーション例２
```        
def setup():    # 1回だけ実行される
    size(255, 255)          # ウィンドウのサイズ

def draw():     # setupを終えた後、繰り返し実行される
    z = frameCount % 256
    fill(z, 255 - z, 255)   # 円の塗りつぶしの色を決める
    ellipse(z, z, 30, 30)   # 円を描画する
```
### アニメーション例１のプログラムから「background(192)」を削除して実行した場合、どのようになるか確かめてください。また、どうしてそうなるのか、理由を考えてください。
## アニメーション失敗例
```
def setup():    # 1回だけ実行される
    size(255, 255)  # ウィンドウのサイズ

def draw():     # setupを終えた後、繰り返し実行される
    x = 0
    background(192) # 背景色で塗りつぶす
    fill(0, 200, 200)   # 円の塗りつぶしの色を決める
    ellipse(x, x, 30, 30)   # 円を描画する
    x += 1
```
### このプログラムは、アニメーションとしては成立しない
  * その理由を考えてみてください
## グローバル変数
### setup関数、draw関数の外側で変数を宣言することで、プログラム（setup関数、draw関数）のどこからでも使用可能な変数のこと
  * プログラムが終わるまで、変数は存在する
  * draw関数が終わったとしても、値を維持できる
  * 関数の中で宣言した変数はその関数でしか利用できない
```
x = 10  # グローバル変数の宣言
def setup():
    # 初期化処理をここに書く
def draw():
    # フレームごとの処理をここに書く
```
##　グローバル変数の使い方
### 関数中からグローバル変数の値を変更する場合、グローバル変数の値を変更する関数の戦闘にglobal 変数名　と記述する必要がある
```
x = 10  # グローバル変数の宣言
def setup():
    # 初期化処理をここに書く
def draw():
    # フレームごとの処理をここに書く
    global x    # グローバル変数を変更するため
    x += 1      # グローバル変数を変更
```
## アニメーション成功例
```
x = 0   # グローバル変数の宣言
def setup():    # 1回だけ実行される
    size(255, 255)          # ウィンドウのサイズ

def draw():     # setupを終えた後、繰り返し実行される
    global x
    background(192)         # 背景色で塗りつぶす
    fill(0, 200, 200)       # 円の塗りつぶしの色を決める
    ellipse(x, x, 30, 30)   # 円を描画する
    x += 1
    x = x % 255
```
# 実践演習「ハエ叩きゲーム」
## Step0: ウィンドウを設定
### 画面の大きさ、背景色を設定する
  * 以下のプログラムでは
  * 画面の大きさを幅800、高さ800
  * 背景色を白としている
```
def setup():
    size(800, 800)  # ウィンドウのサイズ
def draw():
    background(255) # 背景色を決める
```
## Step1: ハエ叩きをマウスの位置で変更
### ハエ叩きをマウスの位置で変更できるようにする
  * Processingでは、マウスの位置を取得できる特別な変数mouseX, mouseYという変数が存在する
  * ハエ叩きの中心位置の座標を(mouseX, mouseY)にすれば良い
```
def draw():
    background(255)
    sWidth = 20         # ハエ叩きの幅
    sHeight = 20        # ハエ叩きの高さ
    fill(198, 204, 255) # ハエ叩きの色
    # ハエ叩きを描画する
    rect(mouseX - sWidth / 2, mouseY - sHeght / 2, sWidth, sHeight)
```
## Step2: ハエを動かす
### ハエの位置、速度をグローバル変数で宣言し、drawメソッドを更新する
  * 速度は1フレームで動くピクセル量となる
### x方向とy方向の変化量を指定することで、平面を1方向に移動することができる
  * 三角比、ベクトルなどの考え方で以下は自明
  * xとyの変化量が同じ場合、45度の方向で進む
### ハエの位置、速度をグローバル変数として宣言し、drawメソッドを更新する
  * 速度は1フレームで動くピクセル量となる
### グローバル変数の追加箇所
```
fX = 50 # ハエのx座標
fY = 50 # ハエのy座標
fVx = 9 # ハエのx方向に対する更新量
fVy = 2 # ハエのy方向に対する更新量

def setup():
    size(800, 800)  # ウィンドウのサイズ
```
### drawメソッドの追加箇所
```
def draw():
    global fX, fY, fVx, fVy # グローバル変数を変更する
    background(255)
    sWidth = 20             # ハエ叩きの幅
    sHeight = 20            # ハエ叩きの高さ
    fill(198, 204, 255)     # ハエ叩きの色
    # ハエ叩きを描画する
    rect(mouseX - sWidth / 2, mouseY - sHeight / 2, sWidth, sHeight)
    fill(0, 0, 0)           # ハエの色
    ellipse(fX, fY, 10, 10) # ハエを描画する
    fX += fVx               # ハエのx座標を更新する
    fY += fVy               # ハエのy座標を更新する
```
## Step 3: ハエを壁で反射させる
### 上端、下端、左端、右端にハエが衝突した場合、ハエが反射するようにする
  * 「衝突した場合」と「ハエを反射する」をプログラムで表現する
### 「衝突した場合」のプログラム表現
  * 上端に衝突する: ハエのy座標 < 0
  * 下端に衝突する: ハエのy座標 > ウィンドウ高さ
  * 左端に衝突する: ハエのx座標 < 0
  * 右端に衝突する: ハエのx座標 > ウィンドウ幅
### ハエを反射するをプログラムで表現するために
  * 上端に衝突した場合、x方向の速度は変化せず、y方向に速度は逆になる
  * 下端に衝突した場合、x方向の速度は変化せず、y方向に速度は逆になる
  * 左端に衝突した場合、x方向の速度は逆になり、y方向に速度は変化しない
  * 右端に衝突した場合、x方向の速度は逆になり、y方向に速度は変化しない
### まとめると
  * 上端・下端に衝突した場合（ハエのy座標が0より小さい場合、または、ウィンドウ高さより大きい場合）、x方向の速度は変化せず、y方向の速度は逆になる
  * 左端・右端に衝突した場合（ハエのx座標が0より小さい場合、または、ウィンドウ幅より大きい場合）、x方向の速度は逆になり、y方向の速度は変化しない
```
def draw():
    # 途中から
    fill(0, 0, 0)               # ハエの色
    ellipse(fX, fY, 10, 10)     # ハエを描画する
    fX += fVx                   # ハエのx座標を更新する
    fY += fVy                   # ハエのy座標を更新する

    if fY < 0 or fY > height:   # 上下端衝突
        fVy *= -1
    if fX < 0 or fX > width:    # 左右端衝突
        fVx *= -1
```
## Step 4: ハエ叩きとハエの衝突判定
### ハエと壁との衝突判定を参考にして、ハエ叩きとハエの衝突判定を行う
  * ハエ叩き（四角形）の内部にハエが存在するかどうかを条件とすれば良い
### ハエ叩きの左端と上端の座標を求めるとプログラムしやすい
  * ハエ叩きの幅と高さから、ハエ叩きの右端と下端の座標を求めることができる
### 下記のプログラムは衝突したと判断した場合、ハエの位置、速度をランダムな値にしている
  * random(n); 0以上n未満の実数を返す
  * 座標値は整数なので、整数に変換する
```
def draw():
    # 途中から
    if fX < 0 or fX > width:        # 左右端衝突
        fVx *= -1

    sLeft = mouseX - sWidth / 2     # ハエ叩きの左端座標
    sRight = mouseX + sWidth / 2    # ハエ叩きの右端座標
    sTop = mouseY - sHeight / 2     # ハエ叩きの上端座標
    sBottom = mouseY + sHeight / 2  # ハエ叩きの下端座標
    # ハエ叩きとハエの衝突（衝突後、ハエの位置と速度を変更する）
    if sLeft <= fX and sRight >= fX and sTop <= fY and sBottom >= fY:
        fX = int(random(width + 1))
        fY = int(random(height + 1))
        fVx = int(random(10)) + 1
        fVy = int(random(10)) + 1
```
## Step 5: 文字列によるインタラクション
### 画面に文字列を出力させ、ゲームの見栄えを良くする
  * ハエ叩きとハエが衝突した回数を表示する
  * 衝突した回数を保存する変数はグローバル変数とする
### Processingでは、以下の方法で文字列を画面に出力できる
  * textSize(size): 文字の大きさをsizeにする
  * text(data, x, y): 文字列dataを座標(x, y)に出力する
```
count = 0   # 衝突回数
def draw():
    global fX, fYm fVx, fVy, count
    # 中略
    # ハエ叩きとハエの衝突（衝突後、ハエの位置と速度を変更する）
    if sLeft <= fX and sRight >= fX and sTop <= fY and sBottom >= fY:
        # 中略
        fVy = int(random(10)) + 1
        count += 1  # 衝突数を増やす
    # 衝突数を表示する
    textSize(16)
    text(str(count), 20, 20)    # 文字列に変換する
```
## 課題（ゲームの改造）
  * ハエを一定数倒せば、ゲームクリアにする
  * ハエの数を増やす
  * ハエの移動スピードを変化させる
  * ハエ叩きも進入禁止領域を定義し、ハエ叩きがそこに触れるとゲームオーバー」にする
  * 上記以外でも自由な発想でゲームを改造してください


# Processing 実践演習

## 1. 青色の四角形を中央に描く
青色の四角形を中央に描いてみます。
```
def setup():
    size(700,700)
    fill(0,0,255)
def draw():
    rect(width/2, height/2, 100, 100)
```
widthとheightという変数はウィンドウの横と縦の長さが保存されているため、width/2,height/2は画面の中央の座標を表すことになります。

### 問題
このプログラムには問題点があります。中央の座標を指定したにもかかわらず中央より若干右下になってしまっています。これはrect関数が四角形の左上の座標を指定するためです。これを修正し、正しく中央に表示されるようにしてください。

### 解答１
```
def setup():
    size(700,700)
    fill(0,0,255)
def draw():
    rect(width/2-50, height/2-50, 100, 100) # 位置をずらす
```
四角形の高さの半分、幅の半分位置をずらします。

### 解答２
```
def setup():
    size(700,700)
    fill(0,0,255)
    rectMode(CENTER)    # 中央描画モード
def draw():
    rect(width/2, height/2, 100, 100)
```
四角形の描画位置の設定を初期値の「左上」から「中央」に変更します。

## 2. 透明度の選択
processingでは透明度を指定することができます。色を指定する関数（fill関数やbackground関数など）では第３引数まででRGBを指定していました。これに加えて第４引数に透明度として0-255の値を指定できます。**値が大きいほど透明度は低くなります。**
さて、以下のようなコードを考えます。
```
def setup():
    size(700,700)
    background(255,255,255)
    stroke(0,0,0)
def draw():
    fill(255,0,0)
    ellipse(350,300,200,200)
    fill(100,255,0)
    rect(180,150,300,300)
```
コード上では円と四角形の２つの図形を表示しているのですが、実行してみると分かる通り、四角形しか表示されません。これは、円が描画された上にそれより大きい四角形が描画され、覆い被さっているためです。
### 問題
上記のコードを改修して、透明度を指定することにより四角形の下の円が見えるようにしてください。（円の座標を変えるとかはなしです！）
### 解答
```
def setup():
    size(700,700)
    background(255,255,255)
    stroke(0,0,0)
def draw():
    fill(255,0,0)
    ellipse(350,300,200,200)
    fill(100,255,0, 128)    # 透明度追加
    rect(180,150,300,300)
```
四角形の描画色に透明度を追加します。

## 3. 図形を動かす
図形を動かすことを考えてみたいと思います。以下のコードを見て下さい。
```
x = 0   # 円の現在の位置
def setup():
    size(700,700)
    background(255,255,255)
def draw():
    global x
    stroke(0,0,0)
    fill(0,0,255)
    ellipse(x, height/2, 200, 200)
    x += 1
    if x > width:
        x = 0
```
drawブロックは繰り返し実行されるのでxの値は徐々に大きくなっていき、円は右に移動します。でも実行してみると分かる通り、思っていたのと違い、変な軌跡が残ってしまいます。これはProcessingが図形を上書きしていく仕様のために、前に描画したxを増やす前の図形が残ってしまうためです。これを回避するためには、background関数で画面全体を背景色で塗りつぶす方法が有効です。
### 問題
```
background(255,255,255) # 背景色と同じ色を指定
```
上記の画面をクリアするbackground関数を正しい位置に配置して、軌跡が残らないようにしてください。
### 解答
```
def setup():
    size(700,700)
    background(255,255,255)
    stroke(0,0,0)
def draw():
    background(255,255,255) # 背景色で塗りつぶす
    fill(255,0,0)
    ellipse(350,300,200,200)
    fill(100,255,0)
    rect(180,150,300,300)
```
## 4. 画像を読み込んで動かす
以下のコードをエディタに貼り付けて、一度保存して下さい。
```
def setup():
    global img
    size(700,700)
    img = loadImage("cat.png")
def draw():
    background(200)
    image(img, mouseX, mouseY, 150, 150)
```
次にネコのイラストを適当なサイトからダウンロードし、コードを保存したフォルダと同じフォルダに「cat.png」として保存して下さい。そうした状態で実行すると、猫がマウスに追従するプログラムが動きます。
## 5. 赤色の円を円周上に動かす
ちょっとわかりづらいですが、赤色の円を動かして、さらにそれをぐるぐる円を描くように回転させてみます。さて、そのプログラムはこちらです。
```
degree = 0
r = 150
def setup():
    size(700,700)
    background(0,0,0)
def draw():
    global degree, r
    fill(0,0,0)
    rect(0,0,width,height)
    degree += 5
    if degree >= 360:
        degree = 0
    rad = radians(degree)
    x = width/2 + r * cos(rad)
    y = height/2 + r * sin(rad)
    fill(255,0,0)
    ellipse(x,y,100,100)
```
### 問題
上のプログラムを改修し、楕円を描くように動くようにしてください。楕円の大きさは自由で構いません。
#### ヒント
今は半径rを用意して円の座標x,yを計算していますが、楕円の場合、半径rの代わりに長半径と短半径を指定する新たな変数a,bを用意します。楕円の式は以下の通りです。
```
x = a * cos(rad)
y = b * sin(rad)
```
## 6. ループ
さて、繰り返し処理を利用したプログラムを作ってみます。以下のプログラムはランダムな色の円を横一列に並べるプログラムです。
```
N = 10
def setup():
    size(700,350)
    background(0,0,0)
    colorMode(HSB,360,255,255)
    noStrike()
    fill(color(random(360),200,200))
def draw():
    for i in range(1, N+1):
        spanx = width / N
        d = (width / 2) / N
        ellipse(i * spanx - d, height/2, d, d)
```
実行すると円が10個横に並んだ画像が出力されます。for文ではループの回数を重ねる毎に自動的に変数iを増やすことが出来ます。Nは描く円の数を表しています。変えるとどうなるかぜひ試してみてください。
### 問題
先のプログラムを改造して円が縦に並ぶようにして下さい。
#### ヒント
for文の中に、y方向の間隔を保存する変数spanyを作成し、widthからspanxを求めるコードを参考にしてみてください。
### 解答
```
N = 10
def setup():
    size(700,350)
    background(0,0,0)
    colorMode(HSB,360,255,255)
    noStrike()
    fill(color(random(360),200,200))
def draw():
    for i in range(1, N+1):
        spany = height / N
        d = (height / 2) / N
        ellipse(width/2, i * spany - d, d, d)
```
## 7. マウスの検出
マウスがクリックされたときに何かアクションをするといったプログラムを考えます。Processingではマウスのクリックやマウスの位置を検出する機能があります。以下のコードを見て下さい。
```
ripList = []
def setup():
    size(700,700)
    colorMode(HSB,360,255,255)
    background(0,0,0)
def draw():
    global ripList
    fade()
    for rip in ripList:
        rip.update()
        rip.display()
    ripList = [rip for rip in ripList if rip.getDiameter() <= width]
def mousePressed():
    global ripList
    ripList.append(Ripple(width/2,height/2))
def fade():
    noStroke()
    fill(0,0,0,50)
    rect(0,0,width,height)
class Ripple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.d = 1
        self.c = color(random(360), 200, 200)
    def getDiameter(self):
        return self.d
    def setDiameter(self, d):
        self.d = d
    def update(self):
        self.d += 5.0
    def display(self):
        noFill()
        stroke(self.c)
        strokeWeight(5)
        ellipse(self.x, self,y, self.d, self.d)
```
マウスのクリックを検出するとランダムな色の波紋を生成するプログラムです。実行してウィンドウ上で適当に何度かクリックしてみて下さい。

Processingにはsetupブロックとdrawブロックに加えて**mousePressedブロック**が用意されています。このブロックには名前の通り、マウスがクリックされた時の動作が記述できます。今回の場合、プログラムの詳細は省きますが、簡単には波紋を追加する命令を書いています。そのため、クリックされる度に波紋が増える処理が実現できました。
### 問題
上記のプログラムでは、画面上のどこをクリックしても画面の中心から波紋が生成されていました。これは波紋を生成する座標を（width/2,height/2）としたためです。これを改変して、画面をクリックしたところを中心に波紋を生成するようにしてください。現在のマウスの位置は、**mouseX**,**mouseY**で取得できます。
### 解答
```
def mousePressed():
    global ripList
    ripList.append(Ripple(mouseX,mouseY))
```
上記ブロックを変更します
## 8.ランダムの利用
次のプログラムを実行してみてください。
```
import random
cirList = []
def setup():
    size(1280, 720)
    colorMode(HSB,360,100,100)
    background(0)
    noStroke()
def draw():
    global cirList
    if random.random() < 0.75:
        cirList.append(Circle(random(width),random(height),0,color(180,50,100))
    updateCircles()
    drawCircles()
    fade()
def updateCircles():
    global cirList
    vRadius = 5.0
    maxSize = 100
    for cir in cirList:
        cir.setRadius(cir.getRadius + vRadius)
    cirList = [cir for cir in cirList if cir.getRadius <= maxSize]
def drawCircles():
    for cir in cirList:
        cir.draw()
def fade():
    fill(0,0,0,15)
    rect(0,0,width,height)
class Circle:
    def __init__(self, x, y, r, c):
        self.x = x
        self.y = y
        self.r = r
        self.c = c
    def setRadius(self, r):
        self.r = r
    def getRadius(self):
        return self.r
    def draw(self):
        fill(self.c)
        ellipse(self.x,self.y,self.r,self.r)
```
random関数を利用することでランダムな位置に円を表示させています。random関数の使い方は以下の通りです。
```
random(50)  # 0<=x<50のランダムな小数
random(20,100)  # 20<=x<100のランダムな小数
int(random(30)) # 0<=n<30のランダムな整数
random.random() # 0<=x<1のランダムな小数
```
### 問題
ランダムな位置に表示させることは出来ましたが、色についてもランダムになるようにプログラムを改変してください。
#### ヒント
draw関数内の一部のパラメータをランダムにします。
### 解答
```
def draw():
    global cirList
    if random.random() < 0.75:
        cirList.append(Circle(random(width),random(height),0,color(random(255),random(255),random(255)ｒ))
    updateCircles()
    drawCircles()
    fade()
```
## 9. 再帰関数
次のプログラムを実行してみてください。
```
def setup():
    size(700,700)
    translate(width/2, height/2)
    circlesR(0,0,350,4)
def draw():
    pass
def circlesR(x, y, r, n):
    ellipse(x,y,r*2,r*2)
    if n <= 1:
        return
    newR = r/2
    circlesR(x+newR,y,newR,n-1)
    circlesR(x-newR,y,newR,n-1)
```
circleR関数に着目すると、関数内でcircleR自身をまた呼び出していることが分かります。このような関数を一般に**再帰関数**と呼びます。再帰関数は「深さ優先探索」と呼ばれるアルゴリズムを実装したり、数学の漸化式を解いたり出来ます。circlesRの動きを追っていくと、円を描いてその円の内側にさらに２つの円を描いて...を繰り返していることが分かると思います。setup関数内で呼び出しているcirclesR関数の第４引数（今は4になっている）を書き換えるとどんな風になるかも試してみてください。
### 問題
上記のプログラムでは円の内側に左右２つの円を配置していました。これを改造して円の上下左右に配置するようにして、n=6で実行してみてください。
### 解答
```
def setup():
    size(700,700)
    translate(width/2, height/2)
    circlesR(0,0,350,6)
def draw():
    pass
def circlesR(x, y, r, n):
    ellipse(x,y,r*2,r*2)
    if n <= 1:
        return
    newR = r/2
    circlesR(x+newR,y,newR,n-1)
    circlesR(x-newR,y,newR,n-1)
    circlesR(x,y+newR,newR,n-1)
    circlesR(x,y-newR,newR,n-1)
```
## 10. フラクタル
再帰関数を応用してフラクタルを作ってみます。次のプログラムを実行してみてください。
```
def setup():
    size(700,700)
    gen = FractalGenerator()
    gen.add(PVector(50,450))
    gen.add(PVector(200,450))
    gen.add(PVector(220,150))
    gen.add(PVector(240,450))
    gen.add(PVector(650,450))
    gen.show(1)
def draw():
    pass
class FractalGenerator:
    def __init__(self):
        self.vecs = []
        self.p0 = None
        self.pp = None
        self.v0 = None
    def add(self, p):
        if self.p0 is None:
            self.p0 = p
            self.pp = p
            return
        self.vecs.append(PVector.sub(p,self.pp))
        self.v0 = PVector.sub(p, self.p0)
        self.pp = p
    def show(self, n):
        pushMatrix()
        translate(self.p0.x, self.p0.y)
        rotate(self.v0.heading())
        self.rec(1, n)
        popMatrix()
    def rec(self, rate, n):
        pushMatrix()
        pRad = self.v0.heading()
        for v in self.vecs:
            rad = v.heading()
            l = v.mag()
            rotate(rad - pRad)
            if n == 1:
                line(0,0,rate*l,0)
            else:
                self.rec(rate*l/self.v0.mag(),n-1)
            translate(rate*l,0)
            pRad = rad
        popMatrix()
```
何の変哲もない図形が表示されます。
次に上記コードを以下のように変えて再度実行してみてください。
```
gen.show(1)
→
gen.show(2)
```
この画像をよく観察すると、初めの図形の各辺を図形自身に置き換えたものだと分かります。さらに次のようにコードを変えます。
```
gen.show(2)
→
gen.show(5)
```
数字は各辺を自分自身で書き換える回数を指定していました。このように自己相似形を繰り返し発見できる図形のことを一般にフラクタルと呼びます。
### 問題
**コッホの曲線**と呼ばれる曲線をインターネット上で調べ、上記プログラムを変更してn=5になるコッホの曲線を作成してください。
#### ヒント
setup関数内で指定している座標値を変更し、nの値を5にすればコッホの曲線を描画することができます。

