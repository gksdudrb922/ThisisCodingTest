## 연구소
"""
// problem
N*M 연구소에서 빈칸, 벽, 바이러스가 있다. 바이러스는 상하좌우로 퍼진다.
벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다.
// input
첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)
둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다.
2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.
빈 칸의 개수는 3개 이상이다.
// output
안전 영역의 최대 크기를 출력한다.
"""
# my code
from itertools import combinations
from collections import deque
import copy

def bfs(x, y, data):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if data[nx][ny] == 1 or data[nx][ny] == 2:
                continue
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                queue.append((nx, ny))
    return data


n, m = map(int, input().split())
data = []
blank = []
virus = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
for _ in range(n):
    data.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            blank.append((i, j))
        elif data[i][j] == 2:
            virus.append((i, j))
walls = list(combinations(blank, 3))
for wall in walls:
    count = 0
    temp = copy.deepcopy(data)
    for x, y in wall:
        temp[x][y] = 1
    for x, y in virus:
        temp = bfs(x, y, temp)
    for row in temp:
        count += row.count(0)
    result = max(result, count)

print(result)
# O(NM C 3)