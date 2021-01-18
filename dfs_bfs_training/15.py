## 특정 거리의 도시 찾기
"""
// problem
어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서,
최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오.
또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.
// input
첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다.
(2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N)
둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다.
이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ A, B ≤ N)
단, A와 B는 서로 다른 자연수이다.
// output
X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.
"""
# my code
import sys
from collections import deque

# BFS 메서드 정의
def bfs(graph,start,visited):
  result=[]
  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue=deque([(start,0)])
  # 현재 노드를 방문 처리
  visited[start]=True
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력
    (v,count)=queue.popleft()
    # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append((i,count+1))
        visited[i]=True
        if count+1==k:
          result.append(i)
  return result

input = sys.stdin.readline
n,m,k,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for _ in range(m):
  start,end=map(int,input().split())
  graph[start].append(end)
result=bfs(graph,x,visited)
if len(result)==0:
  print(-1)
else:
  result.sort()
  for i in result:
    print(i)
# O(N+M)