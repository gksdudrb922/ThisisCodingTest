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

def bfs(i,j):
  dx=[1,-1,0,0]
  dy=[0,0,-1,1]
  queue=deque([(i,j,1)])
  visited[i][j]=True
  while queue:
    (x,y,count)=queue.popleft()
    for k in range(4):
      nx=x+dx[k]
      ny=y+dy[k]
      if ((0<=nx<n) and (0<=ny<m)) and graph[nx][ny]==1 and not visited[nx][ny]:
        if nx==n-1 and ny==m-1:
          return count+1
        queue.append((nx,ny,count+1))
        visited[nx][ny]=True


n,m=map(int,input().split())
graph=[]
visited=[[False]*m for _ in range(n)]
for _ in range(n):
  graph.append(list(map(int,input())))
print(bfs(0,0))
# O(nm)
