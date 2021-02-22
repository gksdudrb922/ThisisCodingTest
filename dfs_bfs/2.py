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
n,m=map(int,input().split())
data=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for _ in range(n):
  data.append(list(input()))

def bfs(x,y):
  q=deque([(x,y,1)])
  data[x][y]='0'
  while q:
    x,y,count=q.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<n and 0<=ny<m and data[nx][ny]=='1':
        if nx==n-1 and ny==m-1:
          return count+1
        q.append((nx,ny,count+1))
        data[nx][ny]='0'
  return 0

print(bfs(0,0))
# O(nm)