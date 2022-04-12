## 감시 피하기
"""
// problem
NxN 크기의 복도가 있다. 복도는 1x1 크기의 칸으로 나누어지며,
특정한 위치에는 선생님, 학생, 혹은 장애물이 위치할 수 있다.
각 선생님들은 자신의 위치에서 상, 하, 좌, 우 4가지 방향으로 감시를 진행한다.
단, 복도에 장애물이 위치한 경우, 선생님은 장애물 뒤편에 숨어 있는 학생들은 볼 수 없다.
또한 선생님은 상, 하, 좌, 우 4가지 방향에 대하여,
아무리 멀리 있더라도 장애물로 막히기 전까지의 학생들은 모두 볼 수 있다고 가정하자.
// input
첫째 줄에 자연수 N이 주어진다. (3 ≤ N ≤ 6) 둘째 줄에 N개의 줄에 걸쳐서 복도의 정보가 주어진다.
각 행에서는 N개의 원소가 공백을 기준으로 구분되어 주어진다.
해당 위치에 학생이 있다면 S, 선생님이 있다면 T, 아무것도 존재하지 않는다면 X가 주어진다.
단, 전체 선생님의 수는 5이하의 자연수, 전체 학생의 수는 30이하의 자연수이며
항상 빈 칸의 개수는 3개 이상으로 주어진다.
// output
첫째 줄에 정확히 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지의 여부를 출력한다.
모든 학생들을 감시로부터 피하도록 할 수 있다면 "YES", 그렇지 않다면 "NO"를 출력한다.
"""
# my code
n = int(input())
data = []
teachers = []
for x in range(n):
    data.append(input().split())
    for y in range(n):
        if data[x][y] == "T":
            teachers.append((x, y))

result = "NO"
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(count):
    global result
    if count == 3:
        for teacher in teachers:
            for direction in range(4):
                nx, ny = teacher
                while True:
                    nx += dx[direction]
                    ny += dy[direction]
                    if 0 <= nx < n and 0 <= ny < n:
                        if data[nx][ny] == "O":
                            break
                        elif data[nx][ny] == "S":
                            return
                    else:
                        break
        result = "YES"
    else:
        for i in range(n):
            for j in range(n):
                if data[i][j] == "X":
                    data[i][j] = "O"
                    count += 1
                    dfs(count)
                    data[i][j] = "X"
                    count -= 1


dfs(0)
print(result)

# O(nC3*n2)
