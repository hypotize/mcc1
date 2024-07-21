+++
title = "レッスン 36"
date = "2024-06-26T10:00:00+09:00"
author = "小野寺 健"
description = "スプレッドシートでボウリングのスコアシートを作ろう"
showFullContent = false
readingTime = false
tags = ["スプレッドシート", "自動計算", "ボウリング", "初級"]
+++
# スプレッドシートでボウリングのスコアシートを作ろう
## スコアシートの例
ボウリングでは次のようなスコアシートが付けられます。

#### 例１
<table>
<tr>
    <th colspan="2" align="center">1</th>
    <th colspan="2" align="center">2</th>
    <th colspan="2" align="center">3</th>
    <th colspan="2" align="center">4</th>
    <th colspan="2" align="center">5</th>
    <th colspan="2" align="center">6</th>
    <th colspan="2" align="center">7</th>
    <th colspan="2" align="center">8</th>
    <th colspan="2" align="center">9</th>
    <th colspan="3" align="center">10</th>
</td>
<tr>
    <td>6</td><td>／</td>
    <td>8</td><td>－</td>
    <td>Ｘ</td><td>&nbsp;</td>
    <td>2</td><td>7</td>
    <td>5</td><td>／</td>
    <td>3</td><td>4</td>
    <td>Ｘ</td><td>&nbsp;</td>
    <td>9</td><td>／</td>
    <td>1</td><td>2</td>
    <td>7</td><td>1</td><td>&nbsp;</td>
</tr>
<tr>
    <td colspan="2" align="center">18</td>
    <td colspan="2" align="center">26</td>
    <td colspan="2" align="center">46</td>
    <td colspan="2" align="center">54</td>
    <td colspan="2" align="center">67</td>
    <td colspan="2" align="center">74</td>
    <td colspan="2" align="center">94</td>
    <td colspan="2" align="center">105</td>
    <td colspan="2" align="center">108</td>
    <td colspan="3" align="center">116</td>
</tr>
</table>

#### 例２
<table>
<tr>
    <th colspan="2" align="center">1</th>
    <th colspan="2" align="center">2</th>
    <th colspan="2" align="center">3</th>
    <th colspan="2" align="center">4</th>
    <th colspan="2" align="center">5</th>
    <th colspan="2" align="center">6</th>
    <th colspan="2" align="center">7</th>
    <th colspan="2" align="center">8</th>
    <th colspan="2" align="center">9</th>
    <th colspan="3" align="center">10</th>
</td>
<tr>
    <td>1</td><td>8</td>
    <td>9</td><td>／</td>
    <td>7</td><td>2</td>
    <td>Ｘ</td><td>&nbsp;</td>
    <td>Ｇ</td><td>－</td>
    <td>9</td><td>／</td>
    <td>3</td><td>6</td>
    <td>8</td><td>－</td>
    <td>5</td><td>4</td>
    <td>Ｘ</td><td>8</td><td>1</td>
</tr>
<tr>
    <td colspan="2" align="center">9</td>
    <td colspan="2" align="center">26</td>
    <td colspan="2" align="center">35</td>
    <td colspan="2" align="center">45</td>
    <td colspan="2" align="center">45</td>
    <td colspan="2" align="center">58</td>
    <td colspan="2" align="center">67</td>
    <td colspan="2" align="center">75</td>
    <td colspan="2" align="center">84</td>
    <td colspan="3" align="center">103</td>
</tr>
</table>

### スコアシートの意味
１行目はフレーム番号

２行目は各フレームの１投目と２投目（１０フレームはさらに３投目）、数字は倒した本数、「Ｘ」は「ストライク」、「／」は「スペア」、「Ｇ」は「ガター」、「－」は「ミス（ピンに当たらなかった）」

３行目はそのフレームまでのスコア

## スコアの計算方法
ストライクの場合、次の２投分の点数を、スペアの場合は次の１投分の点数を加算。
また、ガター、ミスは0点です。

なお、10フレーム目はストライクやスペアがあれば3回投げられますが、それ以外は2回だけ投げられます。
10フレーム目では倒れたピンの数だけカウントされるため、ストライクが3つの場合は30点です。

### 最高点
つまり、すべてストライクの場合は次のようになり、最高点は300点です。

#### 例３
<table>
<tr>
    <th colspan="2" align="center">1</th>
    <th colspan="2" align="center">2</th>
    <th colspan="2" align="center">3</th>
    <th colspan="2" align="center">4</th>
    <th colspan="2" align="center">5</th>
    <th colspan="2" align="center">6</th>
    <th colspan="2" align="center">7</th>
    <th colspan="2" align="center">8</th>
    <th colspan="2" align="center">9</th>
    <th colspan="3" align="center">10</th>
</td>
<tr>
    <td>Ｘ</td><td>&nbsp;</td>
    <td>Ｘ</td><td>&nbsp;</td>
    <td>Ｘ</td><td>&nbsp;</td>
    <td>Ｘ</td><td>&nbsp;</td>
    <td>Ｘ</td><td>&nbsp;</td>
    <td>Ｘ</td><td>&nbsp;</td>
    <td>Ｘ</td><td>&nbsp;</td>
    <td>Ｘ</td><td>&nbsp;</td>
    <td>Ｘ</td><td>&nbsp;</td>
    <td>Ｘ</td><td>Ｘ</td><td>Ｘ</td>
</tr>
<tr>
    <td colspan="2" align="center">30</td>
    <td colspan="2" align="center">60</td>
    <td colspan="2" align="center">90</td>
    <td colspan="2" align="center">120</td>
    <td colspan="2" align="center">150</td>
    <td colspan="2" align="center">180</td>
    <td colspan="2" align="center">210</td>
    <td colspan="2" align="center">240</td>
    <td colspan="2" align="center">270</td>
    <td colspan="3" align="center">300</td>
</tr>
</table>

## 入力データ
上記の例の場合、次のような入力形式で各フレームでの点数が与えられるものとします
<table>
<tr>
    <th>&nbsp;</th>
    <th colspan="2" align="center">1</th>
    <th colspan="2" align="center">2</th>
    <th colspan="2" align="center">3</th>
    <th colspan="2" align="center">4</th>
    <th colspan="2" align="center">5</th>
    <th colspan="2" align="center">6</th>
    <th colspan="2" align="center">7</th>
    <th colspan="2" align="center">8</th>
    <th colspan="2" align="center">9</th>
    <th colspan="3" align="center">10</th>
</td>
<tr>
    <td>例１</td>
    <td>6</td><td>4</td>
    <td>8</td><td>0</td>
    <td>10</td><td>&nbsp;</td>
    <td>2</td><td>7</td>
    <td>5</td><td>5</td>
    <td>3</td><td>4</td>
    <td>10</td><td>&nbsp;</td>
    <td>9</td><td>1</td>
    <td>1</td><td>2</td>
    <td>7</td><td>1</td><td>&nbsp;</td>
</tr>
<tr>
    <td>例２</td>
    <td>1</td><td>8</td>
    <td>9</td><td>1</td>
    <td>7</td><td>2</td>
    <td>10</td><td>&nbsp;</td>
    <td>0</td><td>0</td>
    <td>9</td><td>1</td>
    <td>3</td><td>6</td>
    <td>8</td><td>0</td>
    <td>5</td><td>4</td>
    <td>10</td><td>8</td><td>1</td>
</tr>
<tr>
    <td>例３</td>
    <td>10</td><td>&nbsp;</td>
    <td>10</td><td>&nbsp;</td>
    <td>10</td><td>&nbsp;</td>
    <td>10</td><td>&nbsp;</td>
    <td>10</td><td>&nbsp;</td>
    <td>10</td><td>&nbsp;</td>
    <td>10</td><td>&nbsp;</td>
    <td>10</td><td>&nbsp;</td>
    <td>10</td><td>&nbsp;</td>
    <td>10</td><td>10</td><td>10</td>
</tr>
</table>

## 問題
スプレッドシートの5行目に下記の入力データを入力し、1行目から3行目までに入力データから自動的にスコアシートが表示されるようにしてください。

<table>
<tr>
    <th colspan="2" align="center">1</th>
    <th colspan="2" align="center">2</th>
    <th colspan="2" align="center">3</th>
    <th colspan="2" align="center">4</th>
    <th colspan="2" align="center">5</th>
    <th colspan="2" align="center">6</th>
    <th colspan="2" align="center">7</th>
    <th colspan="2" align="center">8</th>
    <th colspan="2" align="center">9</th>
    <th colspan="3" align="center">10</th>
</td>
<tr>
    <td>9</td><td>1</td>
    <td>8</td><td>2</td>
    <td>10</td><td>&nbsp;</td>
    <td>5</td><td>0</td>
    <td>3</td><td>6</td>
    <td>4</td><td>2</td>
    <td>7</td><td>3</td>
    <td>6</td><td>3</td>
    <td>10</td><td>&nbsp;</td>
    <td>9</td><td>1</td><td>9</td>
</tr>
</table>

### フレーム番号の作成
1行目にフレーム番号を入力します。
A列からR列まで2列単位で結合し1～9までフレーム番号を入力します。
10フレームはS列からU列まで3列を結合し、フレーム番号10を入力します。

### 各フレームで倒したピン表示の作成
2行目に各フレームで倒したピンの情報を表示します。
各セルに対し、フレームごとに1投目、2投目（10フレーム目はさらに3投目）を以下のように表示します。
#### 1フレームから9フレームまで
1投目は、以下のように表示します。
* 0（ガター）の場合

    数字の代わりに全角の"Ｇ"を表示します
* 10（ストライク）の場合

    数字の代わりに全角の"Ｘ"を表示します
* それ以外の場合

    入力データの数字をそのまま表示します

2投目は、以下のように表示します。
* 1投目がストライクの場合

    入力データが空欄になっているので、空欄をそのまま表示します
* 1投目と2投目の合計が10の場合

    スペアなので、数字の代わりに全角の"／"を表示します
* 2投目は0（ミス）の場合
    
    数字の代わりに全角の"－"を表示します
* それ以外の場合

    入力データの数字をそのまま表示します

#### 10フレーム
1投目については1～9フレームの1投目と同じ表示を行います。

2投目は、以下のように表示します。
* 1投目がストライクの場合

    1～9フレームの1投目と同じ表示を行います
* それ以外の場合

    1～9フレームの2投目のストライク以外の場合と同じ表示を行います

3投目は、以下のように表示します。
* 2投目がストライクかスペアの場合

    1～9フレームの1投目と同じ表示を行います。
* 1投目がストライクで、2投目がストライク以外の場合

    1～9フレームの2投目のストライク以外の場合の1投目と2投目を2投目と3投目に置き換えて、同様の処理を行います
* それ以外の場合（1投目がストライクでなく、2投目がスペアでもない場合）

    空欄を表示します

### スコアの表示
3行目をフレーム番号と同じように結合し、フレームごとに以下のようにスコアを表示します。
#### 1～8フレーム
1投目と2投目の値によって前のフレームのスコア（ただし、1フレーム目は前のフレームの値は加算されません）に対し、以下のようにスコアが加算されます。
* 1投目が10（ストライク）の場合

    * 次のフレームの1投目が10（ストライク）の場合
    
       1投目の値(10)＋ 次のフレームの1投目の値(10)＋次の次のフレームの1投目の値
    * 次のフレームの1投目が10（ストライク）以外の場合

        1投目の値(10)＋ 次のフレームの1投目の値＋次のフレームの2投目の値
* 1投目と2投目の値の合計が10（スペア）の場合

    1投目の値＋2投目の値（合わせて10）＋次のフレームの1投目の値

* それ以外の場合

    1投目の値＋2投目の値

#### 9フレーム
1投目と2投目の値によって前のフレームのスコア（8フレームのスコア）に対し、以下のようにスコアが加算されます。
* 1投目が10（ストライク）の場合

    1投目の値(10)＋10フレームの1投目の値＋10フレームの2投目の値

* 1投目と2投目の値の合計が10（スペア）の場合

    1投目の値＋2投目の値（合わせて10）＋10フレームの1投目の値

* それ以外の場合

    1投目の値＋2投目の値

#### 10フレーム
前のフレームのスコア（9フレームのスコア）に対し、全ての投げた値（2投または3投）の合計値を加算します。

### 罫線の作成
1行目から3行目まで、1フレームから10フレームまで全てに罫線を設定します。

## 結果の確認
1行目から3行目までが以下のように表示されていれば正解です。

<table>
<tr>
    <th colspan="2" align="center">1</th>
    <th colspan="2" align="center">2</th>
    <th colspan="2" align="center">3</th>
    <th colspan="2" align="center">4</th>
    <th colspan="2" align="center">5</th>
    <th colspan="2" align="center">6</th>
    <th colspan="2" align="center">7</th>
    <th colspan="2" align="center">8</th>
    <th colspan="2" align="center">9</th>
    <th colspan="3" align="center">10</th>
</td>
<tr>
    <td>9</td><td>／</td>
    <td>8</td><td>／</td>
    <td>Ｘ</td><td>&nbsp;</td>
    <td>5</td><td>－</td>
    <td>3</td><td>6</td>
    <td>4</td><td>2</td>
    <td>7</td><td>／</td>
    <td>6</td><td>3</td>
    <td>Ｘ</td><td>&nbsp;</td>
    <td>9</td><td>／</td><td>9</td>
</tr>
<tr>
    <td colspan="2" align="center">18</td>
    <td colspan="2" align="center">38</td>
    <td colspan="2" align="center">53</td>
    <td colspan="2" align="center">58</td>
    <td colspan="2" align="center">67</td>
    <td colspan="2" align="center">73</td>
    <td colspan="2" align="center">89</td>
    <td colspan="2" align="center">98</td>
    <td colspan="2" align="center">118</td>
    <td colspan="3" align="center">137</td>
</tr>
</table>

## ヒント
計算式は以下のように使用します。
#### IF式
`IF(条件, YESの時, NOの時)` YESの時、NOの時の部分にもIF式を設定することができます。
#### AND式
`AND(条件1, 条件2)` IFの条件が複数条件で「かつ」の場合、ANDで結合できます。また、条件1や条件2の部分にもAND式やOR式を設定することができます。
#### OR式
`OR(条件1, 条件2)` IFの条件が複数条件で「または」の場合、ORで結合できます。また、条件1や条件2の部分にもAND式やOR式を設定することができます。
#### 等しい・等しくない
条件では、`=`で等しい、`<>`で等しくないを表します。

## 解答
<details>
<summary>解答</summary>

#### 1フレームから10フレームまでの1投目

```
IF(A5=0, "Ｇ", IF(A5=10, "Ｘ", A5))
```
Aの部分はフレームによって、C, E, G ... Sまで変更される（コピペ）

#### 1フレームから9フレームまでの2投目

```
IF(A5=10, "", IF(A5+B5=10, "／", IF(B5=0, "－", B5)))
```
(A,B)の部分はフレームによって、(C,D), (E,F), (G,H)... (Q,R)まで変更される（コピペ）

#### 10フレームの2投目

```
IF(S5=10, IF(T5=0, "Ｇ", IF(T5=10, "Ｘ", T5)), IF(S5+T5=10, "／", IF(S5=0, "－", S5)))
```

#### 10フレームの3投目

```
IF(OR(T5=10, AND(S5<>10, S5+T5=10)), IF(U5=0, "Ｇ", IF(U5=10, "Ｘ", U5)), IF(AND(S5=10, T5<>10), IF(T5+U5=10, "／", IF(U5=0, "－", U5)), ""))
```

#### 1フレームのスコア

```
IF(A5=10, IF(C5=10, 20+E5, 10+C5+D5), IF(A5+B5=10, 10+C5, A5+B5))
```

#### 2フレームから8フレームのスコア

```
A3+IF(C5=10, IF(E5=10, 20+G5, 10+E5+F5), IF(C5+D5=10, 10+E5, C5+D5))
```
(A,C,D,E,F,G)の部分はフレームによって(C,E,F,G,H,I)...(M,O,P,Q,R,S)まで変更される（コピペ）

#### 9フレームのスコア

```
O3+IF(Q5=10, 10+S5+T5, IF(Q5+R5=10, 10+S5, Q5+R5))
```

#### 10フレームのスコア

```
Q3+IF(U5="", S5+T5, S5+T5+U5)
```

</details>