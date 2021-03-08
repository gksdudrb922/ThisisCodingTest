## 정확한 순위
"""
// problem
시험을 본 N명의 성적을 서로 비교한 결과가 있다.
A반 학생의 성적이 B반 학생보다 낮다면 화살표가 A에서 B를 가리키도록 할 때,
성적 순위를 정확히 알 수 있는 학생은 모두 몇 명인지 계산하라.
// input
첫째 줄 -> 학생들의 수 N (2 ~ 500), 성적 비교 횟수 M (2 ~ 10,000)
M개 줄 -> 두 학생의 성적 비교 결과 A, B (A번 학생의 성적이 B번 학생보다 낮다는 것을 의미한다)
// output
성적 순위를 정확히 알 수 있는 학생이 몇 명인지 출력한다.
"""
# my code
INF=int(1e9)

n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b]=0

for _ in range(m):
  a,b=map(int,input().split())
  graph[a][b]=1

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

result=0
for k in range(1,n+1):
  count=0
  for b in range(1,n+1):
    if 0<graph[k][b]<INF:
      count+=1
  for a in range(1,n+1):
    if 0<graph[a][k]<INF:
      count+=1
  if count==n-1:
    result+=1

print(result)
# O(n3)