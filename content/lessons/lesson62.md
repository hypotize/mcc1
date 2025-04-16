+++
title = "レッスン 62"
date = "2025-04-14T08:30:00+09:00"
author = "小野寺 健"
description = "Pygameで遊んでみよ" 
showFullContent = false
readingTime = false
tags = ["プログラミング", "Pygame", "Python", "上級"]
+++

# レッスンの目標

Pygameであそんでみよう。

Pygameについては、このウェブサイトとか参照してください。 [http://westplain.sakuraweb.com/translate/pygame/](http://westplain.sakuraweb.com/translate/pygame/)

# Pygameの基礎

## ウィンドウを作成

### pygame.display.set_mode((w, h)): 幅w, 高さh のウィンドウを作成する

* w: 整数値, 幅（ピクセル）

* h: 整数値, 高さ（ピクセル）

### Pygameの座標系

* ウィンドウの左上: 原点(0,0)

* 横方向: X軸方向、右向きが正方向

* 縦方向: Y軸方向、下向きが正方向

## Pygameでの描画方法

### 関数を実行することで、Pygameで描画できる

* 点を描く、線を描く、図形を描く関数

* この関数に線または塗りつぶしの色、指定なし（塗りつぶし）または線の太さなどの引数を指定する

#### ウィンドウの大きさを指定した後、「背景を描画（クリア）し、図形を描画し、ウィンドウを更新し、フレーム数分待つ」を繰り返すのがPygameの基本

### 基本のプログラム

```python
import sys        # プログラムを終了する関数sys.exit()を使用する
import pygame    # Pygameを使用する
from pygame.locals import QUIT    # ウィンドウを閉じた時のコード

# 最初に1度だけ実行される部分
pygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((600, 400))    # 600x400のウィンドウを作成し、SURFACE変数に設定
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数

def main():    # メイン関数
    # 必要ならこの部分にも1度だけ実行される部分を記載する
    while True:    # ずっと
        for event in pygame.event.get():
            if event.type == QUIT:    # ウィンドウを閉じたらプログラムを終了する
                pygame.quit()
                sys.exit()

        # フレームを表示するたびに実行される部分
        SURFACE.fill((255, 255, 255))    # 背景を白で描画（クリア）する
          # ここで図形を描画する

        pygame.display.update()    # ウィンドウを更新
        FPSCLOCK.tick(3)    # １秒に3回フレームを更新する

if __name__ == '__main__':    # メイン関数を呼ぶ
    main()
```

上記基本のプログラムはmcc1/code/python/pygameの下にsample.pyという名前で作成済みです。

このファイルをコピーして、名前を変え、「# ここで図形を描画する」の部分を書き換えていろいろな図形を描画してみましょう。

### 線を描画するサンプルプログラム

sample.pyをコピーしてline.pyという名前に変更し、「# ここで図形を描画する」の部分を`pygame.draw.line(SURFACE, (50.0, 60.0, 200.0), (100.0, 100.0), (300.0, 200.0), 4.5)`に書き換えてます。

```python
import sys        # プログラムを終了する関数sys.exit()を使用する
import pygame    # Pygameを使用する
from pygame.locals import QUIT    # ウィンドウを閉じた時のコード

# 最初に1度だけ実行される部分
pygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((600, 400))    # 600x400のウィンドウを作成し、SURFACE変数に設定
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数

def main():    # メイン関数
    # 必要ならこの部分にも1度だけ実行される部分を記載する
    while True:    # ずっと
        for event in pygame.event.get():
            if event.type == QUIT:    # ウィンドウを閉じたらプログラムを終了する
                pygame.quit()
                sys.exit()

        
        SURFACE.fill((255, 255, 255))    # 背景を白で描画（クリア）する
        pygame.draw.line(SURFACE, (50, 60, 200), (100, 100), (300, 200), 5)
          # 引数(ウィンドウ, 線の色, 線の始点, 線の終点, 線の太さ)

        pygame.display.update()    # ウィンドウを更新
        FPSCLOCK.tick(3)    # １秒に3回フレームを更新する

if __name__ == '__main__':    # メイン関数を呼ぶ
    main()
```

コマンドラインから`python3 line.py`を実行し、青い線が右斜め下方向に引かれます。

## 基本的な描画関数の紹介

以下に基本的な描画関数を紹介するので、sample.pyをコピーして名前に変更し、「# ここで図形を描画する」の部分を書き換えていろいろな図形を描画してみましょう。

### pygame.drawline(SURFACE, (r, g, b), (x0, y0), (x1, y1), lw): 直線を引く

* SURFACE（ウィンドウ）に、座標(x0, y0)から、座標(x1, y1)へ、(r, g, b)色で、lwの幅の線を描画する

### pygame.draw.rect(SURFACE, (r, g, b), (x, y, w, h)): 長方形を描く（塗りつぶす）

* SURFACE（ウィンドウ）に、四角形の左上頂点(x, y)とし、幅w、高さhの長方形を(r, g, b)色で塗りつぶす

### pygame.draw.rect(SURFACE, (r, g, b), (x, y, w, h), lw): 長方形を描く（枠線を引く）

* SURFACE（ウィンドウ）に、四角形の左上頂点(x, y)とし、幅w、高さhの長方形を(r, g, b)色で、lwの幅の枠線を描画する

### pygame.draw.circle(SURFACE, (r, g, b), (x, y), r): 円を描く（塗りつぶす）

* 中心座標(x, y)とし、半径rの円を(r, g, b)色で塗りつぶす

### pygame.draw.circle(SURFACE, (r, g, b), (x, y), r, lw): 円を描く（枠線を引く）

* 中心座標(x, y)とし、半径rの円を(r, g, b)色で、lwの幅の枠線を描画する

### pygame.draw.ellipse(SURFACE, (r, g, b), (x, y, w, h)): 楕円を描く（塗りつぶす）

* 中心座標(x, y)とし、幅w、高さhである楕円を(r, g, b)色で塗りつぶす。

### pygame.draw.ellipse(SURFACE, (r, g, b), (x, y, w, h), lw): 楕円を描く（枠線を引く）

* 中心座標(x, y)とし、幅w、高さhである楕円を(r, g, b)色で、lwの幅の枠線を描画する

### SURFACE.fill(r, g, b): 背景色を設定

* 赤成分r、緑成分g、青成分bは0から255の値とする

## 描画の注意

プログラムは上から下に順番に実行されるため、最初に描いた図形が最背面、最後に描いた図形が最前面となる

設定した線の太さ、線の色、塗りつぶし色に関しては、設定を変更しない限り、状態が継続される

ウィンドウを作成した後、ウィンドウの幅と高さはSURFACE.get_size()で取得できる。

* ウィンドウの幅だけはSURFACE.get_width()、ウィンドウの高さだけはSURFACE.get_height()で個々に取得することもできる。
* ウィンドウの中心の座標は(ウィンドウの幅/2, ウィンドウの高さ/2)となる

## 練習問題

1. 日本の国旗を描いてください
   * 幅：高さ　＝　３：２
2. オランダの国旗を描いてください
   * 幅：高さ　＝　３：２
3. スイスの国旗を描いてください
   * 幅：高さ　＝　１：１

## 繰り返し処理との融合

### グラデーションの描画例

sample.pyをコピーし、`SURFACE = pygame.display.set_mode((600, 400)) `の部分と`# ここで図形を描画する`の部分を以下のように書き換えてみましょう。

```python
...(前略)
SURFACE = pygame.display.set_mode((810, 300))     # 画面の大きさ
        ...(中略)
        # 色を青色から赤色に変えながら81個の長方形を描画する
        for i in range(81):
            pygame.draw.rect(SURFACE, (i * 255 // 80, 0, 255 - i * 255 // 80),
                (i * 10, 0, 10, 300))    # 塗りつぶし
        ...(後略)
```

## アニメーションの基礎

### 静止画を高速に切り替えることでアニメーションが実現できる

* アニメーションにおいて、１秒間あたりに処理させる静止画像（フレーム）数のことをフレームレートとよぶ

* 単位: fps (60fpsは1秒間に60フレーム切り替えている）

### Pygameも同様に、各フレームを高速に切り替えることで、アニメーションを実現する

* FPSClock.tick()関数にフレーム数(fps)を設定する

## アニメーションプログラム概要

### 最初に１度だけ実行される部分

* ウィンドウのサイズ設定など１度だけ必要な処理をこの部分に記述する
* main()関数の最初の部分に記載することもできる

## フレームを表示するたびに実行される部分

* この部分で記載していることがアニメーションで表示される

```python
import sys        # プログラムを終了する関数sys.exit()を使用する
import pygame    # Pygameを使用する
from pygame.locals.import QUIT    # ウィンドウを閉じた時のコード

# 最初に1度だけ実行される部分
pygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((600, 400))    # 600x400のウィンドウを作成し、SURFACE変数に設定
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数

def main():    # メイン関数
    # 必要ならこの部分にも1度だけ実行される部分を記載する
    while True:    # ずっと
        for event in pygame.event.get():
            if event.type == QUIT:    # ウィンドウを閉じたらプログラムを終了する
                pygame.quit()
                sys.exit()

        # フレームを表示するたびに実行される部分
        SURFACE.fill((255, 255, 255))    # 背景を白で描画（クリア）する
        # ここで図形を描画する

        pygame.display.update()    # ウィンドウを更新
        FPSCLOCK.tick(60)    # フレームの更新頻度を制御する（1秒間に60回）

if __name__ == '__main__':    # メイン関数を呼ぶ
    main()
```

## アニメーション例１

sample.pyをコピーし、`# 最初に1度だけ実行される部分`、`# 必要ならこの部分にも1度だけ実行される部分を記載する`、および`# フレームを表示するたびに実行される部分`を以下のように書き換えて、簡単なアニメーションを作ってみましょう。

```python
...(前略)
# 最初に1度だけ実行される部分
pygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((255, 255))    # ウィンドウのサイズ
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数
...(中略)
def main():
    # 必要ならこの部分にも1度だけ実行される部分を記載する
    frameCount = 0    # フレームのカウンタ
    ...(中略)
        # フレームを表示するたびに実行される部分
        SURFACE.fill((192, 192, 192))    # 背景色で塗りつぶす
        z = frameCount % 256
        pygame.draw.circle(SURFACE, (z, 255 - z, 255), (z, z), 30)    # 円を描画する
        frameCount += 1

        pygame.display.update()    # ウィンドウを更新
        FPSCLOCK.tick(60)    # １秒に60回フレームを更新する
        ...(後略)
```

実行すると左上から右下に円が色を変えながら動いていきます。 

* frameCountという変数を用意し、フレームを表示するたびに１つずつ増えるようにしています。
* 剰余を利用して、変数zの値が0から255となるように設定しています。

## アニメーション例２

```python
...(前略)
# 最初に1度だけ実行される部分
pygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((255, 255))    # ウィンドウのサイズ
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数
...(中略)
def main():
    # 必要ならこの部分にも1度だけ実行される部分を記載する
    frameCount = 0    # フレームのカウンタ
    ...(中略)
        # フレームを表示するたびに実行される部分
        z = frameCount % 256
        pygame.draw.circle(SURFACE, (z, 255 - z, 255), (z, z), 30)    # 円を描画する
        frameCount += 1

        pygame.display.update()    # ウィンドウを更新
        FPSCLOCK.tick(60)    # １秒に60回フレームを更新する
        ...(後略)
```

アニメーション例１のプログラムから「background(192)」を削除して実行した場合、どのようになるか確かめてください。また、どうしてそうなるのか、理由を考えてください。

# Pygame 実践演習1「ハエ叩きゲーム」

## Step0: ウィンドウを設定

### 画面の大きさ、背景色を設定する

sample.pyをコピーして以下のように書き換えます。

```python
...(前略)
# 最初に1度だけ実行される部分
pygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((800, 800))    # 画面の大きさは幅800、高さ800
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数
...(中略)
        # フレームを表示するたびに実行される部分
        SURFACE.fill((255, 255, 255))    # 背景を白で描画（クリア）する
        # ここで図形を描画する    

        pygame.display.update()    # ウィンドウを更新
        FPSCLOCK.tick(60)    # １秒に60回フレームを更新する
        ...(後略)
```

上記のプログラムでは、画面の大きさを幅800、高さ800にし、背景色を白として 、フレームレートを60fps（1秒間に60フレーム）にしています。

## Step1: ハエ叩きをマウスの位置で変更

### ハエ叩きをマウスの位置で変更できるようにする

* Pygameではpygame.mouse.get_pos()という関数でマウスの位置（x座標とy座標の値）を取得することができます。
* ハエ叩きの中心位置の座標を上記関数で取得したマウスの座標にします。

```python
...(前略)
def main():
    # 必要ならこの部分にも1度だけ実行される部分を記載する
    sWidth = 20    # ハエ叩きの幅
    sHeight = 20    # ハエ叩きの高さ
    sColor = (198, 204, 255)    # ハエ叩きの色
        ...(中略)
        # フレームを表示するたびに実行される部分
        SURFACE.fill((255, 255, 255))    # 背景を白で描画（クリア）する
        x, y = pygame.mouse.get_pos()
        pygame.draw.rect(SURFACE, sColor, (x - sWidth // 2, y - sHeight // 2, sWidth, sHeight))
        ...(後略)
```

マウスを動かすとハエ叩き（四角）がマウスに合わせて移動していることがわかります。

## Step2: ハエを動かす

### ハエの位置、変化量を設定する

* 速度は1フレームで動くピクセル量となる

### x方向とy方向の変化量を指定することで、平面を1方向に移動することができる

* x方向の変化量とy方向の変化量をいろいろ変えることで、いろいろな方向に移動する。

* 例えば、x方向の変化量とy方向の変化量が同じ場合、45度の方向で進む

### ハエの位置、変化量に合わせてハエを移動するようにする

* ハエは半径5の円の黒い円にする

* 描画するたびにハエの位置を変化量にあわせて移動させる

### 変数の追加箇所

```python
...(前略)
def main():
    # 必要ならこの部分にも1度だけ実行される部分を記載する
    fX = 50 # ハエのx座標
    fY = 50 # ハエのy座標
    fVx = 9 # ハエのx方向に対する更新量
    fVy = 2 # ハエのy方向に対する更新量
    ...(後略)
```

### ハエの移動の追加箇所

```python
        ...(前略)
        # フレームを表示するたびに実行される部分
        SURFACE.fill((255, 255, 255))    # 背景を白で描画（クリア）する
        x, y = pygame.mouse.get_pos()
        pygame.draw.rect(SURFACE, sColor, (x - sWidth // 2, y - sHeight // 2, sWidth, sHeight))
        pygame.draw.circle(SURFACE, (0, 0, 0), (fX, fY), 5)    # ハエを描画する
        fX += fVx               # ハエのx座標を更新する
        fY += fVy               # ハエのy座標を更新する
        ...(後略)
```

ハエに見たてた小さい円が右斜め下方向に移動していきます。

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

```python
...(前略)
def main():
     # 必要ならこの部分にも1度だけ実行される部分を記載する
     height, width = SURFACE.get_size()
        ...(中略)
        pygame.draw.circle(SURFACE, (0, 0, 0), (fX, fY), 5)    # ハエを描画する
        fX += fVx               # ハエのx座標を更新する
        fY += fVy               # ハエのy座標を更新する

        if fY < 0 or fY > height:    # 上下端衝突
            fVy *= -1
        if fX < 0 or fX > width:    # 左右端衝突
            fVx *= -1
        ...(後略)
```

ハエが壁に衝突するとはねかえるようになります。

## Step 4: ハエ叩きとハエの衝突判定

### ハエと壁との衝突判定を参考にして、ハエ叩きとハエの衝突判定を行う

* ハエ叩き（四角形）の内部にハエが存在するかどうかを条件とすれば良い

### ハエ叩きの左端と上端の座標を求めるとプログラムしやすい

* ハエ叩きの幅と高さから、ハエ叩きの右端と下端の座標を求めることができる

### 下記のプログラムは衝突したと判断した場合、ハエの位置、速度をランダムな値にする

* randrange(n); 0以上n未満の数を返す（from random import randrangeが必要）

* 座標値は整数なので、整数に変換する

```python
...(前略)
from random import randrange
         ... (中略)
        if fX < 0 or fX > SURFACE.get_width():    # 左右端衝突
            fVx *= -1

        sLeft = x - sWidth // 2    # ハエ叩きの左端座標
        sRight = x + sWidth // 2    # ハエ叩きの右端座標
        sTop = y - sHeight // 2    # ハエ叩きの上端座標
        sBottom = y + sHeight // 2    # ハエ叩きの下端座標
        # ハエ叩きとハエの衝突（衝突後、ハエの位置と速度を変更する）
        if sLeft <= fX and sRight >= fX and sTop <= fY and sBottom >= fY:
            fX = randrange(width + 1)
            fY = randrange(height + 1)
            fVx = randrange(10) + 1
            fVy = randrange(10) + 1        
        ...(後略)
```

ハエがハエ叩きに衝突すると、ハエがランダムな場所から現れ、ランダムな方向に移動する。

## Step 5: 文字列によるインタラクション

### 画面に文字列を出力させ、ゲームの見栄えを良くする

* ハエ叩きとハエが衝突した回数用の変数を作成し、画面に表示する

### Pygameでは、以下の方法で文字列を画面に出力できる

* font = pygame.font.SysFont(None, size)
  
  * フォントの大きさを指定する
  
  * フォントは毎回変わらないので、1回だけ指定する

* text = font.render(data, True, color)
  
  * 文字列dataと色を指定する

* SURFACE.blit(text, (x, y))
  
  * 指定の文字を座標(x, y)に描画する
  
  * 座標は文字の左上の位置

```python
...(前略)
def main():
    # 必要ならこの部分にも1度だけ実行される部分を記載する
    count = 0    # 衝突回数
    font = pygame.font.SysFont(None, 16)
    ...(中略)
        # ハエ叩きとハエの衝突（衝突後、ハエの位置と速度を変更する）
        if sLeft <= fX and sRight >= fX and sTop <= fY and sBottom >= fY:
            ...(中略)
            fVy = randrange(10) + 1
            count += 1  # 衝突数を増やす

        # 衝突数を表示する
        text = font.render(str(count), True, (0, 0, 0))
        SURFACE.blit(text, (20, 20))    # 文字列を表示する
        ...(後略)
```

画面の左上にハエとハエ叩きの衝突数が表示され、衝突すると値が増えます。

## 課題（ゲームの改造）

* ハエを一定数倒せば、ゲームクリアにする
* ハエの数を増やす
* ハエの移動スピードを途中で変化させる
* ハエ叩きの進入禁止領域を定義し、ハエ叩きがそこに触れるとゲームオーバーにする
* 上記以外でも自由な発想でゲームを改造してください

# Pygame 実践演習 2

## 1. 青色の四角形を中央に描く

sample.pyをコピーして、青色の四角形を中央に描いてみます。

```python
...(前略)
# 最初に1度だけ実行される部分
Spygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((700, 700))
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数
...(中略)
def main():
    # 必要ならこの部分にも1度だけ実行される部分を記載する
    width, height = SURFACE.get_size()
    ...(中略)
        # フレームを表示するたびに実行される部分
        SURFACE.fill((255, 255, 255))    # 背景を白で描画（クリア）する
        pygame.draw.rect(SURFACE, (0, 0, 255), (width // 2, height // 2, 100, 100))
    ...(後略) 
```

widthとheightという変数はウィンドウの横と縦の長さなので、width/2,height/2は画面の中央の座標を表すことになります。

### 問題

このプログラムには問題点があります。中央の座標を指定したにもかかわらず中央より若干右下になってしまっています。これはrect関数が四角形の左上の座標を指定するためです。これを修正し、正しく中央に表示されるようにしてください。

### 解答１

```python
    ...(前略)
        # フレームを表示するたびに実行される部分
        SURFACE.fill((255, 255, 255))    # 背景を白で描画（クリア）する
        Pygame.draw.rect(SURFACE, (0, 0, 255), (width // 2 - 50, height // 2 -50, 100, 100)) 
    ...(後略) 
```

四角形の高さの半分、幅の半分位置をずらします。

### 解答２

```python
...(前略)
from pygame.locals import QUIT, Rect
    ...(中略)
        # フレームを表示するたびに実行される部分
        SURFACE.fill((255, 255, 255))    # 背景を白で描画（クリア）する
        rect = Rect(0, 0, 100, 100)
        rect.center = (width // 2, height // 2)
        Pygame.draw.rect(SURFACE, (0, 0, 255), rect) 
    ...(後略) 
```

四角形をRect(x, y, h, w)で最初(0, 0)の位置に指定し、rect.center = (x, y)で中心位置を指定し直します。

プログラムは長くなりますが、高さの半分、幅の半分などを計算する必要がなくなります。

## 2. 透明度の選択

Pygameでは透明度を指定することができます。色を指定する部分では3つの値を使ってRGBを指定していました。これを4つの値にして、4番目の値に透明度として0-255の値を指定できます。**この値が大きいほど透明度は低くなります。**
さて、以下のようなプログラムを作成してみます。

```python
...(前略)
# 最初に1度だけ実行される部分
pygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((700, 700))
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数
...(中略)
        # フレームを表示するたびに実行される部分
        SURFACE.fill((255, 255, 255))    # 背景を白で描画（クリア）する
        pygame.draw.circle(SURFACE, (255, 0, 0), (350, 300), 100)
        pygame.draw.circle(SURFACE, (0, 0, 0), (350, 300), 100, 2)
        pygame.draw.rect(SURFACE, (100, 255, 0), (180, 150, 300, 300))
        pygame.draw.rect(SURFACE, (0, 0, 0), (180, 150, 300, 300), 2)
        ...(後略)
```

コード上では円と四角形の２つの図形を表示しているのですが、実行してみると分かる通り、四角形しか表示されません。これは、円が描画された上にそれより大きい四角形が描画され、円を隠しているからです。

### 問題

上記のコードを改修して、透明度を指定することにより四角形の下の円が見えるようにしてください。（円の座標を変えるとかはなしです！）

pygameの場合、図形に直接透明度を指定してもうまくいかないので、難易度は高いです。

### 解答

```python
...(前略)
# 最初に1度だけ実行される部分
pygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((700, 700))
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数
...(中略)
        # フレームを表示するたびに実行される部分
        SURFACE.fill((255, 255, 255))    # 背景を白で描画（クリア）する
        pygame.draw.circle(SURFACE, (255, 0, 0), (350, 300), 100)
        pygame.draw.circle(SURFACE, (0, 0, 0), (350, 300), 100, 2)
        # 透過用のフレームを作成
        s = pygame.Surface(SURFACE.get_size(), pygame.SRCALPHA)
        # 透過用のフレーム上に透明度を指定した図形を描画
        pygame.draw.rect(s, (100, 255, 0, 128), (180, 150, 300, 300))
        # 透過用のフレームを通常フレーム上に描画
        SURFACE.blit(s, (0, 0))
        pygame.draw.rect(SURFACE, (0, 0, 0), (180, 150, 300, 300), 2)
        ...(後略)
```

pygameでは個々の図形毎に透明度を指定することはできないので、透過用のフレームを作成し、そのフレーム上に透明度を指定した図形を描画し、そのフレームを従来フレーム上に描画するという処理を行う必要があります。

## 3. 図形を動かす

図形を動かすことを考えてみたいと思います。以下のコードを見て下さい。

```python
...(前略)
# 最初に1度だけ実行される部分
pygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((700, 700))
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数

def main():    # メイン関数
    # 必要ならこの部分にも1度だけ実行される部分を記載する
    SURFACE.fill((255, 255, 255))    # 背景を白で描画（クリア）する
    width, height = SURFACE.get_size()
    x = 0    # 円の現在の位置
    ...(中略)
        # フレームを表示するたびに実行される部分
        pygame.draw.circle(SURFACE, (0, 0, 255), (x, height // 2), 100)
        pygame.draw.circle(SURFACE, (0, 0, 0), (x, height // 2), 100, 2)
        x += 1
        if x > width:
            x = 0

        pygame.display.update()    # ウィンドウを更新
        FPSCLOCK.tick(60)    # １秒に60回フレームを更新する
    ...(後略)
```

drawブロックは繰り返し実行されるのでxの値は徐々に大きくなっていき、円は右に移動します。でも実行してみると分かる通り、思っていたのと違い、変な軌跡が残ってしまいます。これはpygameが図形を上書きしていく仕様のために、前に描画したxを増やす前の図形が残ってしまうためです。これを回避するためには、SURFACE.fill()関数で画面全体を背景色で塗りつぶす方法が有効です。ku

### 問題

```python
SURFACE.fill((255, 255, 255))    # 背景色を指定
```

上記の画面をクリアするSURFACE.fill()関数を正しい位置に配置して、軌跡が残らないようにしてください。

### 解答

```python
...(前略)
# 最初に1度だけ実行される部分
pygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((700, 700))
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数

def main():    # メイン関数
    # 必要ならこの部分にも1度だけ実行される部分を記載する
    SURFACE.fill((255, 255, 255))    # 背景を白で描画（クリア）する
    width, height = SURFACE.get_size()
    x = 0    # 円の現在の位置
    ...(中略)
        # フレームを表示するたびに実行される部分
        SURFACE.fill((255, 255, 255))    # 背景を白で描画（クリア）する
        pygame.draw.circle(SURFACE, (0, 0, 255), (x, height // 2), 100)
        pygame.draw.circle(SURFACE, (0, 0, 0), (x, height // 2), 100, 2)
        x += 1
        if x > width:
            x = 0

        pygame.display.update()    # ウィンドウを更新
        FPSCLOCK.tick(60)    # １秒に60回フレームを更新する
    ...(後略)
```

## 4. 画像を読み込んで動かす

以下のプログラムをエディタに貼り付けて、一度保存して下さい。

```python
import sys        # プログラムを終了する関数sys.exit()を使用する
import pygame    # Pygameを使用する
from pygame.locals import QUIT    # ウィンドウを閉じた時のコード

# 最初に1度だけ実行される部分
pygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((700, 700))
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数

def main():    # メイン関数
    # 必要ならこの部分にも1度だけ実行される部分を記載する
    img = pygame.transform.scale(pygame.image.load("cat.png"), (150, 150))
    while True:    # ずっと
        for event in pygame.event.get():
            if event.type == QUIT:    # ウィンドウを閉じたらプログラムを終了する
                pygame.quit()
                sys.exit()

        # フレームを表示するたびに実行される部分
        SURFACE.fill((200, 200, 200))    # 背景を灰色に描画（クリア）する
        x, y = pygame.mouse.get_pos()
        SURFACE.blit(img, (x, y))

        pygame.display.update()    # ウィンドウを更新
        FPSCLOCK.tick(3)    # １秒に3回フレームを更新する

if __name__ == '__main__':    # メイン関数を呼ぶ
    main()
```

次にネコのイラストを適当なサイトからダウンロードし、コードを保存したフォルダと同じフォルダに「cat.png」として保存して下さい。そうした状態で実行すると、猫がマウスに追従するプログラムが動きます。

なお、マウスの位置は画像の左上になります。

## 5. 赤色の円を円周上に動かす

ちょっとわかりづらいですが、赤色の円を動かして、さらにそれをぐるぐる円を描くように回転させてみます。さて、そのプログラムはこちらです。

```python
import sys        # プログラムを終了する関数sys.exit()を使用する
import pygame    # Pygameを使用する
from pygame.locals import QUIT    # ウィンドウを閉じた時のコード
import math

# 最初に1度だけ実行される部分
pygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((700, 700))
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数

def main():    # メイン関数
    # 必要ならこの部分にも1度だけ実行される部分を記載する
    SURFACE.fill((0, 0, 0))
    width, height = SURFACE.get_size()
    degree = 0
    r = 150
    while True:    # ずっと
        for event in pygame.event.get():
            if event.type == QUIT:    # ウィンドウを閉じたらプログラムを終了する
                pygame.quit()
                sys.exit()

        # フレームを表示するたびに実行される部分
        pygame.draw.rect(SURFACE, (0, 0, 0), (0, 0, width, height))
        degree += 5
        if degree >= 360:
            degree = 0
        rad = math.radians(degree)
        x = width // 2 + r * math.cos(rad)
        y = height // 2 + r * math.sin(rad)
        pygame.draw.circle(SURFACE, (255, 0, 0), (x, y), 50)
        pygame.display.update()    # ウィンドウを更新
        FPSCLOCK.tick(60)    # １秒に60回フレームを更新する

if __name__ == '__main__':    # メイン関数を呼ぶ
    main()
```

### 問題

上のプログラムを改修し、赤い円が楕円を描くように動くようにしてください。楕円の大きさは自由で構いません。

#### ヒント

今は半径rを用意して円の座標x,yを計算していますが、楕円の場合、半径rの代わりに長半径と短半径を指定する新たな変数a,bを用意します。楕円の式は以下の通りです。

```
x = a * cos(rad)
y = b * sin(rad)
```

## 6. ループ

さて、繰り返し処理を利用したプログラムを作ってみます。以下のプログラムはランダムな色の円を横一列に並べるプログラムです。

```python
import sys        # プログラムを終了する関数sys.exit()を使用する
import pygame    # Pygameを使用する
from pygame.locals import QUIT    # ウィンドウを閉じた時のコード
from random import randrange

# 最初に1度だけ実行される部分
pygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((750, 350))
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数

def main():    # メイン関数
    # 必要ならこの部分にも1度だけ実行される部分を記載する
    width, height = SURFACE.get_size()
    N = 10
    SURFACE.fill((0, 0, 0))
    col = pygame.Color(0, 0, 0)
    col.hsva = (randrange(360), 78, 78, 100)
    while True:    # ずっと
        for event in pygame.event.get():
            if event.type == QUIT:    # ウィンドウを閉じたらプログラムを終了する
                pygame.quit()
                sys.exit()

        # フレームを表示するたびに実行される部分
        for i in range(1, N+1):
            spanx = width // N
            d = (width // 2) // N
            pygame.draw.circle(SURFACE, col, (i * spanx - d, height // 2), d)
        pygame.display.update()    # ウィンドウを更新
        FPSCLOCK.tick(3)    # １秒に3回フレームを更新する

if __name__ == '__main__':    # メイン関数を呼ぶ
    main()
```

実行すると円が10個横に並んだ画像が出力されます。for文ではループの回数を重ねる毎に自動的に変数iを増やすことが出来ます。Nは描く円の数を表しています。変えるとどうなるかぜひ試してみてください。

### 問題

先のプログラムを改造して円が縦に並ぶようにして下さい。

#### ヒント

for文の中に、y方向の間隔を保存する変数spanyを作成し、widthからspanxを求めるコードを参考にしてみてください。

### 解答

```python
        ...(前略)
        # フレームを表示するたびに実行される部分
        for i in range(1, N+1):
            spany = height // N
            d = (height // 2) // N
            pygame.draw.circle(SURFACE, col, (width // 2, i * spany - d), d)
        ...(後略)
```

## 7. マウスの検出

マウスがクリックされたときに何かアクションをするといったプログラムを考えます。Pygameではマウスのクリックやマウスの位置を検出する機能があります。以下のプログラムを見て下さい。

```python
import sys        # プログラムを終了する関数sys.exit()を使用する
import pygame    # Pygameを使用する
from pygame.locals import QUIT, MOUSEBUTTONDOWN    # ウィンドウを閉じた時のコード
from random import randrange

# 最初に1度だけ実行される部分
pygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((700, 700))
width, height = SURFACE.get_size()
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数

def fade():
    col = pygame.Color(0, 0, 0)
    col.hsva = (0, 0, 0, 50)
    pygame.draw.rect(SURFACE, col, (0,0,width,height))

class Ripple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.d = 1
        self.c = pygame.Color(0, 0, 0)
        self.c.hsva = (randrange(360), 83, 83, 100)
    def getDiameter(self):
        return self.d
    def setDiameter(self, d):
        self.d = d
    def update(self):
        self.d += 5.0
    def display(self):
        pygame.draw.circle(SURFACE, self.c, (self.x, self.y), self.d, 5)

def main():    # メイン関数
    # 必要ならこの部分にも1度だけ実行される部分を記載する
    SURFACE.fill((0, 0, 0))
    ripList = []
    while True:    # ずっと
        for event in pygame.event.get():
            if event.type == QUIT:    # ウィンドウを閉じたらプログラムを終了する
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                ripList.append(Ripple(width // 2, height // 2))
        # フレームを表示するたびに実行される部分
        fade()
        for rip in ripList:
            rip.update()
            rip.display()
        ripList = [rip for rip in ripList if rip.getDiameter() <= width]
        pygame.display.update()    # ウィンドウを更新
        FPSCLOCK.tick(60)    # １秒に60回フレームを更新する

if __name__ == '__main__':    # メイン関数を呼ぶ
    main()
```

マウスのクリックを検出するとランダムな色の波紋を生成するプログラムです。実行してウィンドウ上で適当に何度かクリックしてみて下さい。

Pygameには**MOUSEBUTTONDOWNイベント**が用意されています。このイベントには名前の通り、マウスがクリックされた時の動作が記述できます。今回の場合、プログラムの詳細は省きますが、簡単には波紋を追加する命令を書いています。そのため、クリックされる度に波紋が増える処理が実現できました。

### 問題

上記のプログラムでは、画面上のどこをクリックしても画面の中心から波紋が生成されていました。これは波紋を生成する座標を（width/2,height/2）としたためです。これを改変して、画面をクリックしたところを中心に波紋を生成するようにしてください。現在のマウスの位置(x, y)は、**pygame.mouse.get_pos**という関数で取得できます。

### 解答

```python
            ...(前略)
            if event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                ripList.append(Ripple(x, y))
            ...(後略)
```

上記部分を変更します

## 8.ランダムの利用

次のプログラムを実行してみてください。

```python
import sys        # プログラムを終了する関数sys.exit()を使用する
import pygame    # Pygameを使用する
from pygame.locals import QUIT    # ウィンドウを閉じた時のコード
import random

# 最初に1度だけ実行される部分
pygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((1280, 720))
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数
width, height = SURFACE.get_size()
cirList = []

def updateCircles():
    global cirList
    vRadius = 5
    maxSize = 100
    for cir in cirList:
        cir.setRadius(cir.getRadius() + vRadius)
    cirList = [cir for cir in cirList if cir.getRadius() <= maxSize]

def drawCircles():
    for cir in cirList:
        cir.draw()

def fade():
    col = pygame.Color(0, 0, 0)
    col.hsva = (0,0,0,15)
    pygame.draw.rect(SURFACE, col, (0,0,width,height))

class Circle:
    def __init__(self, x, y, r, c):
        self.x = x
        self.y = y
        self.r = r
        self.c = pygame.Color(0, 0, 0)
        self.c.hsva = c
    def setRadius(self, r):
        self.r = r
    def getRadius(self):
        return self.r
    def draw(self):
        pygame.draw.circle(SURFACE, self.c, (self.x,self.y), self.r)

def main():    # メイン関数
    # 必要ならこの部分にも1度だけ実行される部分を記載する
    SURFACE.fill((0, 0, 0))
    while True:    # ずっと
        for event in pygame.event.get():
            if event.type == QUIT:    # ウィンドウを閉じたらプログラムを終了する
                pygame.quit()
                sys.exit()

        # フレームを表示するたびに実行される部分
        if random.random() < 0.75:
            cirList.append(Circle(random.randrange(width),random.randrange(height),0,(180,50,100,100)))
        fade()
        updateCircles()
        drawCircles()
        pygame.display.update()    # ウィンドウを更新
        FPSCLOCK.tick(60)    # １秒に60回フレームを更新する

if __name__ == '__main__':    # メイン関数を呼ぶ
    main()
```

random関数を利用することでランダムな位置に円を表示させています。random関数の使い方は以下の通りです。

```python
import random
...
random.random() # 0<=x<1のランダムな小数
random.randrange(50) # 0<=x<50のランダムな整数
random.randint(20, 100)　# 20<=x<100のランダムな整数
```

### 問題

ランダムな位置に表示させることは出来ましたが、色についてもランダムになるようにプログラムを改変してください。

#### ヒント

draw関数内の一部のパラメータをランダムにします。

### 解答

```python
        # フレームを表示するたびに実行される部分
        if random.random() < 0.75:
            cirList.append(Circle(random.randrange(width),random.randrange(height),0,(random.randrange(360),random.randrange(100),random.randrange(100),100)))
```

## 9. 再帰関数

次のプログラムを実行してみてください。

```python
import sys        # プログラムを終了する関数sys.exit()を使用する
import pygame    # Pygameを使用する
from pygame.locals import QUIT    # ウィンドウを閉じた時のコード

# 最初に1度だけ実行される部分
pygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((700, 700))
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数

def circlesR(x, y, r, n):
    pygame.draw.circle(SURFACE, (255, 255, 255), (x,y), r, 1)
    if n <= 1:
        return
    newR = r/2
    circlesR(x+newR,y,newR,n-1)
    circlesR(x-newR,y,newR,n-1)

def main():    # メイン関数
     # 必要ならこの部分にも1度だけ実行される部分を記載する
    width, height = SURFACE.get_size()
    circlesR(width//2,height//2,350,4)
    while True:    # ずっと
        for event in pygame.event.get():
            if event.type == QUIT:    # ウィンドウを閉じたらプログラムを終了する
                pygame.quit()
                sys.exit()

        # フレームを表示するたびに実行される部分

        pygame.display.update()    # ウィンドウを更新
        FPSCLOCK.tick(3)    # １秒に3回フレームを更新する

if __name__ == '__main__':    # メイン関数を呼ぶ
    main()
```

circleR関数に着目すると、関数内でcircleR自身をまた呼び出していることが分かります。このような関数を一般に**再帰関数**と呼びます。再帰関数は「深さ優先探索」と呼ばれるアルゴリズムを実装したり、数学の漸化式を解いたり出来ます。circlesRの動きを追っていくと、円を描いてその円の内側にさらに２つの円を描いて...を繰り返していることが分かると思います。main関数内で呼び出しているcirclesR関数の第4引数（今は4になっている）を書き換えるとどんな風になるかも試してみてください。

### 問題

上記のプログラムでは円の内側に左右２つの円を配置していました。これを改造して円の上下左右に配置するようにして、n=6で実行してみてください。

### 解答

```python
...(前略)
def circlesR(x, y, r, n):
    pygame.draw.circle(SURFACE, (255, 255, 255), (x,y), r, 1)
    if n <= 1:
        return
    newR = r/2
    circlesR(x+newR,y,newR,n-1)
    circlesR(x-newR,y,newR,n-1)
    circlesR(x,y+newR,newR,n-1)
    circlesR(x,y-newR,newR,n-1)

def main():    # メイン関数
     # 必要ならこの部分にも1度だけ実行される部分を記載する
    width, height = SURFACE.get_size()
    circlesR(width//2,height//2,350,6)
    ...(後略)
```

## 10. フラクタル

再帰関数を応用してフラクタルを作ってみます。次のプログラムを実行してみてください。

```python
import sys        # プログラムを終了する関数sys.exit()を使用する
import pygame    # Pygameを使用する
from pygame.locals import QUIT    # ウィンドウを閉じた時のコード
import numpy as np
import math

# 最初に1度だけ実行される部分
pygame.init()    # Pygameを初期化する（最初に必ず実行する）
SURFACE = pygame.display.set_mode((700, 700))
FPSCLOCK = pygame.time.Clock()    # コマ数の設定用変数

class PVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.v = np.array([x, y])
    @classmethod
    def sub(cls, v0, v1):
        v = v0.v - v1.v
        return PVector(v[0], v[1])
    @classmethod
    def cross2d(cls, x, y):
        return x[..., 0] * y[..., 1] - x[..., 1] * y[..., 0]
    def heading(self):
        v0 = np.array([100, 0])
        uv0 = v0 / np.linalg.norm(v0)
        uv1 = self.v / np.linalg.norm(self.v)
        cos = np.dot(uv0, uv1)
        rad = np.arccos(cos)
        if PVector.cross2d(v0, self.v) > 0:
            rad *= -1
        return rad
    def mag(self):
        return np.linalg.norm(self.v)
        
class Graphics:
    def __init__(self, g=None):
        if g is None:
            self.ctm = np.array([1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]).reshape(3, 3)
        else:
            self.ctm = g.ctm
    def scale(self, sx, sy):
        matrix = np.array([sx, 0.0, 0.0, 0.0, sy, 0.0, 0.0, 0.0, 1.0]).reshape(3, 3)
        self.ctm = np.matmul(matrix, self.ctm)
    def translate(self, tx, ty):
        matrix = np.array([1.0, 0.0, 0.0, 0.0, 1.0, 0.0, tx, ty, 1.0]).reshape(3, 3)
        self.ctm = np.matmul(matrix, self.ctm)
    def rotateAngle(self, angle):
        radian = math.radians(angle)
        self.rotate(radian)
    def rotate(self, radian):
        matrix = np.array([math.cos(radian), -math.sin(radian), 0.0, math.sin(radian), math.cos(radian), 0.0, 0.0, 0.0, 1.0]).reshape(3, 3)
        self.ctm = np.matmul(matrix, self.ctm) 
    def conv(self, x, y):
        nx = int(x * self.ctm[0][0] + y * self.ctm[1][0] + self.ctm[2][0])
        ny = int(x * self.ctm[0][1] + y * self.ctm[1][1] + self.ctm[2][1])
        return (nx, ny)
     
class FractalGenerator:
    def __init__(self):
        self.vecs = []
        self.p0 = None
        self.pp = None
        self.v0 = None
        self.g = Graphics()
        self.save = []
    def add(self, p):
        if self.p0 is None:
            self.p0 = p
            self.pp = p
            return
        self.vecs.append(PVector.sub(p,self.pp))
        self.v0 = PVector.sub(p, self.p0)
        self.pp = p
    def show(self, n):
        self.save.append(Graphics(self.g))
        self.g.translate(self.p0.x, self.p0.y)
        self.g.rotate(self.v0.heading())
        self.rec(1, n)
        self.g = self.save.pop()
    def rec(self, rate, n):
        self.save.append(Graphics(self.g))
        pRad = self.v0.heading()
        for v in self.vecs:
            rad = v.heading()
            l = v.mag()
            self.g.rotate(rad - pRad)
            if n == 1:
                pygame.draw.line(SURFACE, (255, 255, 255), self.g.conv(0, 0), self.g.conv(rate*l, 0))
            else:
                self.rec(rate*l/self.v0.mag(),n-1)
            self.g.translate(rate*l,0)
            pRad = rad
        self.g = self.save.pop()

def main():    # メイン関数
     # 必要ならこの部分にも1度だけ実行される部分を記載する
    gen = FractalGenerator()
    gen.add(PVector(50,450))
    gen.add(PVector(200,450))
    gen.add(PVector(220,150))
    gen.add(PVector(240,450))
    gen.add(PVector(650,450))
    gen.show(1)
    while True:    # ずっと
        for event in pygame.event.get():
            if event.type == QUIT:    # ウィンドウを閉じたらプログラムを終了する
                pygame.quit()
                sys.exit()

          # フレームを表示するたびに実行される部分

        pygame.display.update()    # ウィンドウを更新
        FPSCLOCK.tick(3)    # １秒に3回フレームを更新する

if __name__ == '__main__':    # メイン関数を呼ぶ
    main()
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

main関数内で指定している座標値を変更し、nの値を5にすればコッホの曲線を描画することができます。
