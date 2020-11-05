#使えそうなライブラリをまとめる（随時更新）

#--------------------------------------
#Collections
import collections
#--------------------------------------

#Counter：各要素の出現回数をカウント (返り値はCounterオブジェクト，サブクラスはdict型)
cnt1 = collections.Counter('112')
cnt2 = collections.Counter(['a','a','b','c'])
print(cnt1) #Counter({'1': 2, '2': 1})
print(cnt2) #Counter({'a': 2, 'b': 1, 'c':1})

#使用例：ある文字列orリストに特定の文字が入っているか判別する
if cnt1 - collections.Counter('1112') == collections.Counter():
    print('Yes')
else:
    print('No')

#--------------------------------------
#bisect
import bisect
#--------------------------------------

#bisect：ソート済みのリストに順序を崩さぬよう要素を追加するとき，何番目に入れれば良いか返す．
numbers = [1,3,4,6,8,10,12]
index = bisect.bisect(numbers,5)
print(index) # 3


