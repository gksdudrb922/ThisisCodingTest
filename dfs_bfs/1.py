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
# study, 풀지 못함
def dfs(i,j):
  if not(0<=i<n) or not(0<=j<m):
    return
  if graph[i][j]==0:
    graph[i][j]=1
    dfs(i-1,j)
    dfs(i+1,j)
    dfs(i,j-1)
    dfs(i,j+1)
    return True
  return False

n,m=map(int,input().split())
graph=[]
for i in range(n):
  graph.append(list(map(int,input())))
result=0
for i in range(n):
  for j in range(m):
    if dfs(i,j)==True:
      result+=1
print(result)
# O(nm)
"""
// learn
구성요소를 구하는 알고리즘 학습
파이썬 함수 내부에서 외부 변수 사용가능. 단, 변경은 불가능
"""