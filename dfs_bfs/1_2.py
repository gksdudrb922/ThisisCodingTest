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
# study
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))


# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    # 해당 노드 방문 처리
    graph[x][y] = 1
    # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False


# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    # 현재 위치에서 DFS 수행
    if dfs(i, j) == True:
      result += 1

print(result)  # 정답 출력
# O(n2m2)
"""
// learn
파이썬 함수 내부에서 외부 변수 사용가능. 단, 변경은 불가능
study code에서는 dfs를 사용했고 my code와 로직이 살짝 다르다.
visited 여부를 0or1로 표현했고 not visited이면(graph[x][y]==1) 상하좌우 모두 dfs 호출을 한다.

복잡도 : n, m의 범위가 1000인데 my code, study code 모두 1초 안에 처리가 힘들지 않을까 싶다.
"""