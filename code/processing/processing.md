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