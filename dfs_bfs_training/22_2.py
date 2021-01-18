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
# study, 풀지 못함
from collections import deque
def get_next_pos(pos,board):
  next_pos=[]
  pos=list(pos)
  pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # (상, 하, 좌, 우)로 이동하는 경우에 대해서 처리
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  for i in range(4):
    pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        # 이동하고자 하는 두 칸이 모두 비어 있다면
    if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
      next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
  if pos1_x==pos2_x:
    for i in [-1,1]:
      if board[pos1_x+i][pos1_y]==0 and board[pos2_x+i][pos2_y]==0:
        next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
        next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
  elif pos1_y==pos2_y:
    for i in [-1,1]:
      if board[pos1_x][pos1_y+i]==0 and board[pos2_x][pos2_y+i]==0:
        next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
        next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
  return next_pos


def solution(board):
  n=len(board)
  new_board=[[1]*(n+2) for _ in range(n+2)]
  for i in range(n):
    for j in range(n):
      new_board[i+1][j+1]=board[i][j]
  pos={(1,1),(1,2)}
  visited=[]
  q=deque()
  q.append((pos,0))
  visited.append(pos)
  while q:
    pos,cost=q.popleft()
    if (n,n) in pos:
      return cost
    for next_pos in get_next_pos(pos,new_board):
      if next_pos not in visited:
        q.append((next_pos,cost+1))
        visited.append(next_pos)
  return 0
# 약 O(n2)
"""
// learn
전형적인 bfs문제다. 그러나 로봇의 길이가 2이고, 회전도 고려해야한다. 기본적인 아이디어는 다음과 같다.
- 범위의 확장 : 매 탐색마다 범위를 체크하는 것도 괜찮지만, 범위를 확장시켜 사방을 벽으로 둘러싸 벽인지 아닌지만 고려하게끔 할 수 있다.
- 집합 사용 : 방문 여부를 확인하기 위해서 집합을 사용한다. 집합은 순서가 없기 때문에 두 점으로 이루어진 로봇의 방문 체크를 편리하게 할 수 있다.
- 회전 : 회전하는 방향의 모든 칸에 벽이 없어야 회전 가능하다는 것을 고려한다.
"""