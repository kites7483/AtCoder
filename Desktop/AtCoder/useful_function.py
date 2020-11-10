#使えそうな関数の一覧

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