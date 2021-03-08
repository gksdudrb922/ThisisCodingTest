## 화성 탐사
"""
// problem
N*N 2차원 공간에서 각각의 칸을 지나기 위한 비용이 존재한다.
[0][0] 위치에서 [N-1][N-1] 위치로 이동하는 최소 비용을 구하라.
// input
첫째 줄 -> 테스트 케이스 T (1 ~ 10)
매 테스트 케이스의 첫재 줄에는 N (2 ~ 125)
이어서 N개의 줄에 걸쳐 각 칸의 비용이 주어진다. (0 <= 각 칸의 비용 <= 9)
// output
각 테스트 케이스마다 [0][0] 위치에서 [N-1][N-1] 위치로 이동하는 최소 비용을 출력
"""
# my code
import heapq

INF = int(1e9)
for tc in range(int(input())):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))

    graph = [[] for _ in range(n * n)]
    distance = [INF] * (n * n)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for x in range(n):
        for y in range(n):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    graph[x * n + y].append((nx * n + ny, data[nx][ny]))


    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))


    dijkstra(0)

    print(distance[n * n - 1] + data[0][0])
# O(n2logn)