---
title: "watarutaru.com // ブログの立ち上げに向けて考えたこと"
date: 2018-10-11T21:08:16
category: blog
tags: []
description: "ようやく完成しました！ watarutaru.com。ドメイン取ってから1年半もかかってしまった。久しぶりに自 […]"
originalUrl: "http://watarutaru.com/hello-watarutaru-com/"
sourceUrl: "https://web.archive.org/web/20181011210816/http://watarutaru.com/hello-watarutaru-com/"
archivedAt: 20181011210816
---
# [watarutaru.com watarutaru.com](/web/20181011210816/http://watarutaru.com/)

26

  

Aug.

2014.08.26

## watarutaru.com // ブログの立ち上げに向けて考えたこと

![hello-watarutaru01](https://web.archive.org/web/20181011210816im_/http://watarutaru.com/wp/wp-content/uploads/2014/08/hello-watarutaru01.png)

ようやく完成しました！ watarutaru.com。ドメイン取ってから1年半もかかってしまった。久しぶりに自分で実装する機会になって、何から何までわからずじまいの勉強会になりました。ひとまず完成！ そして、残りは公開後対応、、、ということに笑

### watarutaru.comブログの立ち上げにあたって

「watarutaru.com」のドメインを取った時からブログはやりたいなぁと思っていたのだけど、書きたいことも、位置づけも、ターゲットもコンセプトも何も無いままはじめていいのだろうか……とうじうじしてました。で、最近頭が弱くなったのか「そういうの別に気にしなくていいか、とにかくやっちゃえ！」っていう気持ちが強くなってきたのでやっちゃいました。

構想というか、やりたいなーって口で言ってた期間は1年以上あったけど、ようやくこのドメインに何かしらアップロードできました。ドメイン閉じるまで永遠と[「卒論つらい」ページ](https://web.archive.org/web/20181011210816/http://watarutaru.com/wother/sotsuron)でしかないかと焦っていたところ。

##### 「卒論つらい」ページ

卒論が進まなくてつらすぎた大学4年の12月のある日、突然思い立って「watarutaru.com」のドメインを取得して、卒論がつらいことを表現したページ。なんの役にも立ちませんでした。

#### watarutaru.comでやること

* 作ったものとかの掲載
* ブログ自体の運用・改修での勉強
* キャンペーンとか、制作系のアウトプット()のため
* ダラダラ文章を書くためのばしょ
* （そのうち）ちゃんとしたポートフォリオにしたいなぁ

……しかしリストに上げると途端にどうでもいいものに見えてくるね。バナー広告っぽいものがあえてスルーされるみたいな感じかな。リスト化は思考を停止する。世の中のリストに上げるって行為に絶望したよ。

まぁ、仕事の中で「自分で手を動かして作る」ことが少ない今、貴重な場所になるかなぁとも。名刺に堂々とURL書いてあちこちに配って回ったわりにしばらくTOPが[「卒論つらい」ページ](https://web.archive.org/web/20181011210816/http://watarutaru.com/wother/sotsuron)だったことは本当に反省しています。

### やってみたこと

せっかくなので、と、いくつか（自分の中での）チャレンジも取り入れました。どれも、実際にガンガン作っている人達からはなんぞ今更、というものばかりだと思いますが。僕の場合はリハビリとかも兼ねて。

#### WEBフォントの導入

![hello-watarutaru02](https://web.archive.org/web/20181011210816im_/http://watarutaru.com/wp/wp-content/uploads/2014/08/hello-watarutaru02.png)

気になってたけど特に使うシーンもなく触れていなかったWEBフォント。watarutaru.comでは全面的にGoogleの［Noto Sans Japanese］を導入してみました。（あと、Google fontsでDosisも）Noto Sansシリーズ初のcjkフォントとして、GoogleとAdobeからリリースされて話題になりましたね。

実はこのNoto Sans Japaneseがリリースされた2014/07/16は、僕の誕生日！ ……ということで勝手な親近感もあって、また素敵な画面のブログにしたいと思って入れてみた次第です。日本語のWEBフォントということでやっぱりネックなのはファイルサイズかな……かなり読み込みにラグはある感じ。。サブセット化も検討しつつ、ひとまず本文もNotoにしたまま様子を見ようと思っています。

Adobeからリリースされている方は（同じフォントだけど）Source Han Sans［源ノ角ゴシック］という名前で出ていますよね。Notoの方が響きがかわいいので好きです。でも、［源ノ角］の乙な感じも捨てがたくて、どっちにするか2日ぐらい迷いました。

##### Noto Sansフォントについて詳しく

Noto SnasフォントについてはStocker.jpで詳しくまとめられています。ご参照ください。

GoogleとAdobeのフォントNoto Sans（Source Han Sans）の画期的なところ | Stocker.jp / diary [http://stocker.jp/diary/noto-sans/](https://web.archive.org/web/20181011210816/http://stocker.jp/diary/noto-sans/ "Stocker.jp")

#### レスポンシブ対応

![hello-watarutaru03](https://web.archive.org/web/20181011210816im_/http://watarutaru.com/wp/wp-content/uploads/2014/08/hello-watarutaru03.png)

いまさらですが、自分の手でレスポンシブ実装したのは初めてでした。とはいっても、そもそも1カラムだし大変なことはなにもはないのだけど。

なんとなくでしか知らなかったことを、こうやってきちんと拾いなおしていけるのは幸せなことですね。そのうち、やっぱりカラム増やしてなんか入れたい〜とか、そういうのが出てくるかもしれないし、その時の柔軟性に期待もこめて。

#### 画像を極力避けて……

![hello-watarutaru04](https://web.archive.org/web/20181011210816im_/http://watarutaru.com/wp/wp-content/uploads/2014/08/hello-watarutaru04.png)

CSSでの装飾に徹しました。ロゴは手を抜いて画像。だけど少なくとも近いうちにsvgにしたいなぁと思っています。

もともとミニマル寄りなのがすごく好きだし、あとフラットとかなんとか流行っているしで、SNSシェアボタンとかもCSSでシンプルに。その他もコテコテしないものにしたつもりです。雑誌を作りたいな〜っていう思いがあるので「紙ものっぽく」というのも、ちょっとした裏テーマ。だから文字がちょっと小さめです。

#### WordPressオリジナルテーマで

![hello-watarutaru05](https://web.archive.org/web/20181011210816im_/http://watarutaru.com/wp/wp-content/uploads/2014/08/hello-watarutaru05.png)

テーマと言えないかもだけど、Wordpressで作りました。これが大変だった……。サーバーのこととか、phpとか、？？の連続でなんや勉強せなあかんなーという所感。次は、汎用性あるテーマとか作って配布してみたいなー。自分のだと、改修しながらやっていけばいいやって雑になっちゃうし。

### そんなわけで……

watarutaru.comでいろいろ書いていきます。今後よろしくお願いいたします！

[ページの一番上に戻る](#top)

[Facebook](https://web.archive.org/web/20181011210816/http://www.facebook.com/share.php?u=http://watarutaru.com/hello-watarutaru-com/)
[twitter](https://web.archive.org/web/20181011210816/http://twitter.com/share?url=http://watarutaru.com/hello-watarutaru-com/&text=watarutaru.com // ブログの立ち上げに向けて考えたこと-watarutaru.com)
[Hatena](https://web.archive.org/web/20181011210816/http://b.hatena.ne.jp/entry/http://watarutaru.com/hello-watarutaru-com/ "watarutaru.com // ブログの立ち上げに向けて考えたこと")
[pocket](https://web.archive.org/web/20181011210816/http://getpocket.com/edit?url=http://watarutaru.com/hello-watarutaru-com/&title=watarutaru.com // ブログの立ち上げに向けて考えたこと)
[Google+](https://web.archive.org/web/20181011210816/https://plus.google.com/share?url=http://watarutaru.com/hello-watarutaru-com/)

関連してそうな記事

- [See you ‘again’ 2015.](https://web.archive.org/web/20181011210816/http://watarutaru.com/see-you-again-2015/ "See you ‘again’ 2015.")
- [代々木の隠れ家的美容室「groove」のWEBサイトを作りました](https://web.archive.org/web/20181011210816/http://watarutaru.com/groove-web/ "代々木の隠れ家的美容室「groove」のWEBサイトを作りました")
- [［書籍工暦］文学フリマガイド 二〇一五 第七号 のデザインを担当しました](https://web.archive.org/web/20181011210816/http://watarutaru.com/bunfree-guide07/ "［書籍工暦］文学フリマガイド 二〇一五 第七号 のデザインを担当しました")

© 2018 watarutaru.com. All rights reserved.
