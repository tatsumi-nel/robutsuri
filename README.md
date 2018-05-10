# Robutsuri Programming DOJO

<div style="text-align: right;">
文責：巽　雅洋 (㈱原子力エンジニアリング)
</div>

本資料は、日本原子力学会炉物理部会が主催する「第50回炉物理夏期セミナー」のテキストの一部である。

炉物理をテーマに「プログラミングの今」を参加者に伝えることを目的として、実習形式で講義を行う。

Programming DOJO という名前は、たんなる講義や演習と違い、参加者が互いに切磋琢磨できる場を
提供したいという筆者の願いからつけられたものである。

DOJO 開校日に、すぐさま修行モードに入れるように、参加者全員には以下の事前準備を課す。
この準備ができていない者は、DOJO への入室を禁止するので注意してほしい。

## DODO 参加に必要な事前準備

### 武器の調達
DOJO 参加には、**次の武器が必須**である。これがないと、当日は戦いに参加できない
ため、会場に来る意味が120%削減されてしまうので、必ず準備おくこと。

+ コンピュータ一式
   - Windows, Mac いずれでも可
   - ただし、会場の関係からノートパソコンに限る

+ 筆記用具
   - ただし、メモなどはパソコンで取った方が効率的かもしれない

また、次のアイテムを準備しておくと、より充実したDOJO生活が過ごせるだろう。

+ モバイル Wi-Fi ルーター
+ Python 参考書
+ おやつ

DOJO 会場のホテルにも Wi-Fi 環境はあるが、多くの参加者があると見込まれており、
全員が集中してアクセスするとトラブルが発生するかもしれない。したがって、所有している人はモバイル Wi-Fi ルーターを持参し、他のファイターとシェアしてほしい。

Python 参考書については、あれば手元に置いておきたい。


### 環境構築

本DOJOでは、Python 言語を用いたオブジェクト指向プログラミングについて特訓する。
したがって、**下記の環境を必ず準備しておくこと**。

+ Python3 の環境 (Anaconda3 を強く推奨）
+ 使い慣れたエディタ (Visual Studio Code を激しく推奨）
+ Git

各環境のインストールについては、各自調べて実施しておくこと。
（気が向いたら解説を作るかもしれないが、現時点では確率は低い…）

### 事前課題

本DOJOに参加するためには、下記のことをマスターしておくこと。

+ 理論編テキストの熟読
    - DOJO での実践は、あくまでもプログラミングの部分に集中する。したがって、プログラミングを行う対象である、1次元拡散方程式の解法に関する理論的な内容については、ある程度把握しておく必要がある。
    - 計算機プログラムは、コンピュータに解き方を示すプロセスを手順化したものにすぎない。したがって、解くべき対象について熟知しておく必要がある。実のところ、プログラミングの未経験者の多くは、プログラミング作業には何か魔法があるように錯覚しがちであるが、実はそうではない。解くべき対象について、あるべき姿が理解出来ていないのであれば、決してプログラミングは出来ないのである。

+ Python による基礎的なプログラミング
    - 今回のDOJOでは、Python言語について学ぶのではない。あくまで、炉物理の問題解決を通じて、オブジェクト指向プログラミングの実践的アプローチを学ぶ機会としたい。したがって、Python言語に関する基礎的知識については、事前に学んでおくこと。例えば、DOJOにおいては下記の内容について事前に理解していることを前提とする。
        - 基本的な文法
        - 型とリテラル（リスト(list), 辞書(dictionary)など）
        - 制御構文 (if, for)
    
    - 上記の内容は、Python 言語によるプログラミングの入門書を1冊読んでおけば良い。DOJO においても適宜補足していくので、その点はあまり心配しなくても大丈夫だ。

+ エディタの使い方
    - 使い慣れたエディタがあればそれでも良いが、Python でのプログラミングのための支援機能があるものを使うことを強く推奨する。
    - 特に強いこだわりがない限り、Visual Studio Code をインストールしておこう。（Microsoftが開発し、無償で利用可能。Widnows, Mac, Linux で動作する。） DOJO 当日でも、同エディタを使って講義をおこなう。

+ タッチタイピング
    - DOJOでは、説明内容を聞きながら、サクサクと作業を行う必要がある。タッチタイピングができないと、戦闘能力は著しく低下してしまう。
    - 可能な限りタイピングスピードを高めておくこと。測定にはここが便利　https://10fastfingers.com/typing-test/english
        - 目安として、最低でも 150字/分を目指そう（できれば、200字/分）



では、諸君の検討を祈る。

当日、DOJO で会おう。