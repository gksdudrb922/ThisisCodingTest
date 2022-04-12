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

n, m = map(int, input().split())
data = []
blanks = []
viruses = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(m):
        if data[i][j] == 0:
            blanks.append((i, j))
        elif data[i][j] == 2:
            viruses.append((i, j))

blanks_combi = list(combinations(blanks, 3))
temp = [[0] * m for _ in range(n)]
result = 0


def bfs(x, y, data):
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
                q.append((nx, ny))
                data[nx][ny] = 2


for blank_three in blanks_combi:
    for i in range(n):
        for j in range(m):
            temp[i][j] = data[i][j]

    for x, y in blank_three:
        temp[x][y] = 1

    for x, y in viruses:
        bfs(x, y, temp)

    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1

    result = max(result, count)

print(result)

# O(nmC3 * nm)
