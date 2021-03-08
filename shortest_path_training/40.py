## 숨바꼭질
"""
// problem
1 ~ N번까지의 헛간 중에서 하나를 골라 숨을 수 있으며, 술래는 항상 1번 헛간에서 출발한다.
전체 맵에는 총 M개의 양방향 통로가 존재하며, 전체 맵은 항상 어떤 헛간에서 다른 어떤 헛간으로 도달이 가능한 형태이다.
1번 헛간으로부터 최단 거리가 가장 먼 헛간이 가장 안전하다고 판단한다.
// input
첫째 줄 -> N (2 ~ 20,000), M (1 ~ 50,000)
이후 M개 줄 -> 서로 연결된 두 헛간 A, B (1 <= A,B <= N)
// output
숨어야 하는 헛간 번호(만약 거리가 같은 헛간이 여러 개면 가장 작은 헛간 번호)
그 헛간까지의 거리
그 헛간과 같은 거리를 갖는 헛간의 개수
"""
# my code
import heapq

INF=int(1e9)

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append((b,1))
  graph[b].append((a,1))

def dijkstra(start):
  q=[]
  heapq.heappush(q,(0,start))
  distance[start]=0
  while q:
    dist,now=heapq.heappop(q)
    if distance[now]<dist:
      continue
    for i in graph[now]:
      cost=dist+i[1]
      if distance[i[0]]>cost:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(1)

node=distance.index(max(distance[1:]))
print(node,distance[node],distance.count(distance[node]))
# O(mlogn)
