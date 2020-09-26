#Union Find
#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        tank = []
        while par[x] >= 0:
            tank.append(x)
            x = par[x]
        for elt in tank:
            par[elt] = x
        return x
        
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

n,m = map(int, input().split())
par = [-1] * n
for i in range(m):
  a,b = map(int,input().split())
  unite(a-1,b-1)

ans = set([])
for i in range(n):
  ans.add(find(i))
print(len(ans)-1)
