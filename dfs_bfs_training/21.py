## 인구 이동
"""
// problem
N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며,
r행 c열에 있는 나라에는 A[r][c]명이 살고 있다.
국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루동안 연다.
위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
연합을 해체하고, 모든 국경선을 닫는다.
// input
첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)
둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다.
r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)
인구 이동이 발생하는 횟수가 2,000번 보다 작거나 같은 입력만 주어진다.
// output
인구 이동이 몇 번 발생하는지 첫째 줄에 출력한다.
"""
# my code
from collections import deque


n, l, r = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y, u):
    union[x][y] = u
    queue = deque([(x, y)])
    count = 1
    sum = a[x][y]

    while queue:
        x, y = queue.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == 0:
                if l <= abs(a[x][y] - a[nx][ny]) <= r:
                    union[nx][ny] = u
                    queue.append((nx, ny))
                    count += 1
                    sum += a[nx][ny]

    if count >= 2:
        union_record[u] = (count, sum)


result = 0
while True:
    u = 0
    union = [[0] * n for _ in range(n)]
    union_record = dict()

    for i in range(n):
        for j in range(n):
            if union[i][j] == 0:
                u += 1
                bfs(i, j, u)

    if len(union_record) == 0:
        break

    result += 1
    for i in range(n):
        for j in range(n):
            if union[i][j] in union_record:
                a[i][j] = int(union_record[union[i][j]][1] / union_record[union[i][j]][0])

print(result)

# 약 O(n4) -> PyPy3로만 통과
