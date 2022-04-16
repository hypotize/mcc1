+++
title = "レッスン 03"
date = "2022-04-16T08:30:00+09:00"
author = "Michael Cashen"
description = ""

showFullContent = true
readingTime = false
+++

# レッスンの目標
自己紹介を書いて、世の中に公開してみよう。

# 勉強すること
[GitHub](https://github.com/)というオンラインのソースコード管理ツールのアカウントを作って、自分の自己紹介の文書をそこにコミットします(アップロードします)。ソースコード管理は開発者としてとても大事な作業です。最初は難しいけど、ちょっとずつ慣れましょう。

# 手順①  GitHubアカウント取得
1. まずは、ユーザ名を考えましょう。例えば、あなとの名前がyumiなら、ユーザ名を`mcc-yumi`にしましょう。最初のmccはMiura Computer Clubの頭文字ね！他のみんなとかぶらないようにしましょう。

2. `ユーザ名@miura.io`のメールアドレス用いて、[https://github.com/signup](https://github.com/signup) でアカウントを作ってみましょう。例えば、mcc-yumi@miura.io。写真のように入力します。
![signup](/images/lesson3_githubsignup.png)|

3. 確認のメールはマイケルに届く設定になっているので、この下に画面まで行けたら、マイケルに聞いてください。![signup](/images/lesson3_launchcode.png)

4. サインアップが終わったら、マイケルにアカウント名を言ってください。パスワードは自分でメモってね！マイケルがあなたのアカウントに三浦コンピュータクラブのそーそコードの管理に使っているレポジトリーに書き込みの権限を設定します。

# 手順②  mcc1のレポジトリーを自分のパソコンに同期する

1. mcc1(三浦コンピュータクラブの一番のレポジトリ)は公開しているので、クローン(コピー)するためには実はアカウントは入りません。下記のコマンド一つでできます。アカウントは後ほど、コミット(登録)するときに使います。コマンドを打つためには、ターミナルを開きます。ターミナルはパソコンに対してコマンドを打ち込むための入り口です。

{{< code language="shell" id="1" isCollapsed="false">}}
git clone https://github.com/hypotize/mcc1
{{< /code >}}

2. 三浦コンピュータクラブのウェブサイトは[hugo](https://gohugo.io/)というウェブサイトをつくるためのフレームワーク(枠組み)を使っていて、レイアウトは今はterminalというテーマを使っています。そのテーマは別の場所にGitHubで公開していて、インストールする必要があります。そのターミナルも下記のコマンドで入れます。

{{< code language="shell" id="2" isCollapsed="false">}}
git clone https://github.com/panr/hugo-theme-terminal.git themes/terminal
{{< /code >}}
 
3. これでウェブサイトのコピーが自分のパソコンでできました。そのディレクトリに入りましょう。

{{< code language="shell" id="3" isCollapsed="false">}}
cd mcc1
{{< /code >}}
 
4. クラブのパソコンなら、hugoがインストールされてるので、下記のコマンドでウェブサイトを実行できます。新しいターミナルを開いて、やってみましょう。

{{< code language="shell" id="4" isCollapsed="false">}}
cd mcc1
hugo server -t terminal
{{< /code >}}

インタネットで公開しているサイトは [https://miura.io/](https://miura.io/)でアクセスしますが、自分のパソコンでで動いているウェブサイトはこのアドレスでアクセスします: [http://localhost:1313/](http://localhost:1313/)。

# 手順③  自己紹介を書いてみましょう

三浦コンピュータクラブのウェブサイトの内容はいくつかのフォルダーに分けています。メンバーの自己紹介は`content/members`のディレクトリにあります。そこに移動しましょうか。

{{< code language="shell" id="5" isCollapsed="false">}}
cd content/members
{{< /code >}}

自分の今どのディレクトリにいるのがわからないなら、下記のコマンドで教えてもらいましょう。

{{< code language="shell" id="6" isCollapsed="false">}}
pwd
{{< /code >}}

また、`..`は一個上のディレクトリを指します。今は`mcc1/content/members`にいたいので、打たないでね。

{{< code language="shell" id="7" isCollapsed="false">}}
cd .. 
{{< /code >}}

自己紹介はみんな似た形にしたいので、テンプレートを用意しました。テンプレートをコピーして、自分で書き込みましょう。HugoのウェブサイトはHTMLという言語で公開されますが、記述するのは[マークダウン](https://ja.wikipedia.org/wiki/Markdownン)です。コピーのコマンドはこれですが、`mcc-yumi.md`ではなく、自分のユーザ名.mdにしてくださいね。mdはマークダウンを指すファイル拡張子です。

{{< code language="shell" id="8" isCollapsed="false">}}
cp template.md mcc-yumi.md
{{< /code >}}

ここまで長い道のりでしたが、やっと自分のプロファイルを編集できるところまできました。マークダウンはただのテキストですので、テキストエディターを使って編集します。ターミナルではなく、GUI(ウィンドウ)でそのファイルが入っているフォルダーを開きたいので、自分の使っているパソコンにあったコマンドを実行してみてください。

{{< code language="WINDOWS SHELL" id="9" isCollapsed="false">}}
start . 
{{< /code >}}

{{< code language="MAC OS-X SHELL" id="10" isCollapsed="false">}}
open  . 
{{< /code >}}

{{< code language="LINUX SHELL" id="11" isCollapsed="false">}}
xdg-open . 
{{< /code >}}

GUI上でディレクトリが開いたら、そこに入っている自分の名前の`.md`ファイルを右クリックして、テキスト編集ツールで編集してみましょう。編集が終わったら、保存しましょう。まだhugoが動いている場合、ファイルを保存した瞬間で、[http://localhost:1313/](http://localhost:1313/)で見えるウェブサイトは更新されます。自分の自己紹介が足されたかを見てみましょう。

# 手順④  書いた自己紹介をcommitしましょう。

ここからはちょっと難しいので、分からないところは聞きながらやりましょう。

まずは、ファイルがわかったかを確認します。

{{< code language="SHELL" id="12" isCollapsed="false">}}
git status
{{< /code >}}

このコマンドの結果がこのような感じで表示されるはずです。出力結果には自分が編集したファイルがあれば、OKです。
{{< code language="SHELL" id="13" isCollapsed="false">}}
mcashen@silver mcc1 % git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	content/members/mcc-yumi.md

no changes added to commit (use "git add" and/or "git commit -a")
mcashen@silver mcc1 % 
{{< /code >}}

つぎにその編集したファイルをソースコードのトラッキング対象に追加します。

{{< code language="SHELL" isCollapsed="false">}}
git add mcc-yumi.md
{{< /code >}}

コマンドが成功したら、何も出力がありません。でも`git status`とうつと、そのコマンドの出力が変わって、自分のファイルがソースコードのトラッキング対象になったことがわかります。

{{< code language="SHELL" isCollapsed="false">}}
mcashen@silver members % git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   mcc-yumi.md
mcashen@silver members %
{{< /code >}}

次にソースコードに足されたファイルをコミット(登録)します。

{{< code language="SHELL" isCollapsed="false">}}
git commit -m 'adding self intro' 
{{< /code >}}
`-m`はコマンドのパラメーター、`' '`の中にはコミットのときのメッセージを指定します。変えてもいいし、そのままでもOKです。英語でも日本語でも何語でもいいですが、必ず何かを書かなくちゃいけないです。変更内容を短く記述するのが通例です。

コミットが成功したら、最後は自分のパソコンからGitHubのサーバーにアップします。Git用語ではPushといいます。Pushするには、githubのユーザアカウントと[https://github.com/settings/tokens](https://github.com/settings/tokens)から発行できるトークンが必要です。

{{< code language="SHELL" isCollapsed="false">}}
git push
{{< /code >}}

これでめでたく、自己紹介の内容がアップされました。すぐにウェブサイトには公開されませんが、マイケルが公開の手続きをすれば、されます。



