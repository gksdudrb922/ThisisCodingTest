## 자물쇠와 열쇠
"""
// problem
자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있다.
열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조다.
자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만,
자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며
열쇠의 돌기와 자물쇠의 돌기가 만나서는 안된다.
또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있다.
// input
2차원 배열 : key[M][M], lock[N][N], (0<=M<=N<=20)
// output
key로 lock을 풀 수 있다면 True, 그렇지 않다면 False
"""
# my code
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

def match(lock,key,x,y):
  n=len(lock)//3
  m=len(key)
  false_flag=0
  for i in range(m):
    for j in range(m):
      lock[i+x][j+y]+=key[i][j]

  for i in range(n,2*n):
    for j in range(n,2*n):
      if lock[i][j]!=1:
        false_flag=1
  for i in range(m):
    for j in range(m):
      lock[i+x][j+y]-=key[i][j]
  if false_flag==1:
    return False
  else:
    return True

def solution(key,lock):
  n=len(lock)

  new_lock=[[1]*(3*n) for _ in range(3*n)]
  for i in range(n):
    for j in range(n):
      new_lock[i+n][j+n]=lock[i][j]

  for i in range(1,2*n):
    for j in range(1,2*n):
      for _ in range(4):
        key=rotate_a_matrix_by_90_degree(key)
        if match(new_lock,key,i,j):
          return True
  return False
# O(1)