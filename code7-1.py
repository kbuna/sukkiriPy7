


#7.2 組み込み関数 7.3 標準ライブラリ 7.5 外部ライブラリ

#7-1
text = input("何を記録しますか? >>")
#file = open("diary.txt","a",encoding="UTF-8")
file = open("diary.txt","r",encoding="UTF-8")
# aはappend　追記モード
#file.write(text + "\n")
#t=file.read()
t2=file.readline()
#print(t)
print(t2)
file.close()
"""
open(ファイル名,モード)
ファイル名に開くファイルを指定する
モードにはどのようにファイルを操作するか指定する
r:読み込み(指定したファイルが存在しない場合はエラー)
w:書き込み(指定したファイルが存在しない場合は新規作成)
a:追記(指定したファイルが存在しない場合は新規作成)

新規textは、vsコードで開くフォルダの直下に作られる。

ファイルオブジェクト.write(書き込む内容)
/nで書き込むたびに改行されるように


"""


#7-2
text = input("今日は何をした? >>")
with open("diary.txt","a",encoding="UTF-8")as file:
    file.write(f"{text}\n")
"""
ファイルを閉じるタイミングはpythonに任されているので
または、必ずしも閉じるかはわからないので
なるべく手動で管理するべき　→close関数

確実に閉じたい場合は
→with文、with文で、ファイルを開き、
withブロックで開いたファイルに関する操作を行います
withブロックが終了すると自動的にファイルを閉じてくれる

・with文
with ファイルを開く処理 as 変数:
    ファイルを操作する処理

・ストリーム
プログラムは通常、キーボード画面、ファイルなどとデータをやりとりして動作するが、
そのようなデータの流れをストリームという
大規模システムでは、さらにデータベースやネットワークなど外部資源とも
ストリームでつながることがあります
ストリームは不用意に開き続けると、リソースを使い果たしてシステムダウンするなど
問題が発生することがあります。開いたら閉じるべきものはwith文で確実に閉じよう


"""



"""
モジュールが属する２種類のライブラリ
標準ライブラリ　python公式
外部ライブラリ 個人や別の組織

標準ライブラリの主なモジュール
math 数学計算
random 乱数に関する
datetime 日付と時間に関する
email 電子メール
csv csvファイル
json jsonファイル
os os操作


"""
#7-3 mathモジュールを利用する
import math
print(f"円周率は{math.pi}です")
print(f"小数点以下を切り捨てれば{math.floor(math.pi)}")
print(f"小数点以下を切り上げれば{math.ceil(math.pi)}")

#7-4 math モジュールに別名をつけて利用する

import math as m
print(f"円周率は{m.pi}です")
print(f"小数点以下を切り捨てれば{m.floor(m.pi)}")
print(f"小数点以下を切り上げれば{m.ceil(m.pi)}")

#7-5 特定の関数や変数だけを利用する
from math import pi
from math import floor
print(f"円周率は{pi}")
print(f"小数点以下を切り下げれば{floor(pi)}です")

#7-6 関数名が重複すると
from math import log
def log(msg):
    print(f"{msg}を記録します")
log(10)
#モジュールからlog関数を取り込み、対数を求めるはずが、自作のlog関数が発動する

#7-7 特定の変数や関数だけを別名をつけて利用する
from math import pi as ensyuritsu
from math import floor as kirisute
print(f"円周率は{ensyuritsu}")
print(f"小数点以下を切り捨てば{kirisute(ensyuritsu)}です")


#7-8 ワイルドカードインポート
from math import *
print(f"円周率は{pi}")
print(f"小数点以下を切り捨てれば{floor(pi)}")
print(f"小数点以下を切り上げれば{ceil(pi)}")


"""
モジュール取り込みのまとめ

１　モジュールを取り込む
import モジュール名
２　モジュールに別名を付けて取り込む
import モジュール名 as 別名
３　特定の変数や関数だけを取り込む
from モジュール名 import 変数名または関数名
４　特定の変数や関数だけを別名をつけて取り込む
from モジュール名 import 変数名または関数名 as 別名 
５　ワイルドカードインポート(非推奨)
from モジュール名 import *

    取り込む範囲         取り込んだ変数の参照       取り込んだ関数の呼び出し
１  モジュール全体         モジュール名.変数名      モジュール名.関数名()
２  モジュール全体          別名.変数名             別名.変数名()
３  特定の変数または関数    変数名                  関数名()
４  特定の変数または関数    別名                    別名()
５  モジュール全体          変数名                  関数名()
"""



#7-9    httpパッケージのclientモジュールを取り込む
import http.client
conn = http.client.HTTPConnection('www.python.org')

#7-10   httpパッケージのclientモジュールを取り込む(from利用)
from http import client
conn = client.HTTPConnection('www.python.org')

#7-11   httpパッケージのclientモジュールから関数だけを取り込む
from http.client import HTTPConnection
conn = HTTPConnection('www.python.org')

"""
パッケージ内のモジュールの取り込み 変数参照 関数呼び出し
import パッケージ名.モジュール名
※asで別名を付けることも可能
パッケージ名.モジュール名.変数名
パッケージ名.モジュール名.関数名(引数,...)

パッケージ内のモジュールの取り込み 変数参照 関数呼び出し
(from利用)
from パッケージ名　import モジュール名
※asで別名を付けることも可能
モジュール名.変数名
モジュール名.関数名(引数,...)

パッケージ内のモジュールから特定の変数や関数だけを取り込む
from パッケージ名.モジュール名 import 変数名または関数名
※取り込んだ変数や関数はその名前だけで参照できる
※asで別名をつけることも


"""





