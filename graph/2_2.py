## 도시 분할 계획
"""
// problem
N개의 집과 M개의 길로 이루어진 마을이 있다. 각 길마다 길을 유지하는데 드는 유지비가 있다.
마을을 2개의 분리된 마을로 분할할 계획을 세우고 있다. 각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다.
또한 분리된 두 마을 사이에 있는 길들을 없애고 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 없앨 수 있다.
위 조건을 만족하도록 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하고 싶다.
// input
첫째 줄 -> N (2 ~ 100,000), M (1 ~ 1,000,000)
M개 줄 -> A,B,C : A와 B를 연결하는 길의 유지비가 C (1 ~ 1,000)
// output
길을 없애고 남은 유지비 합의 최솟값
"""
# study
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

# 노드의 개수와 간선(Union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()
last = 0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)
# O(mlogm) -> PyPy3로만 통과
"""
// learn
my code와 동일한 풀이다.
다만, 가장 마지막에 집합에 포함된 경로가 최소 신장 트리에서 비용이 가장 크기 때문에
계속 max_value를 비교하는 my code와 달리 study code에서는 집합에 포함되는 경로마다 last값을 부여해 주었다.
"""