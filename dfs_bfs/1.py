## 음료수 얼려 먹기
"""
// problem
N*M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분끼리 상하좌우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
// input
첫 번째 줄 -> 세로 길이 N, 가로 길이 M(1 ~ 1000)
두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다. (구멍이 뚫려있는 부분 : 0, 그렇지 않은 부분 : 1)
// output
한 번에 만들 수 있는 아이스크림의 개수
"""
# my code
from collections import deque


def bfs(x, y):
    q = deque([(x, y)])
    graph[x][y] = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = 1


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            bfs(i, j)
            result += 1

print(result)


# O(nm)
