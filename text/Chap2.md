# Part 2: 炉物理プログラミング (実践編)

では、いよいよ本題のテーマである炉物理プログラミングを始めてみる。

いきなり実践に入る前に、少しだけ準備運動をしておこう。

事前課題において Python言語の基礎的な知識は習得しているはずだが、少しだけおさらいしておく。

## Python言語について

Python言語は、いま最も使われているスクリプト言語の一つだと言って良いだろう。特に、最近は機械学習・深層学習がとても注目されているが、その関連でも Pythonは非常によく使われている。

また、欧米の高等教育現場において Python の利用率は非常に高い。少し前は MATLAB がメジャーだったが、今は完全に Python が追い越したと言っても良いだろう。このように、Python は教育現場や実プロジェクトで多く用いられているため、是非とも使いこなせるようになっておきたい。

プログラミングのエッセンスはプログラミング言語に依存しない。また、プログラミング言語は互いに影響をうけあいながら発展している。したがって、一つのプログラミング言語をマスターしておけば、他の言語の習得は比較的容易に行える。このことからも、まだ本格的にプログラミングを学習していなのであれば、Python を最初に学習することをお薦めする。


### 必須文法・構文

Python の文法は非常にシンプルだ。また、構文（スコープ）がインデントにより決定されるという点が特徴で、この部分は賛否両論があるのだが、なれてしまえばそれほど気にはならない。インデントと上手く付き合うためには、「Python モード」があるエディタを活用する方が良いだろう。

#### 変数・演算

これといって特徴はない。他の言語と同様に使える。ただし、インクリメント・デクリメント演算子(++, --) は存在しないので C++使いの人は要注意。

```Python
hoge = 10
page = ( hoge + 1 ) / 2.0
page += hoge
```

#### リスト・辞書・タプル

Pythonでは、配列は リスト (list)で、ハッシュは辞書(dic) という型で実現している。タプル(Tuple)はPython独自の型で、値の変更が不可能なリストと理解すれば良い。リストはブラケット(bracket)、辞書はブレース({})、タプルは括弧(())にて表記する。リストやタプルについては、一部を切り出す「スライシング (slicing)」が可能であり、上手く使うと実装が劇的に簡単になる場合がある。

```Python
the_list = [1,2,3,4,5,6]

the_first  = the_list[0]     # 1
the_last   = the_list[4]     # 5
the_last2  = the_list[-1]    # 6
the_slice  = the_list[1:4]   # [2,3,4] 
the_slice2 = the_list[1:4:2] # [2,4]


the_dic = {'hoge':1, 'page':2, 'hogepage':3}

hoge = the_dic['hoge']           # 1
the_keys = list(the_dic.keys())  # ['hoge', 'page', 'hogepage']

the_tuple = (1,2,3)
the_first = the_tuple[0]     # 1
the_slise = the_tuple[0:2]   # (1,2)
```


#### 判断

if文の最後のコロン(:)を忘れないようにすること。また、if文の条件部分には括弧は不要である。（括弧をつけても文法上問題はないが、使わないのがPython流）　なお、「後置if」はないのが Rubyist には残念だが、Python のポリシーから考えると仕方がないところだ。

```Python
if hoge == page:
    print("hoge is the same as page!")
elif hoge > page:
    print("hoge is greater than page!")
else:
    print("hoge is smaller than page!")
```

#### 繰り返し

繰り返しには For構文とWhile構文を知っていたら十分だろう。

```Python
the_list = [1,2,3,4,5,6]
for i in the_list:
    print(i)

total = 0
idx = 1
while idx < 5:    # done when idx in [1,2,3,4]
    total += the_list[idx]
    idx += 1
print(idx,total)  # 5, 14 == 2+3+4+5

while True:
    if total > 20:
        break     # 直近のループを抜け出す
    print(total)
    total += 1
```

#### 関数定義

関数定義も簡単である。名前付き引数(named parameter)や省略値を用いることが出来るので便利だ。また、戻り値にリスト、タプル、オブジェクトを用いることで、複雑な戻り値を返すことができる。関数の役割は与えられた引数に対する関数値を返すことである。よってそれ以外の効果を「副作用(side effect)」と呼ぶ。例えば、画面に値を表示したり、データベースに記録したりするなどがある。副作用といっても、決して悪影響を及ぼすことではないので注意すること。


```Python
def die_risk (weight, food, drink="coke"):
    factor = 1.0
    if food == "salad":
        factor = 0.5
    elif food == "pizza":
        factor = 1.5

    if drink=="coke":
        factor *= 2.0

    the_risk = (weight-50) * factor
    print("Die risk: ", the_risk)   # 副作用 (side effect)

    return the_risk


die_risk(60, "salada", "water") 
die_risk(food="pizza", weight=70)
die_risk(food="humberger", drink="coke", weight=100)
```


#### モジュール
他のプログラムから再利用できるようにしたファイルのことを「モジュール」という。
モジュールには、自分でPythonを用いて作成する「通常モジュール」、あらかじめ装備されている「組み込みモジュール」、C言語など他の言語で開発された「拡張モジュール」に分類される。モジュールをパッケージとしてまとめ、「外部ライブラリ」として公開されているので、どんなライブラリがあってどのように使えるのかを知っているかどうかで効率が劇的に変わる。欲しいライブラリは、大抵の場合、既に誰かによって開発されている。車輪の再発明を行わないためにも、事前に入念な調査が必要だ。

モジュールの読み込みは import 文を用いて行う。

```Python
import random      # 乱数に関する組み込みモジュール
from math import sin, cos   # math モジュールから sin, cos 関数を使う

random.random()    # 0.9065161930701089
sin(0), cos(0)     # (0.0, 1.0)
```


#### クラス定義

Python におけるクラスの定義は、他の言語とよく似ており、特に難しいところは無いだろう。メソッドの定義において、第一引数が自分自身を現すselfとなる点に注意。(C++のthisに相当） なお、コンストラクタメソッドは \_\_init\_\_ である。 内部変数にアクセスする場合には、かならず self が必要なので注意が必要だ。

##### worker.py
```Python
import random

class Worker:

    def __init__(self, initial_energy=10):
        self.energy = initial_energy

    def eat(self, the_energy):
        print("Got energy {:.1f}".format(the_energy))
        self.energy += the_energy

    def sleep(self, duration):
        print("Seeep {:.1f} hours".format(duration))
        self.energy += 5.0 * duration

    def work(self, duration):
        print("Work  {:.1f} hours".format(duration))
        self.energy -= 10.0 * duration

    def get_energy(self):
        return self.energy

    def is_alive(self):
        if self.energy > 0:
            return True
        else:
            return False

      
guy = Worker()

ENERGY_UNIT = 10
SLEEP_UNIT = 8
WORK_UNIT  = 8

while True:
    feed_energy = random.random() * ENERGY_UNIT
    guy.eat(feed_energy)

    sleep_duration = random.random() * SLEEP_UNIT
    guy.sleep(sleep_duration)

    work_duration = random.random() * WORK_UNIT
    guy.work(work_duration)

    if guy.is_alive():
        print("   Still Alive: {:.2f}".format(guy.get_energy()))
    else:
        print("   DEAD: {:.2f}".format(guy.get_energy()) )
        break
```

実行例はこちら。なお、乱数を使っているので、実行毎に結果は異なる。これも一種のシミュレーションと言えるか!?

~~~
Got energy 9.3
Seeep 6.8 hours
Work  4.4 hours
   Still Alive: 9.83
Got energy 4.7
Seeep 7.5 hours
Work  5.5 hours
   DEAD: -2.62
~~~


## １群1次元拡散ソルバーの実装

ではいよいよ本題に入ろう。本節では、炉物理計算で最も簡単な問題に該当する、1群1次元拡散方程式を解くプログラムを作っていく。計算コードというほど大げさなものでは無いが、ここでは敢えてそういう言い方をしよう。

さて、一言に1群1次元拡散計算コードといえど、解くための数値解法や実装方法はたくさんある。それらを列挙するのは本講義の本題では無いため、いきなり結論を述べるが、ここでは応答行列法に基づくソルバーを実装していくことにする。

なお、拡散方程式の応答行列法に基づく求解については、夏期セミナーテキストの千葉先生による解説を参照されたい。


### Step0: 全体構想を練る

計算コードであれ、何であれ、システムを構築する際には全体構成を考えておく必要がある。この際のポイントを挙げておこう。

  1. システムの目的を明確にする
  2. システムを幾つかのサブシステムに分割する
  3. 上記の 1. と 2. を細分化出来ないところまで実施する
  4. サブシステムの内部状態と外部との関わり（インターフェース）を規定する
  5. サブシステムと上位システムのインターフェースを規定する
  6. システム間のインターフェースが上手く機能するかチェックする
  7. マクロ側の視点から、全体フローが問題なく流れそうかをチェックする
  8. 納得がいくまで上記ステップを繰り返す

さっぱり意味不明だ･･･と思ったとしても安心して欲しい。

こういったプロセスを上流工程設計と言うが、実はかなりの経験を積まないと適切な設計を行うことは難しい。というのも、上流工程における検討作業は非常に抽象度が高く、システムのデザインパターン・アンチパターンについての知識や、設計文書を作成する技術を習得する必要があるからだ。特に後者については、UML (Unified Modling Language) と呼ばれる表記法を用いることが多い。これを勉強しておけば、複雑なシステムの設計に対しても、自信を持って対応することが出来るようになるだろう。興味がある読者はぜひ調べてみて欲しい。

さて、本題に戻ろう。

ここでは、1群1次元拡散計算コードのシステム設計を行っていく訳だが、どのように考えれば良いのだろうか？　具体的に考えてみよう。

オブジェクト指向分析を行う場合、現実世界をプログラムの世界にある程度直接的にマッピングするという方法が有効だ。もちろん、この方法が唯一の方法ではないが、人間の思考パターンやオブジェクト指向の考え方に沿っているため、直感的に理解しやすいからだ。

---
##### Tips: システム設計で常に意識しておきたいこと
システムを開発する際に重要視すべきことは、大規模になれば大規模になるほど、そのライフサイクルが長くなるという事実だ。これは、保守期間が長くなるということを意味する。そのシステムに自分自身がずっと関わるのであればまだ良いが、多くの場合は将来にわたって複数の人が関与することになる。この際、最も重要視すべきものは、実装中のコメントでも外部のドキュメントでもなく、分かりやすい設計（と実装）自体である。いくらドキュメントが整備され、コメントが詳細に記載されていても、難解な設計だったり「ダメダメな設計」だったとしたら目も当てられない。

ここで言う分かりやすい設計とは、上記で述べたように、直感的に理解できるプログラム構造やオブジェクトクラスへの分割を意味する。あと、忘れてはいけないもう一つの重要なことは、将来の自分は他人と同じであるという事実だ。完璧な記憶を持つ人で無い限り（ほぼ全ての人がそうだろう）、自分が設計した内容であっても時間が経てばその詳細は忘れてしまう。ただし、分かりやすい設計であれば、見た瞬間に理解したり記憶を呼び戻したりするだろう。理想的な設計とは、かくあるべきである。

---

思いっきり脱線してしまったので、再び本題に戻ろう。

今のテーマは拡散方程式を解いて、実効増倍率や中性子束分布を求めることだ。なので、計算体系を定義して、その媒質中における中性子の拡散現象を取り扱う必要がある。

ということで、システムの設計をしなければならないあなたは、次のような考えを巡らすことだろう･･･。

---
##### (あなたの頭の中の声)
取り扱うべき対象は計算体系だから、マクロからミクロに視点をずらしていけば、その本質は、媒質の中で断面積と反応しながら中性子が拡散する･･･ということだな。だったら、中性子や断面積をオブジェクトとして表現すれば良いかな？　ほんでもって、これ以上に分割できそうにないから、これが最も詳細なレベルのサブシステムということで良いかな？　よし、じゃぁ仮に Neutron クラス、CrossSection クラスとすることにしよう。

そしたら、この中性子や断面積といったオブジェクトは、誰がどのようにして取り扱えば良いだろう･･･。今度はミクロ（詳細）なレベルから、マクロな（より上位の）レベルに視点を戻してみよう。

計算機で取り扱うには、特に今回のような決定論的手法だったら、どうしても避けられないのが離散化だよね～。ということは、媒質をメッシュとかノードに分割する必要があるよね。であれば、仮に計算ノードという一単位を作って、この中に中性子や断面積が含まれるとすれば、サブシステムとして都合が良いんじゃないかな？。きっとそうだ。じゃぁ、仮に Node クラスとしておこう。

となると、計算体系というのは計算メッシュの集まり考えたら都合が良いかもしれないな･･･。だったら、Container クラスとして、その内部に Node オブジェクトを管理しておけば良いんじゃないだろうか！？

Container オブジェクトは計算体系を表すから、もしかしたら、詳細メッシュ分割した Container と、粗いメッシュ分割をした Container を別々に準備して、それぞれを上手く作用させたら粗メッシュ拡散加速法とかもうまく実現できるかもしれないな！　どうすれば良いかよく分からんけど、感覚的にはそんな感じかな！？

でも、ちょっと待てよ。Container オブジェクトに計算制御部分も入れるとなると、かなり複雑なシステムになってしまうなぁ。だったら MVC モデルのように、物理量を保持するモデルクラスと実際の挙動を取り仕切る制御クラスと分離して挙げた方がよいかもしれないなぁ。Container クラスを制御するクラスだから ContainerController だな！ 我ながら安直な命名だけど、分かりやすくて良いよね～。Container オブジェクトのインスタンス1つにつき、ContainerController オブジェクトのインスタンスを用意すれば良いね。

じゃぁ、計算全体をマネジメントするのはどうすれば良いかな～。安直だけど、CalclationManager で良いだろう。うん、Simple is best!

さて、今度は全体の流れを考えてみよう。

CalculationManager が Container オブジェクトを作って、ContainerController オブジェクトに渡してあげてから、ContainerController オブジェクトに制御を頼めば良いよね･･･。

Containerオブジェクトが生まれたときに、内部に Node オブジェクトを準備する必要があるな。これには CrossSection オブジェクトが必要かな？　これは計算条件として与えられるとして、これを Node オブジェクトに渡せばいいね。

Container は ContainerController から「計算しろ」と言われたら、Container オブジェクトは内部の Node オブジェクト間で Neutron オブジェクトをやりとりしてから、Node オブジェクトに「計算しろ」と言えばよさそうだな。Node オブジェクトは隣のノードから受け取った流入中性子と、断面積から計算された応答行列を使えば、放出中性子を計算できそうだな･･･。うん、応答行列法を使えば、上手く表現できそうだ。


いや、ちょっとまてよ。

中性子のために Neutron クラスってのを考えたけど、これって必要かな？　**拡散理論の応答行列法なら、中性子流も中性子束も P0成分だけだから、たんなるスカラー量として表現できる**よなぁ。それに、中性子オブジェクトとしたところで、特に振る舞いを規定することもないから、単なる配列とかで良いんじゃね？

---

･･･というような感じで考えただろう（と、いうことにしておこう･･･）

こんな風な思考プロセスを経て、クラス構造をザックリとまとめたのが以下の図だ。

---
+ 断面積（CrossSection）
    - 断面積データの設定・保持
    - 他の断面積との足し算・引き算
    - 中性子束との掛け算
    - スカラー量（体積等）との掛け算
    - 断面積バランスのチェック

+ 計算ノード (Node)
  - 各種物理量の保持
    - 断面積
    - 平均中性子束
  - 各面の部分中性子流(流入及び放出）
  - 部分中性子流のレスポンス計算
  - ノード内の核分裂源の計算

+ 計算体系 (Container)
  - ノードの保持
  - 内側反復の計算
  - 体系内の総核分裂源の計算

+ 計算体系制御 (ContainerController) 
  - 計算体系の保持
  - 内側反復計算の制御

+ 計算全体管理 (CalculationManager)
  - 計算条件の管理
  - 計算体系制御の管理
  - 外側反復計算の制御
  - 加速計算の制御

---


### Step1: 基本的なオブジェクトの設計と実装

基本的な方針が出せたので、いよいよ実際にコーディングを始めてみよう。

ここでは、最も基本的なデータ要素となる断面積クラスを実装してみよう。

##### cross_section.py
```Python
import numpy as np

# 定数
N_REACT = 3  # D, Siga, nuSigf
DIF    = 0
SIGA   = 1
NUSIGF = 2

class CrossSection:
    """
    断面積クラス (1群)
    """

    def __init__(self, val=None):
        """
        コンストラクタ
        """
        self.x = np.zeros(N_REACT)
        if(not (val is None)):
            self.set(val)

    def set_d(self, val):
        self.x[DIF] = val

    def set_siga(self, val):
        self.x[SIGA] = val

    def set_nusigf(self, val):
        self.x[NUSIGF] = val

    def dif(self):
        return self.x[DIF]

    def siga(self):
        return self.x[SIGA]

    def nusigf(self):
        return self.x[NUSIGF]

    def debug(self):
        print("-" * 9 + " XS " + "-" * 9)
        print("D\tSiga\tNuSigf")
        print(self.x[DIF], self.x[SIGA], self.x[NUSIGF], sep='\t', end='\n')
        print("-"*22)

if __name__ == '__main__':
    xs = CrossSection()
    xs.set_d(1.0)
    xs.set_siga(2.0)
    xs.set_nusigf(3.0)
    xs.debug()

```

クラス定義やメソッド定義の直下にはコメントを入れることが出来るので、必要に応じて入れると良いだろう。

最初ということで、必要最小限のメソッド群を定義している。具体的には、コンストラクタ(\_\_init\_\_)、拡散係数の設定(set_d)、吸収断面積の設定(set_siga)、生成断面積の設定(set_nusigf)、拡散係数の取得(dif)、吸収断面積の取得(siga)、生成断面積の取得(nusigf)、デバッグ用メソッド(debug)である。最後のデバッグ用メソッドについては、文字列化する特殊メソッド \_\_str\_\_ として定義する方法もある。

ここで、数値演算用ライブラリである Numpy を用いていることに注目して欲しい。Numpy は Python で高速に計算させる場合には必須なので、必ずチェックしておこう。

最後の if ブロックは、このスクリプトを

```bash
python cross_section.py
```

と実行した際に流れる部分であり、よく使われるテクニックであるので、これも覚えておこう。

さて次に、計算ノードも実装しておこう。こんな感じになる。

##### node.py
```Python
import numpy as np
from cross_section import CrossSection
from config import *

class Node:
    def __init__(self, xs=None):
        self.jout = np.ones(2)    # out-going, [XM, XP]
        self.jin  = np.ones(2)    # in-coming, [XM, XP]
        self.flux  = 1.0    # average flux
        self.width = 1.0
        self.xs = None
        self.keff = 1.0
        self.fis_src = 1.0
        if(xs):
            self.set_xs(xs)

    def set_xs(self, val):
        self.xs = val

    def calc(self):
        pass

    def debug(self):
        print("-"*3 + " Node " + "-"*40)
        print("  jin_XM \t", self.jin[XM] )
        print("  jin_XP \t", self.jin[XP])
        print("  jout_XM\t", self.jout[XM])
        print("  jout_XP\t", self.jout[XP])
        print("  flux   \t", self.flux)
        print("  keff   \t", self.keff)
        self.xs.debug()
        print("-"*50)


if __name__ == '__main__':
    node = Node()
    xs = CrossSection()
    xs.set_d(1.0)
    xs.set_siga(2.0)
    xs.set_nusigf(3.0)
    node.set_xs(xs)
    node.debug()
```

冒頭の import 文で、CrossSection オブジェクトの定義を cross_section.py から読み込んでいる。また、次の config.py で定義されている定数を読み込んでいる。

```Python
# 定数

## 方向
XM = 0
XP = 1
```

Node では、部分中性子流、中性子束、メッシュ幅、断面積オブジェクト、実効増倍率、核分裂源をそれぞれ定義している。

calcメソッドもとりあえず定義しているが、現時点で実態は無い。とりあえず、メソッドだけを準備しておくということは初期の段階で良くやる方法だ。


### Step2: テストコードを準備する

次に、いよいよテストコードを準備する。テスト駆動開発に慣れてくれば、いきなりこのステップから始めても良い（というか、むしろその方が自然）。

ここで問題が出てくる。それは、実際のコード本体とテストコードが混在してしまうということだ。この回答として、それぞれを別々のディレクトリに集約するということを良くやる。たとえばこんな感じだ。

~~~
(project_root) ----+ (ここにメインプログラムを配置)
                   |
                   +--- lib----+--- cross_section.py
                   |           |
                   |           +--- node.py
                   |
                   +--- tests--+--- test_cross_section.py
                               |
                               +--- test_node.py
~~~

ではさっそく実際のテストコードを見てみよう。

##### test_cross_section.py
```Python
import unittest

import sys
sys.path.append('../lib')

from node import Node
from cross_section import CrossSection

class CrossSectionTest(unittest.TestCase):

    def test_sets(self):
        xs = CrossSection()
        xs.set_d(1.0)
        xs.set_siga(2.0)
        xs.set_nusigf(3.0)
        self.assertEqual(xs.dif(), 1.0)
        self.assertEqual(xs.siga(), 2.0)
        self.assertEqual(xs.nusigf(), 3.0)
 
    def test_sets3(self):
        xs1 = CrossSection()
        xs1.set([1.0, 2.0, 3.0])
        xs1_ref = CrossSection()
        xs1_ref.set(xs1)
        self.assertEqual(xs1, xs1_ref)
    

if __name__ == '__main__':
    unittest.main()
```

なんとなく「読める」と思うが、いかがだっただろうか？

ここでは、単体テスト・フレームワークのライブラリである unittest を用いた。Python に標準ライブラリとして準備されているので、すぐに使えて便利だ。

unittest では、各テストメソッドは名前が test から始まる規約となっているので、そのような命名ルールになっている。各メソッドでは、CrossSection オブジェクトを生成してから、各断面積の値をセットしている。そして、assertEqual メソッドにて、第一引数と第2引数が等しいかどうかをチェックしている。assert 系メソッドにはいろいろあるので、目的に応じて使い分けると良い。

ところで、cross_section.py や node.py が異なるディレクトリ (../lib) にあるため、import の際の読み込みパスを追加している点に気をつけて欲しい。これを忘れると import 時にエラーとなるので注意が必要だ。


では、このテストを実行してみよう。下記のようにテストが成功するはずだ。

~~~
% python test_cross_section.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
~~~

えっ？ なんでこんな面倒くさいことをするのかって？

まぁ、この段階では面倒な部分しか見えないだろう。しかし、テストコードを書くということは、幾つものメリットがあるのだ。そのうちの大きなものとしては、次の3つが挙げられる。

- テストコードの作成を通じて、必要なロジックを素早く書ける
- 常にテストを実行することで、いち早くエラーを検出できる
- テストコードが上位層クラスにおけるメソッドのひな形になる


最初にテストを書く "Test First" の姿勢を取っていれば、木を見て森を見ずという状態にはなりにくい。というのも、**テストコードが「成功」する状態にするために、ライブラリに記述する最小限のコードに集中できる**からだ。これが1番目のメリット。いったんテストコードが成功すれば、さらに、**システムがあるべき姿になったときに成功すべきテストコードを追加する**。そして、次にこのテストが成功するようにライブラリを作っていく･･･。あとはこの繰り返しによって、必要なロジックを素早く書くことができる。

繰り返しテストを実行しているわけであるから、万一エラーが発生したとしても、**テストがもれなく・重複なく作成されている限り**、その段階ですぐに見つかる。これが二番目のメリット。テスト駆動開発の要はテストコードをしっかり書くということに他ならない。そのため、テストコードの行数がライブラリ本体よりもずっと多いというプロジェクトも決して珍しくない。「テストを最初に書いて、それが成功するようにライブラリ本体を書く」とう発想の転換は最初は衝撃的かもしれないが、すぐに慣れてくる。そのうち、テストコードを書いてテストを通すのが快感(?)になってくるはずだ。なぜなら、テストコードはテストのためにあるのでは無く、**クラスの使われ方（ユースケース）を決定するために作成するもの**だからだ。

そして3番目のメリットについては、なかなか言葉だけでは説明が難しいので、後で事例を示して説明することにしよう。


ということで、次に行く前に Node クラスのテストコードも示しておこう。

##### test_node.py

```Python
import unittest

import sys
sys.path.append('../lib')
import math

from config import *
from cross_section import CrossSection
from node import Node

class NodeTest(unittest.TestCase):

    def test_onenode(self):
        node = Node()
        xs = CrossSection([1.36, 0.0181, 0.0279])
        #xs.debug()
        node.set_xs(xs)
        node.set_keff( xs.nusigf() / xs.siga() )    
        node.calc()

        for k in range(100):
            jout_xm = node.get_jout(XM)
            jout_xp = node.get_jout(XP)
            node.set_jin(XM, jout_xm)
            node.set_jin(XP, jout_xp)
            node.calc()

        node.debug()

        self.assertEqual(node.get_jout(XM), node.get_jout(XP))
        self.assertEqual(node.get_jin(XM), node.get_jout(XM))
        self.assertEqual(node.get_jin(XP), node.get_jout(XP))
        self.assertEqual(node.get_jout(XM)+node.get_jin(XM), node.get_flux() / 2.0)


if __name__ == '__main__':
    unittest.main()
```

先にも述べたように、このテストコードにおいて Node クラスの実際の使われ方(ユースケース)を定義している。このテストが成功するように Node クラスの実装を整備していくのだ！


テストコードが通るようになった段階で、Git リポジトリを作成し、コミットしておこう。

```bash
git init
git add .
git commit -m "initial import"
```


### Step3: CrossSectionクラスの拡張

次に、CrossSection クラスをもう少し拡張していこう。最初にやることは･･･そうだ、テストを書くことだ！  test_cross_section.py に次のテストを追加しよう。

##### test_cross_section.py への追加部分

```Python
   def test_operation_add(self):
        xs1 = CrossSection([1.0, 2.0, 3.0])
        xs2 = CrossSection([2.0, 3.0, 4.0])
        xs3 = xs1 + xs2
        xs3_ref = CrossSection([3.0, 5.0, 7.0])
        self.assertEqual(xs3, xs3_ref)

    def test_operation_sub(self):
        xs1 = CrossSection([1.0, 2.0, 3.0])
        xs2 = CrossSection([2.0, 3.0, 4.0])
        xs3 = xs2 - xs1
        xs3_ref = CrossSection([1.0, 1.0, 1.0])
        self.assertEqual(xs3, xs3_ref)

    def test_operation_mul(self):
        xs1 = CrossSection([1.0, 2.0, 3.0])
        xs2 = xs1 * 2.0
        xs2_ref = CrossSection([2.0, 4.0, 6.0])
        self.assertEqual(xs2, xs2_ref)

        xs3 = 2.0 * xs1
        xs3_ref = CrossSection([2.0, 4.0, 6.0])
        self.assertEqual(xs3, xs3_ref)

        xs4 = 2.0 * xs1 * 3.0
        xs4_ref = CrossSection([6.0, 12.0, 18.0])
        self.assertEqual(xs4, xs4_ref)
```

先ほどのテストとの違いは次の３つだ。

+ コンストラクタに引数を取れるようにした
+ 足し算、引き算、掛け算を定義
+ オブジェクト同士の比較を定義

以上のコードを追加したテストが成功するように、CrossSectionクラスを拡張していこう。
以下に拡張例を示しておく。

##### cross_section.py への追加部分
```Python
    def __eq__(self, other):
        return np.allclose(self.x, other.x)

    def __mul__(self, factor):
        xs = CrossSection(self)
        xs.x *= factor
        return xs

    def __rmul__(self, factor):
        xs = CrossSection(self)
        xs.x *= factor
        return xs

    def __truediv__(self, factor):
        xs = CrossSection(self)
        xs.x *= (1.0/factor)
        return xs

    def __neg__(self):
        return self * (-1.0)

    def __add__(self, other):
        xs = CrossSection(self)
        xs.x += other.x
        return xs

    def __sub__(self, other):
        xs = CrossSection(self) + (-other)
        return xs
```


### Step4: Nodeクラスの拡張

次に、Node クラスのテストを拡張しよう。いよいよ、応答行列法を用いた Red/Black Iteration の実装に入ってくる。

べき乗法 (Power Method)による固有値問題の基本的な解法は次のようになる（詳細は、別途理論編を参照されたい）

なお、ここでは zero flux 境界条件を仮定している。基本的なアルゴリズムは次の通りだ。

---
#### 基本的なアルゴリズム

1. 初期の核分裂中性子源を設定する。体系全体の全核分裂源(total_fis_src) / keff が 1.0となるように規格化する。

2. 内側反復計算において
    - 自ノードへの流入中性子流を準備する （隣のノードの放出中性子）
        - ただし、境界部においては、自分の放出中性子流の符号を反転させたものを用いる
    - 応答行列を用いて、放出中性子流と中性子束を求める

3. 更新された中性子束を用いて核分裂源を計算する

4. 実効増倍率 = 今回の核分裂源 / ( 前回の核分裂源 / 前回の実効増倍率 )

5. 収束していなければ 2. へ戻る

---


これをテストコードに落とし込んだものが次だ。

**ここが本講義で最も重要なステップなので、以下のコードをよーく見て欲しい。** 


```Python
import unittest

import sys
sys.path.append('../lib')
import math

from config import *
from cross_section import CrossSection
from node import Node

class NodeTest(unittest.TestCase):

    def test_uniform_zeroflux_bc(self):
        xs_fuel = CrossSection([1.36, 0.0181, 0.0279])
        delta = 1.0
        geom = [{'xs':xs_fuel, 'width':100}]

        nodes = []
        for r in geom:
            for k in range(int(r['width']/delta)):
                the_node = Node(r['xs'])
                the_node.set_width(delta)
                nodes.append(the_node)

        keff = 1.0
        keff_old = 1.0
        total_fis_src_old = 1.0
        conv = 1.0e-7

        for idx_outer in range(2000):  # outer iteration

            # calculation of total fission source
            total_fis_src = 0.0
            for the_node in nodes:
                total_fis_src += the_node.get_fis_src()

            # normalize fis src to make total fis src unity
            norm_factor = 1.0 / (total_fis_src/keff)
            for the_node in nodes:
                the_node.normalize_fis_src(norm_factor)

            # inner iteration with fixed fis src
            for istart in range(2):  # start color (0: red, 1:black)
                for ix in range(istart, len(nodes), 2):
                    if(ix==0):  # left boundary
                        jin_xm = -nodes[ix].get_jout(XM)
                    else:
                        jin_xm = nodes[ix-1].get_jout(XP)

                    if(ix==len(nodes)-1):  # right boundary
                        jin_xp = -nodes[ix].get_jout(XP)
                    else:
                        jin_xp = nodes[ix+1].get_jout(XM)

                    nodes[ix].set_jin(XM, jin_xm)
                    nodes[ix].set_jin(XP, jin_xp)
                    nodes[ix].calc()

            # calculation of new fission source
            for the_node in nodes:
                the_node.calc_fis_src()

            # calculation of total fission source
            total_fis_src = 0.0
            for the_node in nodes:
                total_fis_src += the_node.get_fis_src()

            # estimation of eigen value as a ratio of generations
            keff = total_fis_src / (total_fis_src_old/keff_old)

            diff = abs((keff - keff_old)/keff)
            #print( idx_outer, keff, diff)

            if(diff < conv):  
                break

            keff_old = keff
            total_fis_src_old = total_fis_src

            # set new eigen value to all the nodes
            for the_node in nodes:
                the_node.set_keff(keff)

        # reference as analytical solution
        kana = xs_fuel.nusigf() / (xs_fuel.dif() * math.pi ** 2 / 100**2 + xs_fuel.siga())
        #print( 'kana = ', kana)
        self.assertAlmostEqual(keff, kana, places=5)
```

いかがだっただろうか？　よく分からなかった？？　基本的にはアルゴリズムを忠実にコードの落とし込んだものだから、理解できるまで何度でもコードを読んで欲しい。

なんとなくでも良いので、理解出来れば次のステップにいくとしよう。

もうお分かりと思うが、このテストコードが成功するように Node クラスを拡張していく。ここで肝となるのが、応答行列法による計算部分だ。詳細は理論編を参照するとして、ここではエッセンスを示しておく。

---
#### 応答行列法を用いた拡散方程式の解法

1. 着目メッシュ <img src="https://latex.codecogs.com/gif.latex?\inline&space;i" /> に対する流入中性子流 <img src="https://latex.codecogs.com/gif.latex?\inline&space;j^-_{i\pm1/2}" /> を既知とする。

2. 以下の式を用いてメッシュ <img src="https://latex.codecogs.com/gif.latex?\inline&space;i" /> における平均中性子束 <img src="https://latex.codecogs.com/gif.latex?\inline&space;\phi_i" />  を計算する。

<div align="center" style="margin-bottom:1em">
<img src="https://latex.codecogs.com/gif.latex?\{\frac{4 D}{\Delta x} + (1 + \frac{4 D}{\Delta x}) \Sigma_{a,i} \} \phi_i = \frac{2D}{\Delta x}(4 J^-_{i+1/2} + 4 J^-_{i-1/2})+(1+\frac{4D}{\Delta x})\Delta S_i" width=80%/>
</div>

3. 流入中性子流 <img src="https://latex.codecogs.com/gif.latex?\inline&space;J^-_{i\pm 1/2}" /> とノード平均中止子束 <img src="https://latex.codecogs.com/gif.latex?\inline&space;\phi_i" /> から、境界における中性子流 <img src="https://latex.codecogs.com/gif.latex?\inline&space;J_{i\pm 1/2}" /> を以下の式で計算する。

<div align="center" style="margin-bottom:1em">
<img src="https://latex.codecogs.com/gif.latex?J_{i\pm 1/2} = \frac{-\frac{2D}{\Delta x}(4 J^-_{i\pm 1/2}-\phi_i)}{(1+\frac{4D}{\Delta x})}" />
</div>

4. 流入中性子流 <img src="https://latex.codecogs.com/gif.latex?\inline&space;J^-_{i\pm 1/2}" /> と中性子流 <img src="https://latex.codecogs.com/gif.latex?\inline&space;J_{i\pm 1/2}" /> から、放出中性子流 <img src="https://latex.codecogs.com/gif.latex?\inline&space;J^+_{i\pm 1/2}" /> を以下の式で計算する。

<div align="center" style="margin-bottom:1em">
<img src="https://latex.codecogs.com/gif.latex?J^+_{i\pm 1/2} = J_{i\pm 1/2} + J^-_{i\pm 1/2}" />
---

上記の解法を calc メソッドに実装し、他のメソッドも準備したものが次のコードだ。

##### node.py
```Python
import numpy as np
from cross_section import CrossSection
from config import *

class Node:
    def __init__(self, xs=None):
        self.jout = np.ones(2)    # out-going, [XM, XP]
        self.jin  = np.ones(2)    # in-coming, [XM, XP]
        self.flux  = 1.0    # average flux
        self.width = 1.0
        self.xs = None
        self.keff = 1.0
        self.fis_src = 1.0
        if(xs):
            self.set_xs(xs)

    def set_xs(self, val):
        self.xs = val

    def set_keff(self, val):
        self.keff = val

    def set_width(self, val):
        self.width = val

    def get_flux(self):
        return self.flux

    def set_jin(self, dir, val):
        self.jin[dir] = val

    def get_jin(self, dir):
        return self.jin[dir]

    def get_jout(self, dir):
        return self.jout[dir]

    def get_xs(self):
        return self.xs

    def get_width(self):
        return self.width

    def get_fis_src(self):
        return self.fis_src

    def calc_fis_src(self):
        # fission source
        self.fis_src = self.xs.nusigf() * self.flux * self.width

    def normalize_fis_src(self, factor):
        self.fis_src *= factor

    def calc(self):
        #flux by Eq(28)
        coef1 = 2.0*self.xs.dif() / self.width
        coef2 = 2.0*coef1
        coef3 = 1.0 + coef2
        f_nume = coef1 * 4.0 * (self.jin[XP] + self.jin[XM]) + \
                 coef3 * self.fis_src / self.keff
        f_deno = coef2 + coef3*self.xs.siga()*self.width
        self.flux = f_nume / f_deno

        #net current by Eq(29)
        jnet_XM  = -coef1 * (4.0*self.jin[XM] - self.flux) / coef3
        jnet_XP = -coef1 * (4.0*self.jin[XP] - self.flux) / coef3

        #out-goinnt by Eq(30)
        self.jout[XM]  = jnet_XM  + self.jin[XM]
        self.jout[XP] = jnet_XP + self.jin[XP]

    def debug(self):
        print("-"*3 + " Node " + "-"*40)
        print("  jin_XM \t", self.jin[XM] )
        print("  jin_XP \t", self.jin[XP])
        print("  jout_XM\t", self.jout[XM])
        print("  jout_XP\t", self.jout[XP])
        print("  flux   \t", self.flux)
        print("  keff   \t", self.keff)
        self.xs.debug()
        print("-"*50)


if __name__ == '__main__':
    node = Node()
    xs = CrossSection()
    xs.set_d(1.0)
    xs.set_siga(2.0)
    xs.set_nusigf(3.0)
    node.set_xs(xs)
    node.debug()
```


### Step5: Contaierクラスの新設

さて、テストコードを書くことの3番目のメリットとして下記のものを挙げていたが、覚えているだろうか？

---
- テストコードが上位層クラスにおけるメソッドのひな形になる

---


先ほどの Node クラスに対するテストコードは、計算実行に必要なほぼ完全なコードだと言える。ということは、これを上手くまとめることによって、Nodeクラスを取りまとめる上位層、ここでは Container クラスのメソッドとして再利用することができるのだ。

この時、まずはこんな風にしたいな･･･というイメージを Container クラスのテストコードとして落とし込む。こんな感じだ。

##### test_container.py
```Python
import unittest

import sys
sys.path.append('../lib')
import math

from config import *
from cross_section import CrossSection
from node import Node
from container import Container

class ContainerTest(unittest.TestCase):

    def test_container(self):

        xs_fuel = CrossSection([1.36, 0.0181, 0.0279])
        delta = 1.0
        albedo = -1.0
        geom = [{'xs':xs_fuel, 'width':100}]

        cont = Container(geom, delta, albedo)
        #cont.debug()

        keff = 1.0
        keff_old = 1.0
        total_fis_src_old = 1.0
        conv = 1.0e-7

        for idx_outer in range(100):

            total_fis_src = cont.get_total_fis_src()
            norm_factor = 1.0 / (total_fis_src/keff)
            cont.normalize_fis_src(norm_factor)

            for idx_inner in range(4):
                for color in range(2):
                    cont.calc(color)

            cont.calc_fis_src()

            total_fis_src = cont.get_total_fis_src()

            keff = total_fis_src / (total_fis_src_old/keff_old)
            diff = abs((keff - keff_old)/keff)
            #print( keff, diff)
            if(diff < conv):
                break
            keff_old = keff
            total_fis_src_old = total_fis_src

            cont.set_keff(keff)


        kana = xs_fuel.nusigf() / (xs_fuel.dif() * math.pi ** 2 / 100**2 + xs_fuel.siga())
        #print( 'kana = ', kana)
        self.assertAlmostEqual(keff, kana, places=4)


        flux = cont.get_flux_dist()
        self.assertEqual(len(flux), 2)  # x, y
        self.assertEqual(len(flux[0]), int(geom[0]['width']/delta))
        self.assertEqual(flux[0][0], delta/2.0)
        self.assertEqual(flux[0][-1], geom[0]['width']-delta/2.0)
        self.assertEqual(len(flux[1]), int(geom[0]['width']/delta))


if __name__ == '__main__':
    unittest.main()
```

コードがかなりすっきりして、全体がすぐに見渡せる程度になってきた。

このテストコードが成功するように Containerクラスを定義するわけだが、その際に先ほどの Nodeクラスのテストコード (test_node.py) を横目にみながら参考にして実装していけば良い。次のような感じだ。

##### container.py
```Python
import numpy as np

from node import *
from cross_section import *


class Container:
    """
        ノードオブジェクトを保持し体系を構築する
    """
    def __init__(self, geometry, delta=1.0, albedo=0.0):
        self._setup(geometry, delta, albedo)

    def _setup(self, geometry, delta, albedo):
        self.nodes = []
        for r in geometry:
            for k in range(int(r['width']/delta)):
                the_node = Node(r['xs'])
                the_node.set_width(delta)
                self.nodes.append(the_node)

        self.delta = delta
        self.albedo = albedo

    def calc(self, color=None):
        for ix in range(color, len(self.nodes), 2):
            if(ix==0):
                jin_xm = self.albedo * self.nodes[ix].get_jout(XM)
            else:
                jin_xm = self.nodes[ix-1].get_jout(XP)

            if(ix==len(self.nodes)-1):
                jin_xp = self.albedo * self.nodes[ix].get_jout(XP)
            else:
                jin_xp = self.nodes[ix+1].get_jout(XM)

            self.nodes[ix].set_jin(XM, jin_xm)
            self.nodes[ix].set_jin(XP, jin_xp)
            self.nodes[ix].calc()

    def calc_fis_src(self):
        for the_node in self.nodes:
            the_node.calc_fis_src()

    def get_total_fis_src(self):
        total_fis_src = 0.0
        for the_node in self.nodes:
            total_fis_src += the_node.get_fis_src()
        return total_fis_src

    def normalize_fis_src(self, factor):
        for the_node in self.nodes:
            the_node.normalize_fis_src(factor)

    def set_keff(self, keff):
        for the_node in self.nodes:
            the_node.set_keff(keff)

    def get_flux_dist(self):
        x_pos = []
        x_sum = 0.0
        flux = []
        for the_node in self.nodes:
            w = the_node.get_width()
            x_pos.append( x_sum + w/2 )
            x_sum += w
            flux.append( the_node.get_flux() )
        return [x_pos, flux]


    def debug(self):
        print("nodes: ", len(self.nodes))
        for the_node in self.nodes:
            the_node.debug()
```


### Step6: ContainerControllerクラスの新設

Container クラスのテストコードでもかなりすっきりしていたが、これをもう一段階上のレベルに引き上げてみよう。そう、ContainerController の登場だ。

例のごとく、テストコードを先に書いてみる。

##### test_container_controller.py
```Python
import unittest

import sys
sys.path.append('../lib')
import math


from config import *
from cross_section import CrossSection
from node import Node
from container import Container
from container_controller import ContainerController


class ContainerContainerTest(unittest.TestCase):

    def test_container_controller(self):

        xs_fuel = CrossSection([1.36, 0.0181, 0.0279])
        delta = 1.0
        albedo = -1.0
        geom = [{'xs':xs_fuel, 'width':100}]

        container = Container(geom, delta, albedo)
        #cont.debug()

        controller = ContainerController(container)

        controller.calc()

        keff = controller.get_keff()

        kana = xs_fuel.nusigf() / (xs_fuel.dif() * math.pi ** 2 / 100**2 + xs_fuel.siga())
        #print( 'kana = ', kana)
        self.assertAlmostEqual(keff, kana, places=4)


if __name__ == '__main__':
    unittest.main()
```

ブラボー！　かなりスッキリしてきた！！

いや、まだこれはテストコードだ。このコードが動くように ContainerController 本体を書くんだ！！

書け！　書けっ！　書くんだジョー！

##### container_controller.py
```Python
class ContainerController:
    """
    Container オブジェクトを操作し、外側反復計算を行う。
    """

    def __init__(self, container=None):
        self.cont = container
        self.keff = 1.0
        self.keff_old = 1.0
        self.total_fis_src_old = 1.0
        self.conv_criterion = 1.0E-7
        self.max_outer_iterations = 500
        self.inner_iterations = 4
        self.converged = False


    def calc(self):
        for idx_outer in range(self.max_outer_iterations):

            self.total_fis_src = self.cont.get_total_fis_src()
            norm_factor = 1.0 / (self.total_fis_src/self.keff)
            self.cont.normalize_fis_src(norm_factor)

            for idx_inner in range(self.inner_iterations):
                for color in range(2):
                    self.cont.calc(color)

                self.cont.calc_fis_src()

            self.total_fis_src = self.cont.get_total_fis_src()

            self.keff = self.total_fis_src / (self.total_fis_src_old/self.keff_old)
            diff = abs((self.keff - self.keff_old)/self.keff)

            #print(self.keff, diff)

            if(diff < self.conv_criterion):
                self.converged = True
                break

            self.keff_old = self.keff
            self.total_fis_src_old = self.total_fis_src

            self.cont.set_keff(self.keff)

        return (idx_outer, self.converged)


    def get_keff(self):
        return self.keff
```

### Step7: CalculationManagerクラスの新設

よし、これでもかなり良いが、もうちょっと抽象化したい。もうちょっとだけだ。

ContainerController のテストコードをもう一段間上のレベルに引き上げよう！ こんな感じだ！

##### test_calculation_manager.py
```Python
import unittest

import sys
sys.path.append('../lib')
import math

from cross_section import CrossSection
from node import Node
from container import Container
from container_controller import ContainerController
from calculation_manager import CalculationManager

class CalculationManagerTest(unittest.TestCase):

    def test_calculation_manager(self):

        xs_fuel = CrossSection([1.36, 0.0181, 0.0279])
        delta = 1.0
        albedo = -1.0
        geom = [{'xs':xs_fuel, 'width':100}]

        config = { 'geometry':geom, 'mesh_width':delta, "albedo": albedo}

        calc_man = CalculationManager(config)
        calc_man.run()

        keff = calc_man.get_keff()

        kana = xs_fuel.nusigf() / (xs_fuel.dif() * math.pi ** 2 / 100**2 + xs_fuel.siga())
        #print( 'kana = ', kana)
        self.assertAlmostEqual(keff, kana, places=4)


if __name__ == '__main__':
    unittest.main()
```

このレベルまで来ると、計算コードがかなり抽象化されて、取り扱いが非常に楽になる。

ということで、このテストが通るように CalculationManager の本体を実装しよう！

##### calculation_manager.py
```Python
from container import Container
from container_controller import ContainerController


class CalculationManager:
    """
        計算の全体制御
    """

    def __init__(self, param):
        geom = param['geometry']
        delta = param['mesh_width']
        albedo = param['albedo']

        container = Container(geom, delta, albedo)
        self.controller = ContainerController(container)

    def run(self):
        self.controller.calc()

    def get_keff(self):
        return self.controller.get_keff()

```

今度は結構短いな･･･。これで一通りのコーディングは完了した。

テストが通ることを確認したら、リポジトリにコミットしておこう。


### Final: 完成

これでいよいよ完成だ。最終的にできあがった計算コードは次のようになる。


##### bare_1g.py
```Python
import sys

sys.path.append('lib')
from calculation_manager import CalculationManager
from cross_section import CrossSection

xs_fuel = CrossSection([1.36, 0.0181, 0.0279])
delta = 1.0
albedo = -1.0
geom = [{'xs':xs_fuel, 'width':100}]

config = { 'geometry':geom, 'mesh_width':delta, "albedo": albedo}

calc_man = CalculationManager(config)
calc_man.run()

keff = calc_man.get_keff()

print ("keff = ", keff)
```

もう気づいたと思うが、実はこれは CalculatiomNanager のテストコードそのものだ。

今まで書いてきた部分は、いわゆる計算カーネル (claculation kernel) と言うべき中心的部分だ。実際の計算コードでのでは、計算カーネルはむしろ20%程度で、入出力とそれに関わるエラーチェックが80%程度を占めるといっても過言では無い。本講義での目的は、プログラミングの方法論の根幹部分について議論することである。したがって、入出力等の補助的な部分については割愛するが、ニーズに応じて読者の自学自習に期待したい。


ここまでにおいて、CrossSection クラスや Node クラスといった基本的なクラスの定義やテストコードの作成から始まり、徐々に上位の階層におけるテストコードの作成を通じて、最終目的である計算コードの作成にたどり着くことが出来た。

もちろん、必ずしも常にボトムアップでスムーズに開発出来るとは限らない。上位層の設計・実装が思惑通り行かず、階層の設計・実装をやり直すということは良くあることである。多かれ少なかれ試行錯誤は発生するだろうが、経験をつんで自分なりの定石のパターンを築き上げれば、手戻りは少なくなって行くであろう。

また、理論編でも述べたように、デザインパターン、アルゴリズム、実装テクニックについては、書籍や他のソースコードをたくさん読むことにより効果的に学ぶことが出来るので、是非ともチャレンジして欲しい。


### 演習問題

#### 1. 裸の原子炉における中性子束分布 (零中性子束境界条件)

完成した計算コードで求めた中性子束分布をプロットさせてみよう。中性子束分布は、Container オブジェクトにおける get_flux_dist メソッドで下記のように取得できるようにしたい。


```Python
flux_dist = calc_man.controller.container.get_flux_dist()
```

戻り値として、下記のような2次元リストを返すように設定すること。

~~~
[[0.5,
  1.5,
  ...
  98.5,
  99.5],
 [0.012688756616239107,
  0.038053732231784085,
  ...
  0.03806177262712973,
  0.012691395758198915]]
  ~~~

下記のコードを用いて、得られた中性子束を Jupyter Notebook で可視化してみよう。

```Python
%matplotlib notebook
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(flux_dist[0], flux_dist[1])
plt.show()
```

#### 2. 反射体付き原子炉における実効増倍率と中性子束分布

厚さ60cmの燃料の両端に厚さ30cmの軽水反射体が配置されている1次元平板原子炉を考えて、その実効増倍率と中性子束分布を可視化してみよう。なお、断面積は下記のものを用いること。

```Python
xs_fuel = CrossSection([1.36, 0.0181, 0.0279])
xs_ref  = CrossSection([0.55, 0.0127, 0.0])
```

## 2群計算への拡張

前節では1群計算を対象としていたが、これを2群計算に拡張してみよう。以下に1群計算と2群計算の違いをまとめる。

+ 断面積について
    - エネルギー群数が2倍 (引数kgの追加）
    - 核分裂スペクトルの取り扱い
    - 散乱マトリクスの取り扱い
+ 収束計算
    - エネルギー群による反復計算
    - 散乱中性子源の計算


これらの違いを意識しながら、下位層のクラスから少しずつ変更していこう。

### CrossSectionクラス

まずは、CrossSection クラスのテストコードを2群計算に対応すべく変更しよう。

定数設定のためのメソッドについては、第一引数としてエネルギー群を指定できるようにする。また、核分裂スペクトルの設定 (set_xi) も追加しよう。さらに、散乱マトリクス (scattering matrix) を設定するメソッド(set_smat) を追加しよう。また、設定した値を取得できる getter メソッドも必要だ。

以上を考慮して作成したテストコードが次のものだ。

##### test_cross_section.py
```Python
import unittest

import sys
sys.path.append('../lib')

from node import Node
from cross_section import CrossSection

class NodeTest(unittest.TestCase):

    def test_sets(self):
        xs = CrossSection()
        xs.set_d(0, 1.0)
        xs.set_siga(0, 2.0)
        xs.set_nusigf(0, 3.0)
        xs.set_xi(0, 1.0)
        xs.set_d(1, 11.0)
        xs.set_siga(1, 12.0)
        xs.set_nusigf(1, 13.0)
        xs.set_xi(1, 0.0)
        xs.set_smat([[1.0, 2.0],[3.0, 4.0]])
        #   sm(kg, kkg)
        # 
        #             kkg
        #           0     1
        #   kg 0   1.0   2.0
        #      1   3.0   4.0

        self.assertEqual(xs.dif(0), 1.0)
        self.assertEqual(xs.siga(0), 2.0)
        self.assertEqual(xs.nusigf(0), 3.0)
        self.assertEqual(xs.xi(0), 1.0)
        self.assertEqual(xs.dif(1), 11.0)
        self.assertEqual(xs.siga(1), 12.0)
        self.assertEqual(xs.nusigf(1), 13.0)
        self.assertEqual(xs.xi(1), 0.0)
        self.assertEqual(xs.sigs(0,0), 1.0)
        self.assertEqual(xs.sigs(0,1), 2.0)
        self.assertEqual(xs.sigs(1,0), 3.0)
        self.assertEqual(xs.sigs(1,1), 4.0)        

    def test_sets3(self):
        xs1 = CrossSection()
        xs1.set([[1.0, 2.0, 3.0, 1.0],[11.0, 12.0, 13.0, 0.0]])
        xs1.set_smat( [[1.0, 2.0], [3.0, 4.0]])
        xs1_ref = CrossSection()
        xs1_ref.set(xs1)
        self.assertEqual(xs1, xs1_ref)

    def test_operation_add(self):
        xs1 = CrossSection()
        xs1.set([[1.0, 2.0, 3.0, 1.0],[11.0, 12.0, 13.0, 0.0]])
        xs1.set_smat( [[1.0, 2.0], [3.0, 4.0]])

        xs2 = CrossSection()
        xs2.set([[1.0, 2.0, 3.0, 1.0],[11.0, 12.0, 13.0, 0.0]])
        xs2.set_smat( [[1.0, 2.0], [3.0, 4.0]])

        xs3 = xs1 + xs2

        xs3_ref = CrossSection()
        xs3_ref.set([[2.0, 4.0, 6.0, 2.0],[22.0, 24.0, 26.0, 0.0]])
        xs3_ref.set_smat( [[2.0, 4.0], [6.0, 8.0]])

        self.assertEqual(xs3, xs3_ref)

    def test_operation_sub(self):
        xs1 = CrossSection()
        xs1.set([[1.0, 2.0, 3.0, 1.0],[11.0, 12.0, 13.0, 0.0]])
        xs1.set_smat( [[1.0, 2.0], [3.0, 4.0]])

        xs2 = CrossSection()
        xs2.set([[2.0, 4.0, 6.0, 2.0],[22.0, 24.0, 26.0, 0.0]])
        xs2.set_smat( [[2.0, 4.0], [6.0, 8.0]])

        xs3 = xs2 - xs1

        xs3_ref = CrossSection()
        xs3_ref.set([[1.0, 2.0, 3.0, 1.0],[11.0, 12.0, 13.0, 0.0]])
        xs3_ref.set_smat( [[1.0, 2.0], [3.0, 4.0]])

        self.assertEqual(xs3, xs3_ref)

    def test_operation_mul(self):
        xs1 = CrossSection()
        xs1.set([[1.0, 2.0, 3.0, 1.0],[11.0, 12.0, 13.0, 0.0]])
        xs1.set_smat( [[1.0, 2.0], [3.0, 4.0]])

        xs2 = xs1 * 2.0

        xs2_ref = CrossSection()
        xs2_ref.set([[2.0, 4.0, 6.0, 2.0],[22.0, 24.0, 26.0, 0.0]])
        xs2_ref.set_smat( [[2.0, 4.0], [6.0, 8.0]])

        self.assertEqual(xs2, xs2_ref)

        xs3 = 2.0 * xs1
        xs3_ref = xs2_ref
        self.assertEqual(xs3, xs3_ref)

        xs4 = 2.0 * xs1 * 3.0
        xs4_ref = CrossSection()
        xs4_ref.set([[6.0, 12.0, 18.0, 6.0],[66.0, 72.0, 78.0, 0.0]])
        xs4_ref.set_smat( [[6.0, 12.0], [18.0, 24.0]])
        xs4.debug()
        xs4_ref.debug()

        self.assertEqual(xs4, xs4_ref)



if __name__ == '__main__':
    unittest.main()
```

そして、このテストコードが成功するように CrossSection クラスを実装していく。以下に例を示しておこう。


##### cross_section.py
```Python
import numpy as np
import copy

# 大域変数
N_REACT = 5  # D, Siga, nuSigf, Xi, sigr
DIF    = 0
SIGA   = 1
NUSIGF = 2
XI     = 3
SIGR   = 4

class CrossSection:
    """
    断面積クラス (2群)
    """

    def __init__(self, val=None, ng=2):
        """
        コンストラクタ
        """
        self.x  = np.zeros((ng, N_REACT))
        self.sm = np.zeros((ng, ng))
        if not (val is None):
            self.set(val)

    def set(self, val):
        if type(val) == CrossSection:
            self.x = copy.copy(val.x)
            self.sm = copy.copy(val.sm)
        else: # リストの場合
            for kg in range(self.ng()):
                for i in range(len(val[kg])):
                    self.x[kg, i] = val[kg][i]

    def set_d(self, kg, val):
        self.x[kg, DIF] = val

    def set_siga(self, kg, val):
        self.x[kg, SIGA] = val

    def set_nusigf(self, kg, val):
        self.x[kg, NUSIGF] = val

    def set_xi(self, kg, val):
        self.x[kg, XI] = val

    def set_smat(self, mat):
        for kg in range(self.ng()):
            for i in range(self.ng()):
                self.sm[kg, i] = mat[kg][i]

    def calc_sigr(self):
        for kg in range(self.ng()):
            self.x[kg, SIGR] = self.x[kg, SIGA]
            for kkg in range(self.ng()):
                if kg != kkg:
                    self.x[kg, SIGR] += self.sm[kg,kkg]

    def ng(self):
        return self.x.shape[0]

    def dif(self, kg):
        return self.x[kg, DIF]

    def siga(self, kg):
        return self.x[kg, SIGA]

    def sigr(self, kg):
        return self.x[kg, SIGR]

    def nusigf(self, kg):
        return self.x[kg, NUSIGF]

    def xi(self, kg):
        return self.x[kg, XI]

    def sigs(self, kg, kkg):
        return self.sm[kg, kkg]

    def __eq__(self, other):
        return np.allclose(self.x, other.x) and np.allclose(self.sm, other.sm)

    def __mul__(self, factor):
        # ここで val は float であることを前提とする
        xs = CrossSection(self)
        xs.x *= factor
        xs.sm *= factor
        return xs

    def __rmul__(self, factor):
        xs = CrossSection(self)
        xs.x *= factor
        xs.sm *= factor
        return xs

    def __truediv__(self, factor):
        xs = CrossSection(self)
        xs.x *= (1.0/factor)
        xs.sm *= (1.0/factor)
        return xs

    def __neg__(self):
        return self * (-1.0)

    def __add__(self, other):
        xs = CrossSection(self)
        xs.x += other.x
        xs.sm += other.sm
        return xs

    def __sub__(self, other):
        xs = CrossSection(self) + (-other)
        return xs

    def debug(self):
        print("-" * 9 + " XS " + "-" * 29)
        print("kg\tD\tSiga\tSigr\tNuSigf\tXi")
        for kg in range(self.x.shape[0]):
            print(kg, self.x[kg, DIF], self.x[kg, SIGA], self.x[kg, SIGR], self.x[kg, NUSIGF], self.x[kg, XI], sep='\t', end='\n')
        print( "smat")
        print( self.sm )
        print("-"*42)
```

### Nodeクラス

次に Node クラス周りをみていこう。例のごとく、テストコードから。

2群計算になって大きく変わるところは、エネルギーループが必要なことと、散乱ソースの取り扱いだ。

問題を可能な限りシンプルにするために、最初のテストではノードの数を一つとした。これは、2群計算の導入による違いを主としてテストすることができるからだ。このように、「違いをもたらす違い (The difference makes the difference)」に集中した「最小問題セット (the minimum problem set)」のテストを書いて、そのテストを通すように本体を実装していくのが重要だ。初期のテストが通った段階で、必要に応じてテストの数を増やしていけば良い。


少し長くなるが、このような方法で作成したテストコードとクラス実装のの例を以下に示しておく。

##### test_node.py

```Python
import unittest

import sys
sys.path.append('../lib')
import math

from config import *
from cross_section import CrossSection
from node import Node

class NodeTest(unittest.TestCase):

    def test_onenode(self):
        node = Node()
        xs = CrossSection()

        # two-group problem
        xs.set([[1.58, 0.0032, 0.0, 1.0],[0.271, 0.0930, 0.168, 0.0]])
        xs.set_smat( [[0.0, 0.0178], [0.0, 0.0]])
        xs.calc_sigr()

        #xs.debug()
        node.set_xs(xs)

        keff = 1.0
        keff_old = 1.0
        total_fis_src_old = 1.0
        conv = 1.0e-10

        # outer iteration
        for ik in range(1000):

            # normalize total fission source
            total_fis_src = 0.0
            for kg in range(2):
                total_fis_src += node.get_fis_src(kg) * node.get_width()
            factor = 1.0 / (total_fis_src/keff)

            for kg in range(2):
                node.normalize_fis_src(kg, factor)

            # energy loop
            for kg in range(2):
                # update sources
                node.calc_scat_src(kg)

                # inner loop
                for i in range(4):
                    for dir in range(2):
                        node.set_jin(kg, dir, node.get_jout(kg, dir))

                    # calculate jout, flux with response matrix
                    node.calc(kg)

                node.calc_fis_src(kg)

            # calc total fission source and k_eff
            total_fis_src = 0.0
            for kg in range(2):
                total_fis_src += node.get_fis_src(kg) * node.get_width()

            keff = total_fis_src / (total_fis_src_old/keff_old)
            diff = abs((keff - keff_old)/keff)

            # convergence check
            if(diff < conv):
                break

            # update parameters
            total_fis_src_old = total_fis_src
            keff_old = keff
            node.set_keff(keff)

        # --- end of loop for outer iteration

        print("keff=", keff)

        kana_nume = xs.sigr(1)*xs.nusigf(0) + xs.sigs(0,1)*xs.nusigf(1)
        kana_deno = xs.sigr(0) * xs.sigr(1)
        kana = kana_nume / kana_deno
        print("kana=", kana)

        self.assertAlmostEqual(keff, kana, places=5)

        for kg in range(2):
            self.assertAlmostEqual(node.get_jout(kg, XM), node.get_jout(kg, XP), places=5)
            self.assertAlmostEqual(node.get_jin(kg, XM), node.get_jout(kg, XM), places=5)
            self.assertAlmostEqual(node.get_jin(kg, XP), node.get_jout(kg, XP), places=5)
            self.assertAlmostEqual(node.get_jout(kg, XM)+node.get_jin(kg, XM), node.get_flux(kg) / 2.0, places=5)


    def test_uniform_zeroflux_bc(self):
        xs = CrossSection()
        xs.set([[1.58, 0.02, 0.0, 1.0],[0.271, 0.0930, 0.168, 0.0]])
        xs.set_smat( [[0.0, 0.0178], [0.0, 0.0]])
        xs.calc_sigr()

        delta = 1.0
        geom = [{'xs':xs, 'width':100}]

        # geometry setting
        nodes = []        
        for r in geom:
            for k in range(int(r['width']/delta)):
                the_node = Node(r['xs'])
                the_node.set_width(delta)
                nodes.append(the_node)

        keff = 1.0
        keff_old = 1.0
        total_fis_src_old = 1.0
        conv = 1.0e-8

        # outer iteration
        for ik in range(100):

            # normalize total fission source
            total_fis_src = 0.0
            for the_node in nodes:
                for kg in range(2):
                    total_fis_src += the_node.get_fis_src(kg) * the_node.get_width()
            factor = 1.0 / (total_fis_src/keff)

            for the_node in nodes:
                for kg in range(2):
                    the_node.normalize_fis_src(kg, factor)

            # energy loop
            for kg in range(2):

                # update scattering source
                for the_node in nodes:
                    the_node.calc_scat_src(kg)

                # inner loop
                for i in range(4):
                    for istart in range(2):  # start color (0: red, 1:black)
                        for ix in range(istart, len(nodes), 2):

                            # pass partial currents to adjacent nodes
                            if(ix==0):
                                jin_xm = -nodes[ix].get_jout(kg, XM)
                            else:
                                jin_xm = nodes[ix-1].get_jout(kg, XP)

                            if(ix==len(nodes)-1):
                                jin_xp = -nodes[ix].get_jout(kg, XP)
                            else:
                                jin_xp = nodes[ix+1].get_jout(kg, XM)

                            nodes[ix].set_jin(kg, XM, jin_xm)
                            nodes[ix].set_jin(kg, XP, jin_xp)

                            # calculate jout, flux with response matrix
                            nodes[ix].calc(kg)

                # update fission source
                for the_node in nodes:
                    the_node.calc_fis_src(kg)

            # calc total fission source and keff
            total_fis_src = 0.0
            for the_node in nodes:
                for kg in range(2):
                    total_fis_src += the_node.get_fis_src(kg) * the_node.get_width()   

            keff = total_fis_src / (total_fis_src_old/keff_old)
            diff = abs((keff - keff_old)/keff)
            # print( keff, diff)

            # convergence check
            if(diff < conv):
                break

            # update parameters
            total_fis_src_old = total_fis_src
            keff_old = keff
            for the_node in nodes:
                the_node.set_keff(keff)

        # --- end of loop for outer iterations

        # converged
        print("keff=", keff)

        # debug
        #print("fast flux")
        #for ix in range(len(nodes)):
        #    print(ix, nodes[ix].get_flux(0))

        b2 = (math.pi / geom[0]['width'])**2

        kana_nume = (xs.sigr(1) + xs.dif(1)*b2)*xs.nusigf(0) + xs.sigs(0,1)*xs.nusigf(1)
        kana_deno = (xs.dif(0)*b2 + xs.sigr(0) ) * (xs.dif(1)*b2 + xs.sigr(1))
        kana = kana_nume / kana_deno
        print("kana=", kana)

        self.assertAlmostEqual(keff, kana, places=4)



    def test_two_regions_zeroflux_bc(self):

        xs_fuel = CrossSection()
        xs_fuel.set([[1.58, 0.0032, 0.0, 1.0],[0.271, 0.0930, 0.168, 0.0]])
        xs_fuel.set_smat( [[0.0, 0.0178], [0.0, 0.0]])
        xs_fuel.calc_sigr()

        xs_ref = CrossSection()
        xs_ref.set([[1.41, 0.0, 0.0, 1.0],[0.117, 0.0191, 0.0, 0.0]])
        xs_ref.set_smat( [[0.0, 0.0476], [0.0, 0.0]])
        xs_ref.calc_sigr()

        delta = 1.0
        geom = [{'xs':xs_ref, 'width':30}, {'xs':xs_fuel, 'width':60}, {'xs':xs_ref, 'width':30} ]

        # geometry setting
        nodes = []        
        for r in geom:
            for k in range(int(r['width']/delta)):
                the_node = Node(r['xs'])
                the_node.set_width(delta)
                nodes.append(the_node)

        keff = 1.0
        keff_old = 1.0
        total_fis_src_old = 1.0
        conv = 1.0e-8

        # outer iteration
        for ik in range(100):

            # normalize total fission source
            total_fis_src = 0.0
            for the_node in nodes:
                for kg in range(2):
                    total_fis_src += the_node.get_fis_src(kg) * the_node.get_width()
            factor = 1.0 / (total_fis_src/keff)

            for the_node in nodes:
                for kg in range(2):
                    the_node.normalize_fis_src(kg, factor)       

            # energy loop
            for kg in range(2):

                # update scattering source
                for the_node in nodes:
                    the_node.calc_scat_src(kg)

                # inner loop
                for i in range(4):
                    for istart in range(2):  # start color (0: red, 1:black)
                        for ix in range(istart, len(nodes), 2):

                            # pass partial currents to adjacent nodes
                            if(ix==0):
                                jin_xm = -nodes[ix].get_jout(kg, XM)
                            else:
                                jin_xm = nodes[ix-1].get_jout(kg, XP)

                            if(ix==len(nodes)-1):
                                jin_xp = -nodes[ix].get_jout(kg, XP)
                            else:
                                jin_xp = nodes[ix+1].get_jout(kg, XM)

                            nodes[ix].set_jin(kg, XM, jin_xm)
                            nodes[ix].set_jin(kg, XP, jin_xp)

                            # calculate jout, flux with response matrix
                            nodes[ix].calc(kg)

                # update fission source
                for the_node in nodes:
                    the_node.calc_fis_src(kg)

            # calc total fission source and keff
            total_fis_src = 0.0
            for the_node in nodes:
                for kg in range(2):
                    total_fis_src += the_node.get_fis_src(kg) * the_node.get_width()  

            keff = total_fis_src / (total_fis_src_old/keff_old)
            diff = abs((keff - keff_old)/keff)

            # print( keff, diff)
            # convergence check
            if(diff < conv):
                break

            # update parameters
            total_fis_src_old = total_fis_src
            keff_old = keff
            for the_node in nodes:
                the_node.set_keff(keff)

        # --- end of loop for outer iterations

        # converged
        print("keff=", keff)
  
        #print("flux")
        #for ix in range(len(nodes)):
        #   print(ix, nodes[ix].get_flux())

        self.assertAlmostEqual(keff, 1.35826, places=5)  # keff with strict condition

if __name__ == '__main__':
    unittest.main()
```

##### node.py

```Python
import numpy as np

from cross_section import *
from config import *

class Node:
    def __init__(self, xs=None, kg=2):
        self.jout = np.ones((kg,2))   # kg, out-going, [XM, XP]
        self.jin  = np.ones((kg,2))   # kg, in-coming, [XM, XP]
        self.flux  = np.ones(kg)      # average flux
        self.width = 1.0
        self.xs = None
        self.keff = 1.0
        self.fis_src = np.ones(kg)
        self.scat_src = np.zeros(kg)
        if(xs):
            self.set_xs(xs)

    def set_xs(self, val):
        self.xs = val

    def set_keff(self, val):
        self.keff = val

    def set_width(self, val):
        self.width = val

    def set_flux(self, kg, val):
        self.flux[kg] = val

    def get_flux(self, kg):
        return self.flux[kg]

    def set_jin(self, kg, dir, val):
        self.jin[kg, dir] = val

    def get_jin(self, kg, dir):
        return self.jin[kg, dir]

    def get_jout(self, kg, dir):
        return self.jout[kg, dir]

    def get_xs(self):
        return self.xs

    def get_width(self):
        return self.width

    def get_fis_src(self, kg):
        return self.fis_src[kg]

    def calc_fis_src(self, kg):
        # fission source        
        s_fis = 0.0
        for kkg in range(self.xs.ng()):
            s_fis += self.xs.xi(kg) * self.xs.nusigf(kkg)*self.flux[kkg]
        self.fis_src[kg] = s_fis

    def calc_scat_src(self, kg):
        # scattering source
        s_scat = 0.0
        for kkg in range(self.xs.ng()):
            if kg != kkg:
                s_scat += self.xs.sigs(kkg, kg) * self.flux[kkg]
        self.scat_src[kg] = s_scat

    def normalize_fis_src(self, kg, factor):
        self.fis_src[kg] *= factor

    def calc(self, kg):
        #flux by Eq(28)
        coef1 = 2.0*self.xs.dif(kg) / self.width
        coef2 = 2.0*coef1
        coef3 = 1.0 + coef2
        f_nume = coef1 * 4.0 * (self.jin[kg, XP] + self.jin[kg, XM]) + coef3 * \
                (self.fis_src[kg]  / self.keff + self.scat_src[kg]) * self.width
        f_deno = coef2 + coef3*self.xs.sigr(kg)*self.width
        self.flux[kg] = f_nume / f_deno

        #net current by Eq(29)
        jnet_XM  = -coef1 * (4.0*self.jin[kg, XM] - self.flux[kg]) / coef3
        jnet_XP = -coef1 * (4.0*self.jin[kg, XP] - self.flux[kg]) / coef3

        #out-goinnt by Eq(30)
        self.jout[kg, XM] = jnet_XM + self.jin[kg, XM]
        self.jout[kg, XP] = jnet_XP + self.jin[kg, XP]


    def debug(self):
        print("-"*3 + " Node " + "-"*40)
        print( "kg\tjin_XM\tjin_XP\tjout_XM\tjout_XP")
        for kg in range(self.xs.ng()):
            print(kg, self.jin[kg, XM], self.jin[kg, XP], self.jout[kg, XM], self.jout[kg, XP], sep='\t')

        print("  flux   \t", self.flux)
        print("  fis_src\t", self.fis_src)
        print("  scat_src\t", self.scat_src)
        print("  keff   \t", self.keff)

        self.xs.debug()
        print("-"*50)
```

### Containerクラス

Container クラスは内部反復を担当するとした。すなわち、calc メソッドの引数にはエネルギー群である kg を渡して、エネルギー反復を Container クラスの外側で設定する。2群化することで、散乱中性子源の計算部分も追加している。以下に、Container クラスのテストコードにそのロジックの例を示す。

##### test_container.py
```Python
import unittest

import sys
sys.path.append('../lib')
import math

from config import *
from cross_section import CrossSection
from node import Node
from container import Container

class ContainerTest(unittest.TestCase):

    def test_container(self):

        xs = CrossSection()
        xs.set([[1.58, 0.02, 0.0, 1.0],[0.271, 0.0930, 0.168, 0.0]])
        xs.set_smat( [[0.0, 0.0178], [0.0, 0.0]])
        xs.calc_sigr()

        delta = 1.0
        albedo = -1.0
        geom = [{'xs':xs, 'width':100}]

        cont = Container(geom, delta, albedo)
        #cont.debug()

        keff = 1.0
        keff_old = 1.0
        total_fis_src_old = 1.0
        conv = 1.0e-7

        for idx_outer in range(100):

            total_fis_src = cont.get_total_fis_src()
            norm_factor = 1.0 / (total_fis_src/keff)
            cont.normalize_fis_src(norm_factor)

            for kg in range(2):
                cont.calc_scat_src(kg)

                for idx_inner in range(4):
                    for color in range(2):
                        cont.calc(kg, color)

                cont.calc_fis_src(kg)

            total_fis_src = cont.get_total_fis_src()

            keff = total_fis_src / (total_fis_src_old/keff_old)
            diff = abs((keff - keff_old)/keff)
            #print( keff, diff)
            if(diff < conv):
                break
            keff_old = keff
            total_fis_src_old = total_fis_src

            cont.set_keff(keff)

        b2 = (math.pi / geom[0]['width'])**2
        kana_nume = (xs.sigr(1) + xs.dif(1)*b2)*xs.nusigf(0) + xs.sigs(0,1)*xs.nusigf(1)
        kana_deno = (xs.dif(0)*b2 + xs.sigr(0) ) * (xs.dif(1)*b2 + xs.sigr(1))
        kana = kana_nume / kana_deno
        print("kana=", kana)

        self.assertAlmostEqual(keff, kana, places=4)


        flux = cont.get_flux_dist(0)  # first energy
        self.assertEqual(len(flux), 2)  # x, y
        self.assertEqual(len(flux[0]), int(geom[0]['width']/delta))
        self.assertEqual(flux[0][0], delta/2.0)
        self.assertEqual(flux[0][-1], geom[0]['width']-delta/2.0)
        self.assertEqual(len(flux[1]), int(geom[0]['width']/delta))


if __name__ == '__main__':
    unittest.main()
```

毎度のことだが、このテストが通るように Container クラスを実装していく。


##### container.py
```Python
import numpy as np

from node import *
from cross_section import *


class Container:
    def __init__(self, geometry, delta=1.0, albedo=0.0):
        self._setup(geometry, delta, albedo)

    def _setup(self, geometry, delta, albedo):
        self.nodes = []
        for r in geometry:
            for k in range(int(r['width']/delta)):
                the_node = Node(r['xs'])
                the_node.set_width(delta)
                self.nodes.append(the_node)

        self.delta = delta
        self.albedo = albedo
        self.ng = self.nodes[0].get_xs().ng()

    def get_ng(self):
        return self.ng


    def calc(self, kg, color=None):
        for ix in range(color, len(self.nodes), 2):
            if(ix==0):
                jin_xm = self.albedo * self.nodes[ix].get_jout(kg, XM)
            else:
                jin_xm = self.nodes[ix-1].get_jout(kg, XP)

            if(ix==len(self.nodes)-1):
                jin_xp = self.albedo * self.nodes[ix].get_jout(kg, XP)
            else:
                jin_xp = self.nodes[ix+1].get_jout(kg, XM)

            self.nodes[ix].set_jin(kg, XM, jin_xm)
            self.nodes[ix].set_jin(kg, XP, jin_xp)
            self.nodes[ix].calc(kg)

    def calc_fis_src(self, kg):
        for the_node in self.nodes:
            the_node.calc_fis_src(kg)

    def calc_scat_src(self, kg):
        for the_node in self.nodes:
            the_node.calc_scat_src(kg)

    def get_total_fis_src(self):
        total_fis_src = 0.0
        for kg in range(self.ng):
            for the_node in self.nodes:
                total_fis_src += the_node.get_fis_src(kg) * the_node.get_width()
        return total_fis_src

    def normalize_fis_src(self, factor):
        for kg in range(self.ng):
            for the_node in self.nodes:
                the_node.normalize_fis_src(kg, factor)

    def set_keff(self, keff):
        for the_node in self.nodes:
            the_node.set_keff(keff)

    def get_flux_dist(self, kg):
        x_pos = []
        x_sum = 0.0
        flux = []
        for the_node in self.nodes:
            w = the_node.get_width()
            x_pos.append( x_sum + w/2 )
            x_sum += w
            flux.append( the_node.get_flux(kg) )
        return [x_pos, flux]


    def debug(self):
        print("nodes: ", len(self.nodes))
        for the_node in self.nodes:
            the_node.debug()
```


### ContainerController クラス

ContainerController のレベルになれば、テストコードで準備する断面積や解析解の計算式以外に、1群計算と2群計算の間で実質的な差異はない。

##### test_container_controller.py
```Python
import unittest

import sys
sys.path.append('../lib')
import math


from config import *
from cross_section import CrossSection
from node import Node
from container import Container
from container_controller import ContainerController


class ContainerContainerTest(unittest.TestCase):

    def test_container_controller(self):
        xs = CrossSection()
        xs.set([[1.58, 0.02, 0.0, 1.0],[0.271, 0.0930, 0.168, 0.0]])
        xs.set_smat( [[0.0, 0.0178], [0.0, 0.0]])
        xs.calc_sigr()

        delta = 1.0
        albedo = -1.0
        geom = [{'xs':xs, 'width':100}]

        container = Container(geom, delta, albedo)
        #cont.debug()

        controller = ContainerController(container)

        count, flag = controller.calc()
        print("outer iterations: ", count)

        keff = controller.get_keff()

        b2 = (math.pi / geom[0]['width'])**2
        kana_nume = (xs.sigr(1) + xs.dif(1)*b2)*xs.nusigf(0) + xs.sigs(0,1)*xs.nusigf(1)
        kana_deno = (xs.dif(0)*b2 + xs.sigr(0) ) * (xs.dif(1)*b2 + xs.sigr(1))
        kana = kana_nume / kana_deno
        print("kana=", kana)

        self.assertAlmostEqual(keff, kana, places=4)


if __name__ == '__main__':
    unittest.main()
```

ContainerController の実装については、Containerクラスのテストコードでの修正がそのまま取り込まれた形となっている。すなわち、エネルギーループの追加と、散乱ソースの計算部分の追加が行われている。

##### container_controller.py
```Python
class ContainerController:
    """
    Container オブジェクトを操作し、外側反復計算を行う。
    """

    def __init__(self, container=None):
        self.cont = container
        self.keff = 1.0
        self.keff_old = 1.0
        self.total_fis_src_old = 1.0
        self.conv_criterion = 1.0E-7
        self.max_outer_iterations = 500
        self.inner_iterations = 4
        self.converged = False

    def calc(self):
        for idx_outer in range(self.max_outer_iterations):

            self.total_fis_src = self.cont.get_total_fis_src()
            norm_factor = 1.0 / (self.total_fis_src/self.keff)
            self.cont.normalize_fis_src(norm_factor)

            for kg in range(self.cont.get_ng()):
                self.cont.calc_scat_src(kg)

                for idx_inner in range(self.inner_iterations):
                    for color in range(2):
                        self.cont.calc(kg, color)

                    self.cont.calc_fis_src(kg)

                if self.cont.is_asymptotic(kg):
                    self.cont.accel_flux(kg)
                self.cont.save_old_flux(kg)

            self.total_fis_src = self.cont.get_total_fis_src()

            self.keff = self.total_fis_src / (self.total_fis_src_old/self.keff_old)
            diff = abs((self.keff - self.keff_old)/self.keff)

            #print(self.keff, diff)

            if(diff < self.conv_criterion):
                self.converged = True
                break

            self.keff_old = self.keff
            self.total_fis_src_old = self.total_fis_src

            self.cont.set_keff(self.keff)

        return (idx_outer, self.converged)

    def get_keff(self):
        return self.keff
```

### CalculationManager

CalculationManager についても殆ど差異はないが、参考のため、テストコードと本体の実装例を示しておく。

##### test_calculation_manager.y
```Python
import unittest

import sys
sys.path.append('../lib')
import math

from config import *
from cross_section import CrossSection
from node import Node
from container import Container
from container_controller import ContainerController
from calculation_manager import CalculationManager

class CalculationManagerTest(unittest.TestCase):

    def test_calculation_manager(self):

        xs = CrossSection()
        xs.set([[1.58, 0.02, 0.0, 1.0],[0.271, 0.0930, 0.168, 0.0]])
        xs.set_smat( [[0.0, 0.0178], [0.0, 0.0]])
        xs.calc_sigr()

        delta = 1.0
        albedo = -1.0
        geom = [{'xs':xs, 'width':100}]

        config = { 'geometry':geom, 'mesh_width':delta, "albedo": albedo}
                
        calc_man = CalculationManager(config)
        count, flag = calc_man.run()

        keff = calc_man.get_keff()

        b2 = (math.pi / geom[0]['width'])**2
        kana_nume = (xs.sigr(1) + xs.dif(1)*b2)*xs.nusigf(0) + xs.sigs(0,1)*xs.nusigf(1)
        kana_deno = (xs.dif(0)*b2 + xs.sigr(0) ) * (xs.dif(1)*b2 + xs.sigr(1))
        kana = kana_nume / kana_deno
        print("kana=", kana)

        self.assertAlmostEqual(keff, kana, places=4)



if __name__ == '__main__':
    unittest.main()

```

##### calculation_manager.py

```Python
from container import Container
from container_controller import ContainerController

class CalculationManager:
    """
        計算の全体制御
    """
    def __init__(self, param):
        geom = param['geometry']
        delta = param['mesh_width']
        albedo = param['albedo']

        container = Container(geom, delta, albedo)
        self.controller = ContainerController(container)

    def run(self):
        return self.controller.calc()

    def get_keff(self):
        return self.controller.get_keff()

```


## 加速法の実装

さて、2群計算コードが出来たわけだが、まだまだプロトタイプの段階にすぎず、実用にはほど遠い。というのも、計算アルゴリズムが単純な Red/Black法とべき乗法 (Power Method）を組み合わせたものだからだ。これは何を意味するのか？　いろんな計算を試してみると分かるのだが、計算が非常に「重い」のである。

1次元体系での2群計算ならそれほどでも無いが、3次元の詳細メッシュ体系で多群計算をしようものなら目も当てられない程に、収束がとても遅いのである。だからこそこれまでに、いろんな加速法が考案され、実用化されてきたのだ。（詳しくは、多田講師による講義を参照）

本講義では、時間の制約<font size=1>と講師のエネルギー不足</font>の問題から、最も簡単な加速法の一つである　Successive Over Relaxation法（以下、SOR法）を取りあげて、外側反復における中性子束の外挿への適用を試みる。

### SOR法の実装方針

ｎ回目の外部反復の中性子束 $\phi^n_{g,i}$ を n-1 回目の外部反復の中性子束 $\phi^{n-1}_{g,i}$ を用いて次式により外挿する。

$$\phi'^n_{g,i} = \phi^n_{g,i} + \omega ( \phi^n_{g,i} - \phi^{n-1}_{g,i})$$


この実現に必要な基本的な処理は

- 外側反復において、前回の中性子束を保存しておく
- 今回の中性子束を求める際に、上式により中性子束を外挿する

の二つだけである。前回の中性子束を保存する場所は、Node クラスが妥当であろう。個々のノードに対して save_flux_old メソッドを追加し、外側反復のエネルギーループの最後の処理として Container クラスを通じて呼び出せば良いので、それほど難しくはなさそうだ。

### 実装例

今回は、最もトップレベルの CalculationManager のテストコードから考えてみる。加速係数 $\omega$ を指定する必要があるので、CalculationManager のコンストラクタに与える config にその情報を含めた。asymptotic_criteria は収束が漸近状態に入っているかを判定するためのパラメータとして追加している。

##### test_calculation_manager.py
```Python
import unittest

import sys
sys.path.append('../lib')
import math

from config import *
from cross_section import CrossSection
from node import Node
from container import Container
from container_controller import ContainerController
from calculation_manager import CalculationManager

class CalculationManagerTest(unittest.TestCase):

    def test_calculation_manager(self):

        xs_fuel = CrossSection()
        xs_fuel.set([[1.58, 0.0032, 0.0, 1.0],[0.271, 0.0930, 0.168, 0.0]])
        xs_fuel.set_smat( [[0.0, 0.0178], [0.0, 0.0]])
        xs_fuel.calc_sigr()
        
        xs_ref = CrossSection()
        xs_ref.set([[1.41, 0.0, 0.0, 1.0],[0.117, 0.0191, 0.0, 0.0]])
        xs_ref.set_smat( [[0.0, 0.0476], [0.0, 0.0]])
        xs_ref.calc_sigr()
    
        geom = [{'xs':xs_ref, 'width':30}, {'xs':xs_fuel, 'width':60}, {'xs':xs_ref, 'width':30} ]
        
        delta = 1.0
        albedo = -1.0

        config = { 'geometry':geom, 'mesh_width':delta, 'albedo': albedo, 'max_iteration': 1000, \
                    'omega': 0.5, 'asymptotic_criteria': 0.05}
                
        calc_man = CalculationManager(config)
        count, flag = calc_man.run()
        print( "outer iterations:", count)

        keff = calc_man.get_keff()


        self.assertAlmostEqual(keff, 1.35826, places=5)  # keff with strict condition



if __name__ == '__main__':
    unittest.main()
```

このテストコードを成功させるために、CalculationManager, ContainerController, Container, Node をそれぞれ拡張していく。

以下に、各クラスの全体もしくは拡張部分の例を示す。

##### calculation_manager.py
```Python
from container import Container
from container_controller import ContainerController


class CalculationManager:

    def __init__(self, param):
        geom = param['geometry']
        delta = param['mesh_width']
        albedo = param['albedo']
        omega = param['omega']
        asym_cri = param['asymptotic_criteria']

        container = Container(geom, delta, albedo)
        container.set_omega(omega, asym_cri)
        
        self.controller = ContainerController(container)

    def run(self):
        return self.controller.calc()

    def get_keff(self):
        return self.controller.get_keff()

```

##### container_controller.py
```Python
class ContainerController:
    """
    Container オブジェクトを操作し、外側反復計算を行う。
    """

    def __init__(self, container=None):
        self.cont = container
        self.keff = 1.0
        self.keff_old = 1.0
        self.total_fis_src_old = 1.0
        self.conv_criterion = 1.0E-7
        self.max_outer_iterations = 500
        self.inner_iterations = 4
        self.converged = False

    def calc(self):
        for idx_outer in range(self.max_outer_iterations):
            
            self.total_fis_src = self.cont.get_total_fis_src()
            norm_factor = 1.0 / (self.total_fis_src/self.keff)
            self.cont.normalize_fis_src(norm_factor)

            for kg in range(self.cont.get_ng()):
                self.cont.calc_scat_src(kg)

                for idx_inner in range(self.inner_iterations):
                    for color in range(2):
                        self.cont.calc(kg, color)
                    
                    self.cont.calc_fis_src(kg)

                if self.cont.is_asymptotic(kg):
                    self.cont.accel_flux(kg)
                self.cont.save_old_flux(kg)

            self.total_fis_src = self.cont.get_total_fis_src()

            self.keff = self.total_fis_src / (self.total_fis_src_old/self.keff_old)
            diff = abs((self.keff - self.keff_old)/self.keff)

            #print(self.keff, diff)

            if(diff < self.conv_criterion):
                self.converged = True
                break

            self.keff_old = self.keff
            self.total_fis_src_old = self.total_fis_src

            self.cont.set_keff(self.keff)
        
        return (idx_outer, self.converged)

    def get_keff(self):
        return self.keff

```

##### container.py
```Python
import numpy as np

from node import *
from cross_section import *


class Container:
    def __init__(self, geometry, delta=1.0, albedo=0.0):
        self._setup(geometry, delta, albedo)

    def _setup(self, geometry, delta, albedo):
        self.nodes = []
        for r in geometry:
            for k in range(int(r['width']/delta)):
                the_node = Node(r['xs'])
                the_node.set_width(delta)
                self.nodes.append(the_node)

        self.delta = delta
        self.albedo = albedo
        self.ng = self.nodes[0].get_xs().ng()
        self.change_ratio_old = 1.0
        self.max_diff_old = 1.0
        self.asymptotic_criteria = 0.0

    (中略)

    def accel_flux(self, kg):
        for the_node in self.nodes:
            the_node.accel_flux(kg)

    def save_old_flux(self, kg):
        for the_node in self.nodes:
            the_node.save_old_flux(kg)

    def set_omega(self, omega, asym_criteria=0.05):
        self.asymptotic_criteria = asym_criteria
        for the_node in self.nodes:
            the_node.set_omega(omega)

    def is_asymptotic(self, kg):
        diff = np.zeros(len(self.nodes))
        for i in range(len(self.nodes)):
            diff[i] = self.nodes[i].get_flux_diff(kg)
        max_diff = max(diff)

        change_ratio = max_diff / self.max_diff_old
        if change_ratio / self.change_ratio_old < self.asymptotic_criteria:
            flag = True
        else:
            flag = False
        
        self.change_ratio_old = change_ratio
        self.max_diff_old = max_diff

        return flag
```

##### node.py
```Python
import numpy as np

from cross_section import *
from config import *

class Node:
    def __init__(self, xs=None, kg=2):
        self.jout = np.ones((kg,2))   # kg, out-going, [XM, XP]
        self.jin  = np.ones((kg,2))   # kg, in-coming, [XM, XP]
        self.flux  = np.ones(kg)      # average flux
        self.old_flux = np.ones(kg)
        self.omega = 0.5
        self.width = 1.0
        self.xs = None
        self.keff = 1.0
        self.fis_src = np.ones(kg)
        self.scat_src = np.zeros(kg)
        if(xs):
            self.set_xs(xs)

    （中略）

    # SOR acceleration 
    def save_old_flux(self, kg):
        self.old_flux[kg] = self.flux[kg]

    def accel_flux(self, kg):
        self.flux[kg] = self.flux[kg] + self.omega * (self.flux[kg] - self.old_flux[kg])
    
    def set_omega(self, omega):
        self.omega = omega

    def get_flux_diff(self, kg):
        return (self.flux[kg] - self.old_flux[kg])/self.old_flux[kg]

```



### 演習問題

1. 最も効率が良い加速因子 $\omega$ と、その時の収束回数を求めよ

2. メッシュ幅を変化させたとき、収束状況がどのように変化するかを考察せよ。

