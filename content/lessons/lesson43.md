+++
title = "レッスン 43"
date = "2024-10-08T12:00:00+09:00"
author = "小野寺 健"
description = "スクラッチでしんけいすいじゃくゲームをつくろう"
showFullContent = false
readingTime = false
tags = ["Scratch", "スクラッチ", "ゲーム"]
+++
# スクラッチで「しんけいすいじゃく」ゲームをつくろう
スクラッチで「しんけいすいじゃく」ゲームをつくりましょう。

## 「しんけいすいじゃく」ゲームとは
トランプなどで、カードをうらがえしにしてならべ、おなじすうじのカードをめくったら
カードをとりのぞきます。

ふつうはなんにんかであそび、おなじすうじのカードをとりのぞいているあいだは、
つづけてかーどをめくることができ、ちがうすうじがでたらつぎのひとにこうたいします。

たくさん、カードをとれたひとがかちです。

## こんかいつくるゲーム
こんかいは、トランプではなく、おなじえが２くみずつあるカードを１０くみつくり、
すくないしっぱいかいすうですべてのカードをとりのぞけるかをきそうゲームにします。

ステップ１からステップ３までじゅんばんにつくっていきます。

### １しゅるいめのカードをつくる（ステップ１）
まず、１しゅるいめのカードをつくります。

このぶぶんはちょっとむずかしいので、したのプロジェクトを「リミックス」してコピーをつくりましょう。

https://scratch.mit.edu/projects/1082618177

みどりのはたをおすと、ハートが２つひょうじされ、ハートをクリックすると「ねこ」にかわり、もう１まいのハートをクリックすると２つとも「ねこ」にかわり、しばらくするときえます。

うらのえ（ハート）とおもてのえをすきなえにかえてみましょう。

「コスチューム」のタブをせんたくして、したの「コスチュームをえらぶ」からじぶんのすきな「うらのカードのえ」と「おもてのカードのえ」をえらびます。

「おもてのカードのえ」はカードのしゅるいをふやすたびにかえるので、「どうぶつ」とか「のりもの」とかテーマをきめたほうがよいかもしれません。

「うらのカードのえ」と「おもてのカードのえ」をついかしたら、「ハート」と「ねこ」はいらないのでさくじょします。

さくじょしたあと、「うらのえ」が１ばんめ、「おもてのえ」が２ばんめになっていなければ、いれかえをしてください。

さいごに、「コード」のタブをせんたくして、「並び替えを受け取ったとき」のブロックにある「コスチュームを「heart red」にする」のぶぶんをこんかいえらんだ「うらのカードのえ」のなまえにかえてください。

### カードのしゅるいをふやす（ステップ２）
いまはおなじしゅるいのカード１くみしかないので、もう１くみべつのしゅるいのかーどをついかします。

みぎしたのスプライトをみぎクリックして「複製」をえらんで、スプライトをまるごとコピーします。

コピーしたスプライト（なまえが「Heart2」などにかわっている）の「コスチューム」タブをえらび、ひだりがわのコスチュームの２ばんめ（「おもてのえ」、たとえばねこ）をえらび、ごみばこをクリックしてさくじょします。

ひだりしたの「コスチュームをえらぶ」からあたらしい「おもてのカードのえ」（たとえばいぬ）をえらびます。

「コード」のタブをえらび、「並び替えを受け取ったとき」のブロックのせんとうのほうにある「IDを1にする」を
「IDを2にする」にかえます。
 
https://scratch.mit.edu/projects/1082625717

みどりのはたをおすと、ハートが４つひょうじされ、ねことねこまたはいぬといぬなら、カードがきえて残りの枚数が2まいずつへり、ねこといぬならハートにもどって失敗回数が1つずつふえます。

### カードのしゅるいを１０しゅるいにする（ステップ３）

ステップ２とおなじことを１０しゅるいになるまでくりかえします。

IDのすうじをかきかえるぶぶんはしゅるいごとにつぎのようにかえていきます。３しゅるいめいこうがこれからつくるカードのすうじです。

- １しゅるいめのカード（さくせいずみ）

	「IDを1にする」
　
- ２しゅるいめのカード（さくせいずみ）

	「IDを2にする」

- ３しゅるいめのカード

	「IDを3にする」
　
- ４しゅるいめのカード

	「IDを4にする」
	
- ５しゅるいめのカード

	「IDを5にする」
　
- ６しゅるいめのカード

	「IDを6にする」

- ７しゅるいめのカード

	「IDを7にする」
　
- ８しゅるいめのカード

	「IDを8にする」
	
- ９しゅるいめのカード

	「IDを9にする」
　
- １０しゅるいめのカード

	「IDを10にする」
	
おもてのえはしゅるいごとぜんぶかえてください。

かんせいしたものはつぎのとおりです。

https://scratch.mit.edu/projects/1082626493

みどりのはたをおすと、ハートが20こひょうじされ、
おなじしゅるいのカードをひらくとカードがきえて「残り枚数」がへり、
ちがうしゅるいのカードをひらくとハートにもどって「失敗回数」がふえます。

なお、すべてのカードをクリアするとはいけいがハートマークの「おめでとう」にかわります。

ステージのはいけいの２ばんめをかえてじぶんのすきなクリアのえにしましょう。
