'''
point：木の直径を求める時は最短経路を2回求める
(cf) BFS（最短経路算出）（参考：https://note.com/melon_ms_mtcc/n/nd2c0c7c16edb）

from collections import deque

def bfs(graph,start): #(隣接リスト，始点)
  dist = [-1] * len(graph) #初期状態
  dist[0] = 0 #使わないけど一応
  dist[start] = 0 #始点と終点が一緒
  
  d = deque()
  d.append(start)

  while d:
    v = d.popleft()
    for i in graph[v]:
      if dist[i] != -1:
        continue
      dist[i] = dist[v] + 1
      d.append(i)

  return dist #始点から各ノードへの最短経路を算出（index0はダミー）
'''

#本題（Longest Circular Road）
#計算量（n）

from collections import deque

def bfs(graph,start):
  dist = [-1] * len(graph)
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

  return dist

n = int(input())

#隣接リスト作成
graph = [[] for _ in range(n+1)]

for i in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dist_list = bfs(graph,1) #頂点1からの最短経路
x = dist_list.index(max(dist_list)) #頂点1からの最短経路が最大となる頂点
ans = max(bfs(graph,x))+1 #bfs(graph,x)で木の直径
print(ans)