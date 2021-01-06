## 게임 개발
"""
// problem
N*M 크기의 맵에서 다음 조건에 따라 캐릭터가 움직인다.
1. 현재 위치에서 현재 방향을 기준으로 왼족 방향부터 차례대로 갈 곳을 정한다.
2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 못한 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽 한 칸을 전진한다.
왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
// input
입력 예시
4 4         # N * M (3 ~ 50)
1 1 0       # 초기 위치 (x,y) 방향은 0
1 1 1 1     # N * M 맵 생성
1 0 0 1
1 1 0 1
1 1 1 1
// output
이동을 마친 후 캐릭터가 방문한 칸의 수
"""
# my code
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
result = 1
left_count = 0
data[x][y]=2

n, m = map(int, input().split())
x, y, direction = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
result = 1
left_count = 0
data[x][y] = 2
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

while True:

    nx = x + dx[direction]
    ny = y + dy[direction]
    if data[nx][ny] == 0:
        x = nx
        y = ny
        data[x][y] = 2
        result += 1
        left_count = 0
    else:
        left_count += 1
    direction -= 1
    if direction == -1:
        direction = 3

    if left_count == 4:
        nx = x + dx[direction - 1]
        ny = y + dy[direction - 1]
        if data[nx][ny] == 1:
            break
        else:
            x = nx
            y = ny
            left_count = 0
print(result)
# O(NM), N,M이 50 이하이기 때문에 사실상 O(1)