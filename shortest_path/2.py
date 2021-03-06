## 전보
"""
// problem
N개의 도시와 M개의 통로에 대해 방향, 비용 그래프로 이루어져 있는 마을이 있다.
C라는 도시에서 최대한 많은 도시로 메시지를 보내고자 한다.
// input
첫째 줄 -> 도시의 개수 N (1 ~ 30,000), 통로의 개수 (1 ~ 200,000), 메시지를 보내고자 하는 도시 C
둘째 줄 ~ M+1째 줄 -> X,Y,Z (특정 도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있고, 메시지가 전달되는 시간이 Z이다.)
(1 <= X, Y <= N, 1 <= Z <= 1,000)
// output
도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간
"""
# my code
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수, 시작 노드 번호를 입력받기
n, m, c = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(c)

count=0
result=0
for i in range(1, n + 1):
  if distance[i]!=INF and distance[i]!=0:
    count+=1
    result=max(result,distance[i])

print(count,result)
# O(MlogN)