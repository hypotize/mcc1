+++
title = "作品 02"
date = "2022-04-11T07:30:00+09:00"
author = "Michael Cashen"
       description = ""

showFullContent = true
readingTime = false
+++

# ロゴと曲
オンライン画像作成ツールの[Canva](https://www.canva.com/)で作ったクラブのロゴと[Hydrogen](http://hydrogen-music.org/)で作ったドラムの曲を組み合わせて、（動かない）動画を作りました。


画像(jpg)と曲(wav)から動画を作るのに、とてもパワフルな[ffmpeg](https://ffmpeg.org/)というツールを使いました。そして、動画の公開は世界最大の動画共有プラットフォームのYouTubeで公開しました。

{{< youtube LjD87e40yjo >}}

ffmpegのコマンドはこれでした(備忘録)：
{{< code language="shell" id="1" isCollapsed="false">}}
ffmpeg -r 1 -loop 1 -i pic.jpg -i song.wav -acodec copy -r 1 -shortest -vf scale=1280:720 video.flv
{{< /code >}}

