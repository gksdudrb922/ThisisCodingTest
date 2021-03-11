## 팀 결성
"""
// problem
0번부터 N번까지의 학생에 대해 '팀 합치기' 연산과 '같은 팀 여부 확인' 연산을 사용할 수 있다.
1. '팀 합치기' 연산은 두 팀을 합치는 연산이다.
2. '같은 팀 여부 확인' 연산은 특정한 두 학생이 같은 팀에 속하는지를 확인하는 연산이다.
M개의 연산을 수행할 수 있을 때, '같은 팀 여부 확인' 연산에 대한 연산 결과를 출력하라.
// input
첫째 줄 -> N, M (1 ~ 100,000)
M개 줄 -> 각각의 연산
'팀 합치기' 연산은 0 a b 형태로 a 학생과 b 학생이 속한 팀을 합친다.
'같은 팀 여부 확인' 연산은 1 a b 형태로 a 학생과 b 학생이 같은 팀에 속해 있는지를 확인한다.
(a와 b는 N 이하의 양의 정수이다)
// output
'같은 팀 여부 확인' 연산에 대하여 한 줄에 하나씩 YES 혹은 NO로 결과를 출력한다.
"""
# my code
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    op,a,b=map(int,input().split())
    if op==0:
      union_parent(parent,a,b)
    else:
      if find_parent(parent,a)==find_parent(parent,b):
        print('YES')
      else:
        print('NO')

# O(n+mlogn)