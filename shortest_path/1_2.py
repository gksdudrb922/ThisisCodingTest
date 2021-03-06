## 미래 도시
"""
// problem
N개의 회사와 M개의 도로로 이루어져 있는 도시가 있다.
도로로 이어져 있는 회사는 양방향 이동이 가능하고 시간은 1이 소요된다.
1번 도시에서 K번 회사를 거쳐서 X번 회사로 가는 최단 시간을 구한다.
// input
첫째 줄 -> 회사의 개수 N, 경로의 개수 M (1 <= N,M <= 100)
둘째 줄 ~ M+1째 줄 -> 연결된 두 회사의 번호
M+2째 줄 -> X, K (1 ~ 100)
// output
1번 도시에서 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간
만약 X번 회사에 도달할 수 없다면 -1을 출력한다.
"""
# study
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
x, meeting = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][meeting] + graph[meeting][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= 1e9:
    print("-1")
# 도달할 수 있다면, 최단 거리를 출력
else:
    print(distance)
# O(N3)
"""
// learn
my code와 동일한 풀이다.
다만, 교재에서는 알고리즘의 반복 변수 k와 input으로 받는 k를 동일하게 처리했는데 이를 다른 변수로 수정해주었다.
"""