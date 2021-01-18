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
# study, 풀지 못함
from collections import deque

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0


def process(x, y, index):
    union[x][y] = index
    united = []
    united.append((x, y))
    queue = deque()
    queue.append((x, y))
    sum = graph[x][y]
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    union[nx][ny] = index
                    queue.append((nx, ny))
                    united.append((nx, ny))
                    sum += graph[nx][ny]
                    count += 1
    for x, y in united:
        graph[x][y] = int(sum / count)


while True:
    index = 0
    union = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    if index == n * n:
        break
    result += 1
print(result)
# 약 O(n4) -> PyPy3로만 통과
"""
// learn
처음에 한 bfs당 모든 나라의 그룹화를 하려다보니까 코드가 꼬여 실패했다.
한 bfs당 한 그룹씩 하는 방식이 더 보기 쉽고 작성하기도 쉽다.
"""