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
# my code
from collections import deque

v = int(input())

indegree = [0] * (v + 1)
lecture_time = [0] * (v + 1)
total_time = [0] * (v + 1)

graph = [[] for i in range(v + 1)]

for i in range(1, v + 1):
    data = list(map(int, input().split()))
    lecture_time[i] = data[0]
    for x in data[1:]:
        if x == -1:
            break
        graph[x].append(i)
        indegree[i] += 1


# 위상 정렬 함수
def topology_sort():
    q = deque()  # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
            total_time[i] = lecture_time[i]

    temp = 0
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
                total_time[i] = total_time[now] + lecture_time[i]

    for i in range(1, v + 1):
        print(total_time[i])

topology_sort()
# O(n2)