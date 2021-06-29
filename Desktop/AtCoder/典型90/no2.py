'''
point：小さい制約は全探索

(cf) bit演算・bit全探索

○bit演算
x<<n：全体をnビット左シフト　ex) 5<<3 → 101000(2) → 40(10)
x>>n：全体をnビット右シフト　ex) 10>>2 → 10(2) → 2(10) ※最下位より先に押し出されたビットは消去　1010→10.10→10

○bit全探索
iを0~2^n-1でforループし，iの2進数表記における0と1をそれぞれ問題のシチュエーションに合わせて対応させる．
（本題であれば '(' と ')'）
'''

#本題（Encyclopedia of Parentheses）
#計算量（n*2^n）

n = int(input())
for i in range(1<<n):
  letters = ''
  for j in reversed(range(n)):
    #(i & (1 << j)) == 0： i の j ビット目（2^j の位）が 0 であるための条件
    if (i & (1 << j)) == 0:
      letters += '('
    else:
      letters += ')'

  dep = 0
  flag = True
  for s in letters:
    if s == '(':
      dep += 1
    if s == ')':
      dep -= 1
    if dep < 0:
      flag = False
      break
  if flag and (dep == 0):
    print(letters)