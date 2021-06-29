#使えそうな関数の一覧(随時更新)

#----------------------------
#組み合わせの総数を素数で割った余りを高速で算出する(https://qiita.com/derodero24/items/91b6468e66923a87f39f)
#----------------------------

def comb(n,r,mod):
  if (r < 0 or r > n):
    return 0
  r = min(r,n-r)
  return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 2*10**5 #nの最大値
g1 = [1,1] #元テーブル
g2 = [1,1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range(2,N+1):
  g1.append(( g1[-1] * i ) % mod) #(インデックス番号)!のmod
  inverse.append(( -inverse[mod % i] * (mod//i) ) % mod)
  g2.append((g2[-1] * inverse[-1]) % mod)

#----------------------------
#グループの合体及び同じグループに所属しているかの判定を行う（Union-Find）（https://juppy.hatenablog.com/entry/2018/11/08/蟻本_python_Union-Find木_競技プログラミング）
#----------------------------

#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]

n,m = map(int,input().split())
#初期化
#根なら-size,子なら親の頂点
par = [-1]*n

#----------------------------
#高速素因数分解 (https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8）
#----------------------------

#n >= 2
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

factorization(24) #[[2,3],[3,1]]

#----------------------------
#いもす法（https://imoz.jp/algorithms/imos_method.html）
'''
区間の更新が繰り返し行われ，最後にまとめて値を出したいときに使う
'''
#----------------------------

data = [[0,4,5],[2,6,3],[7,9,2],[3,6,1]]
line = [0 for i in range(10)]
for datum in data:
  a,b,c = datum[0],datum[1],datum[2]
  line[a] += c #区間の入り口で加算
  line[b] -= c #区間の出口で減算

#累積和
for i in range(n):
  line[i+1] += line[i]

print(line) #[5, 5, 8, 9, 4, 4, 0, 2, 2, 0]

'''
|5|5|5|5| | | | | | |
| | |3|3|3|3| | | | |
| | | | | | | |2|2| |
| | | |1|1|1| | | | |
          ↓
|5|5|8|9|4|4|0|2|2|0|
'''

#一つずつリストに値を加算していく場合 → 最悪の場合 O(データ数 × 区間の長さ)
#いもす法 → O(データ数 + 区間の長さ) に削減できる！！

#----------------------------
#BFS（幅優先探索） (https://note.com/melon_ms_mtcc/n/nd2c0c7c16edb）
#----------------------------

from collections import deque

def bfs(n,m,edge_list,start):#(ノード数，リンク数，辺のリスト，始点)
    graph = [[] for _ in range(n+1)]

    for edge in edge_list:
      a, b = edge[0],edge[1]
      graph[a].append(b)
      graph[b].append(a)

    dist = [-1] * (n+1)
    dist[0] = 0
    dist[start] = 0

    d = deque()
    d.append(start)

    while d:
      v = d.popleft()
      for i in graph[v]:
        if dist[i] != -1:
          continue
        dist[i] = dist[v] + 1
        d.append(i)

    return dist[1:]

#イメージ（始点が（1,1）の場合）
'''

. . . . .　 　0 1 2 3 4
. * * . .　→　1 * * 4 5       始点から各点までの
. . * . *　→　2 3 * 5 *　　　　最短距離を算出できる！
* . . . .　 　* 4 5 6 7

'''
