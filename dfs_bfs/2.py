## 미로 탈출
"""
// problem
N*M 크기의 미로가 있다. 초기 위치(1,1)에서 (N,M)까지의 최소 이동 칸의 개수를 구하라
// input
첫 번째 줄 -> 세로 길이 N, 가로 길이 M(4 ~ 200)
두 번째 줄부터 N+1번째 줄까지 미로의 정보가 주어진다. (괴물 있는 부분 : 0, 괴물 없는 부분 : 1)
// output
목적지까지 최소 이동 칸의 개수
"""
# my code
from collections import deque


def bfs(x, y):
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1:
                q.append((nx, ny))
                data[nx][ny] = data[x][y] + 1

    return data[n - 1][m - 1]


n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

print(bfs(0, 0))

# O(nm)
