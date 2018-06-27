<style>
/* 吹き出し本体 */
.balloon1{
  position: relative;
  padding: 20px;
  border-radius: 10px;
  color: #ffffff;
  background-color: #0888ff;
  margin-left: 110px;          /* 左に余白を設ける */
}
/* 画像 - 絶対配置で左上に配置 */
.balloon1 .icon{
  position: absolute;
  left: -110px;
  top: 0;
}

/* 三角アイコン */
.balloon1::before{
  content: '';
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  left: -15px;
  top: 20px;
  border-right: 15px solid #0888ff;
  border-top: 15px solid transparent;
  border-bottom: 15px solid transparent;
}

/* 吹き出し本体 */
.balloon2{
  position: relative;
  padding: 20px;
  border-radius: 10px;
  color: #ffffff;
  background-color: #ff9030;
  margin-right: 110px;          /* 右に余白を設ける */
}

/* 画像 - 絶対配置で右上に配置 */
.balloon2 .icon, .baloon22 .icon{
  position: absolute;
  right: -110px;
  top: 0;
op: 0;
}

/* 三角アイコン */
.balloon2::before{
  content: '';
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  right: -15px;
  top: 20px;
  border-left: 15px solid #ff9030;
  border-top: 15px solid transparent;
  border-bottom: 15px solid transparent;
}

del {
  width: 3pt;
}
</style>


# プロローグ
今回、なぜプログラミングがテーマの一つになったのか･･･。そして、何故、講師を引き受けることになってしまったのか･･･。

ま、受講者にとってはどうでも良いことかも知れないが、それなりのストーリーがそこにはある（かもしれない）ので、一応まとめておきたい。


時は2017年秋。北海道大学工学部で日本原子力学会秋の大会が開催され、筆者も参加していた。現地委員をされていた某C先生は忙しそうにしていたが、少し時間がとれそうということで、とある教室にて雑談をしていたところ、急転直下、つぎのようなネタフリがあった。


<div class="balloon1" style="margin-top:2em; margin-bottom:4em;">
  <div class="icon"><img src="https://4.bp.blogspot.com/-dzDIvDO6pY0/V-Nn4U9fhYI/AAAAAAAA-DQ/1oq7TpFspDMEC2P4iVFyDN_lt5h8IQh3QCLcB/s800/shinpai_man.png" width=80></div>
次の炉物理夏期セミナーは北大が幹事なんですが、何か良いアイデアは無いですかね～？
</div>



少し前にあった第49回炉物理夏期セミナーでも講師を<span style="text-decoration:line-through;color:red;"><span style="color:black;">させられた</span></span>させて頂いたのだが、その時にあったワークショップ的な取り組みがなかなか良い印象だった。そんなわけで、ワークショップ形式にすれば、もっと踏み込んだことが出来るのではないか･･･と漠然と思っていたこともあり、ついつい後先考えず、こんなことを口走ってしまった。


<div class="balloon2" style="margin-top:1em; margin-bottom:2em;">
  <div class="icon">   <img src="https://1.bp.blogspot.com/-rBFzjQbEFj4/VhB9jvnHAmI/AAAAAAAAyzs/R1Dwa7c5l78/s800/businessman_dekiru.png" width=80></div>
そうですね～。どうせなら、ワークショップ形式で、実践しながら学ぶとかいうのはどうでしょう？例えばプログラミングとか･･･
</div>

また、最近の学生や新人は、Excel などのソフトはある程度使いこなすけれども、ある一定の規模を超えたデータ処理をやらせようとすると急に困り果てる･･･そんな傾向があるようにも感じていた。それってもしかして、プログラミングが出来ないからのではないか！？　･･･と、そんな思いもあった。

そんなこともあり、以前からもやもやと頭の中にあった「プログラミングは最強スキル。皆が持てばもっと生産性が上がるはず！」という気持ちから、先の発言が出てしまったのだ。

しかしながら、C先生はそのその瞬間を逃さず、目をキラリと光らせた<font size=1>ような気がした</font>。

<div class="balloon1" style="margin-top:2em; margin-bottom:2em;">
  <div class="icon"><img src="https://3.bp.blogspot.com/-p_KqddGXvs4/WBsAzQLBubI/AAAAAAAA_V8/ysrybUP7twsg1CHN_fqlNrPu3lvvbei_wCLcB/s800/pose_kiri_man.png" width=80></div>
プログラミング、それいいですね！　夏期セミナーは第50回目の記念すべき回ということで、ぜひお願いします。<br />ね、巽さん！
</div>



<div align="center" style="margin-top:2em; margin-bottom:2em; font-size:x-large">
しまった !? <br>
<img src="https://1.bp.blogspot.com/-taHssD3GT4Y/VfS6eeT5FGI/AAAAAAAAxQ4/ij8M8Zaofdc/s800/mokuhyou_mitatsu_man.png" width=200px>
</div>


C先生の持ち前の<span style="text-decoration:line-through;color:red;"><span style="color:black;">強引さ</span></span>リーダーシップで、あっという間に<span style="text-decoration:line-through;color:red;"><span style="color:black;">丸め込まれた</span></span>話がまとまったのであった。めでたしめでたし。

<p style="margin-top:3em">
･･･と、<font size=1>一部脚色はあるが</font>このような経緯で、過去の炉物理夏期セミナーで初めての試みである<font size=1>と思われる</font>、プログラミング演習をすることになった次第である。今から思えば、前回の講義資料の最終頁に、こうなることがあらかじめ織り込まれていたのかもしれない･･･。

## 期待される効果・効能
本 DOJO を修了した暁には、以下のような明るい未来があなたを待っている<font size=1>だろう</font>。

 + オブジェクト指向プログラミングの考え方とコーディングの基礎知識が身についている
 + 固有値問題に対する数値解法をプログラミングできる
 + 計算結果を速やかに可視化して理解を深めることができる
 + ○○さん、プログラミングできてカッコいい！ステキ!! と言われる<font size=1>かもしれない</font>

 ただし、過度な期待は禁物である。
 
## 対象者と前提条件
炉物理をテーマにプログラミングを進めていくので、拡散方程式に対する基本的な知識を持っていることを想定している。ただし、理論面については（C先生が準備した講義資料で）別途補足するので、きっちりと理解しておいてほしい。

一応、これまでにプログラミングを行ったことが無い人でも理解できるように工夫したつもりだが、もしかしたら理解しにくい部分もあるかもしれない。そんな時には、まずはインターネットで検索して調べてみよう。Youtube や Qiita.com など、情報サイトはいくらでもある。

プログラマー界隈ではこういう言葉がある。「ググレ、カス！」　おっと、いきなり下品な言葉で申し訳ないが、くだらない質問をする人ほど、何も調べずにいきなり聞いてくる傾向にある。しかし、これではいくらたってもスキルは伸びない。であるから、あえて言おう。カスであると！　（スマン）

ということで、分からないことがあれば、それが自己成長の一歩なんだと思い、まずはググってみて欲しい。そして、答えを見つけたら情報提供者に感謝し、こんどは自分が情報提供者側に回ってみてほしい。そうすることで、世の中はもっと良くなるはずだ。


## 基本的な考え方
本講義では、プログラミングに関する普遍的なスキルを炉物理をテーマとして身につけてもらうことを目的としている。とはいえ、いわゆるハイパフォーマンス・コンピューティングは目指さない。

スパコンや計算機クラスタを用いるような科学技術計算では、とにかく計算速度が速いことが第一優先とされることが多い。そのために、計算機の能力を最大限に発揮できるようなプログラミングの仕方が求められる。

たとえば、レジスタやキャッシュ利用の最適化、メモリアクセスパターンの最適化、通信方法やタイミングの最適化などなど、それこそソースコードがコンパイルされたらどのようなマシン語に変換されるかとか、実行時にCPUはどのように動くか･･･といったレベルで想像しながらコーディングする必要がある。これは、はっきり言って超マニアックな世界であり、そのような（廃人レベルの）スキルは普通の人には不要である。（が、個人的にはこういうネタは大好きである。そういえば、若かりし頃に後輩には「CPUの気持ちになれ！」とか無茶な指導をしていたなぁ･･･<font size=1>（遠い目）</font> しかし、どのようにしてコンピュータが動いているかについては、できれば興味をもって調べてみて欲しいと願う。）

上の例は極端としても、やはりプログラミングといえば、配列にデータを入れてそれを操作する・・・といったイメージを持っている人もいるかもしれない。確かにそういうプログラミングの方法もある。たとえば、Fortran や C で普通にプログラミングすると、いわゆる関数指向の書き方になって、関数（サブルーチン）に配列へのポインタを渡して・・・といったお作法になる。しかしながら、この方法だとプログラミング初心者にはとっつきにくいし、また、大規模なプログラムを書くことが極端に難しくなってしまう。

したがって、本講義では「速さ」ではなく「早さ」を目指す。

ここはものすごく大事なので、もう一回言っておこう。

<div align="center" style="margin:1em">
<strong>「速さ」ではなく「早さ」である。</strong>
</div>

つまり、計算機の性能を極限まで引き出すことを目的とするのではなく、**短時間に正確に目的を達成するかに重点を置く**ことにする。

そのためには、期待通りに動作する（信頼性が高い）誰にとっても理解しやすい（可読性の高い）プログラムを、できるだけ効率よく（手戻りを最小に）、自信を持って(テストによる裏付けを持って)書く必要があるわけで、そういったことを達成するための実践的な方法論を伝授したい。

筆者の中に暗黙知として蓄積されているノウハウをどこまで整理してお伝えできるか、ある意味筆者自身のチャレンジなのでもある。

というわけで、前置きが長かったが、次章からいよいよ本題に入っていくことにしよう。
