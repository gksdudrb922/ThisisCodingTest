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

n,m=map(int,input().split())
data=[]
for _ in range(n):
  data.append(list(map(int,input().split())))


def bfs(start_x,start_y):
  q=deque([(start_x,start_y)])
  visited[start_x][start_y]=True

  while q:
    x,y=q.popleft()

    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if 0<=nx<n and 0<=ny<m and data[nx][ny]==0 and visited[nx][ny]==False:
        q.append((nx,ny))
        visited[nx][ny]=True

dx=[-1,1,0,0]
dy=[0,0,-1,1]
visited=[[False]*m for _ in range(n)]
result=0
for i in range(n):
  for j in range(m):
    if data[i][j]==0 and not visited[i][j]:
      bfs(i,j)
      result+=1
print(result)
#O(n2m2)