## 블록 이동하기
"""
// problem
로봇은 2 x 1 크기의 로봇으로 무지는 0과 1로 이루어진 N x N 크기의 지도에서 2 x 1 크기인 로봇을 움직여
(N, N) 위치까지 이동 할 수 있도록 프로그래밍을 하려고 한다.
로봇이 이동하는 지도는 가장 왼쪽, 상단의 좌표를 (1, 1)로 하며 지도 내에 표시된 숫자 0은 빈칸을 1은 벽을 나타낸다.
로봇은 벽이 있는 칸 또는 지도 밖으로는 이동할 수 없다.
로봇은 처음에 아래 그림과 같이 좌표 (1, 1) 위치에서 가로방향으로 놓여있는 상태로 시작하며,
앞뒤 구분없이 움직일 수 있다.
로봇은 상하좌우, 90도회전이 가능하다.
// input
N*N의 board
// output
최소 몇 초 만에 (n,n)에 도착하는지 출력한다.
"""
# my code
from collections import deque

def movable(x1, y1, x2, y2, n, board):
    if 0 <= x1 < n and 0 <= y1 < n and 0 <= x2 < n and 0 <= y2 < n:
        if board[x1][y1] == 0 and board[x2][y2] == 0:
            return True
    return False

def solution(board):
    n = len(board)
    visited = {(0, 0, 0, 1)}
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(0, 0, 0, 1, 0)])

    while q:
        x1, y1, x2, y2, count = q.popleft()

        if (x1 == n - 1 and y1 == n - 1) or (x2 == n - 1 and y2 == n - 1):
            return count

        # 이동
        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]

            if movable(nx1, ny1, nx2, ny2, n, board):
                if (nx1, ny1, nx2, ny2) not in visited:
                    q.append((nx1, ny1, nx2, ny2, count + 1))
                    visited.add((nx1, ny1, nx2, ny2))

        # 회전
        if x1 == x2:  # 가로
            nx = x1 - 1
            if nx >= 0 and board[nx][y1] == 0 and board[nx][y2] == 0:
                if (nx, y1, x1, y1) not in visited:
                    q.append((nx, y1, x1, y1, count + 1))
                    visited.add((nx, y1, x1, y1))
                if (nx, y2, x2, y2) not in visited:
                    q.append((nx, y2, x2, y2, count + 1))
                    visited.add((nx, y2, x2, y2))

            nx = x1 + 1
            if nx < n and board[nx][y1] == 0 and board[nx][y2] == 0:
                if (x1, y1, nx, y1) not in visited:
                    q.append((x1, y1, nx, y1, count + 1))
                    visited.add((x1, y1, nx, y1))
                if (x2, y2, nx, y2) not in visited:
                    q.append((x2, y2, nx, y2, count + 1))
                    visited.add((x2, y2, nx, y2))

        else:  # 세로
            ny = y1 - 1
            if ny >= 0 and board[x1][ny] == 0 and board[x2][ny] == 0:
                if (x1, ny, x1, y1) not in visited:
                    q.append((x1, ny, x1, y1, count + 1))
                    visited.add((x1, ny, x1, y1))
                if (x2, ny, x2, y2) not in visited:
                    q.append((x2, ny, x2, y2, count + 1))
                    visited.add((x2, ny, x2, y2))

            ny = y1 + 1
            if ny < n and board[x1][ny] == 0 and board[x2][ny] == 0:
                if (x1, y1, x1, ny) not in visited:
                    q.append((x1, y1, x1, ny, count + 1))
                    visited.add((x1, y1, x1, ny))
                if (x2, y2, x2, ny) not in visited:
                    q.append((x2, y2, x2, ny, count + 1))
                    visited.add((x2, y2, x2, ny))
    return 0
