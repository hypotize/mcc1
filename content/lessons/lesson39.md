+++
title = "レッスン 39"
date = "2024-09-01T11:00:00+09:00"
author = "橋本　吉生"
description = "せつめいどうがをつくろう"
showFullContent = false
readingTime = false
tags = ["Python", "動画"]
+++
# おもしろい話をだれかに教えてあげるせつめいどうがを作ろう
ターミナルでコマンドを実行する。
```
cd mcc1
git pull
python3 -m pip install Pillow gTTS moviepy
```

ファイルマネージャを開く。
次のフォルダを開く。「mcc1」→「code」→「lesson39」
「せつめい.txt」を開く。
その中に、自分の好きなことを書く。
１行の長さはあまり長くないほうがいいです。
あまり長いと画面からはみだしてしまいます。
何も書いていない行を入れると、ページを区切ってくれます。

書くことはAIを使って作ってもいいと思います。
https://gemini.google.com/app?hl=ja
AIにいろいろ質問してみましょう。

文章ができたら、動画を作る。
ターミナルでコマンドを実行する。
動画ができるまでには１分くらいかかります。

```
cd code/lesson39
python3 all.py
```

動画を作ったら、ファイル名を変えておきましょう。
そのままだと、次の動画を作ると消えてしまいます。

画像と音声を別の方法で作ってもいいです。
そのときは、「create_video.py」を実行してください。
