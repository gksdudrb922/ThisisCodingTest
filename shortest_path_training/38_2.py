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
# study
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
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
    # A에서 B로 가는 비용을 1로 설정
    a, b = map(int, input().split())
    graph[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1
print(result)
# O(n3)
"""
// learn
my code와 동일한 풀이다.
다만, study code에서는 마지막 count 계산을 이중 loop로 더 효율적이게 작성했다.
"""