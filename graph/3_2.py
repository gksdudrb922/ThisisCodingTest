## 커리큘럼
"""
// problem
N개의 강의를 듣고자 한다. 이 때, 선수 강의가 있는 강의는 선수 강의를 먼저 들어야만 해당 강의를 들을 수 있다.
동시에 여러 강의를 들을 수 있다고 할 때 N개의 강의에 대하여 수강하기 까지 걸리는 최소 시간을 각각 구하라.
// input
첫째 줄 -> N (1 ~ 500)
N개 줄 -> 각 강의의 강의 시간(1 ~ 100,000)과 선수 강의들의 번호가 주어진다.
각 강의 번호는 1부터 N까지로 구성되며, 각 줄은 -1로 끝난다.
// output
N개의 강의에 대하여 수강하기까지 걸리는 최소 시간
"""
# study
from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v + 1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in range(1, v + 1):
        print(result[i])

topology_sort()
# O(n2)
"""
// learn
my code는 indegree가 0이 되어 queue에 들어갈 때 total_time[i] = total_time[now] + lecture_time[i]으로 시간을 계산한다.
그러나 indegree를 0으로 만드는 now보다 0으로 만들지 않는 now의 total_time이 더 크다면 정확한 시간을 계산할 수 없다.
study code에서는 result[i] = max(result[i], result[now] + time[i])으로 시간을 계산한다.
현재 수업의 총 시간과, 현재 수업의 선수과정의 총 시간 + 현재 수업의 시간을 비교해서 큰 값으로 총 수업 시간을 계산한다.
my code는 잘못된 코드다. study code로 푸는 것이 맞다.
"""