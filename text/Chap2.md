# Part 2: 炉物理プログラミング (実践・スキル編)

では、いよいよ本題のテーマである炉物理プログラミングを始めてみる。

いきなり実践に入る前に、少しだけ準備運動をしておこう。

事前課題において Python言語の基礎的な知識は習得しているはずだが、少しだけおさらいしておく。

## Python言語について

Python言語は、いま最も注目されているスクリプト言語の一つだと言って良いだろう。特に、最近は機械学習・深層学習がとても注目されているが、その関連でも Pythonは非常によく使われている。

また、欧米の高等教育現場において Python の利用率は非常に高い。少し前は MATLAB がメジャーだったが、今は完全に Python が追い越したと言っても良いだろう。このように、Python は教育現場や実プロジェクトで多く用いられているため、是非とも使いこなせるようになっておきたい。

プログラミングのエッセンスはプログラミング言語に依存しない。また、プログラミング言語は互いに影響をうけあいながら発展している。したがって、一つのプログラミング言語をマスターしておけば、他の言語の習得は比較的容易に行える。このことからも、まだ本格的にプログラミングを学習していなのであれば、Python を最初に学習することをお薦めする。


### 必須文法・構文

Python の文法は非常にシンプルだ。また、構文（スコープ）がインデントにより決定されるという点が特徴で、この部分は賛否両論があるのだが、なれてしまえばそれほど気にはならない。インデントと上手く付き合うためには、「Python モード」があるエディタを活用する方が良いだろう。

#### 変数・演算

これといって特徴はない。普通に使える。ただし、インクリメント・デクリメント演算子(++, --) は存在しないので C++使いの人は要注意。

```Python
hoge = 10
page = hoge * 2.0
page += hoge
```

#### リスト・辞書・タプル

Pythonでは、配列は リスト (list)で、ハッシュは辞書(dic) という型で実現している。タプル(Tuple)はPython独自の型で、変更不可能なリストと理解すれば良い。リストはブラケット(bracket)、辞書はブレース({})、タプルは括弧(())にて表記する。リストやタプルについては、一部を切り出す「スライシング (slicing)」が可能である。

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

if文の最後のコロン(:)を忘れないようにすること。また、if文の条件部分には括弧は不要である。（括弧をつけても文法上問題はないが、使わないのがPython流）　なお、「後置if」はないのが Rubyist には残念だが、Python のポリシーから考えると仕方がない。

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

Python におけるクラスの定義は、他の言語とよく似ており、特に難しいところは無いだろう。メソッドの定義において、第一引数がselfとなる点に注意。なお、コンストラクタメソッドは \_\_init\_\_ である。

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

### Step0: 全体構想を練る


### Step1: 基本的なオブジェクトの設計と実装


### Step2: テストコードを準備する


### Step3: CrossSectionクラスの拡張


### Step4: Nodeクラスの拡張



### Step5: Contaierクラスの新設


### Step6: ContainerControllerクラスの新設


### Step7: CalculationManagerクラスの新設


### Final: 完成


## 2群計算への拡張


