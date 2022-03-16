from collections import deque


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (n + 1)


def bfs(v):
    queue = deque([(v, 0)])
    visited[v] = True

    while queue:
        v, distance = queue.popleft()
        if distance == k:
            result.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append((i, distance + 1))
                visited[i] = True


result = []
bfs(x)

if len(result) == 0:
    print(-1)
else:
    result.sort()
    for x in result:
        print(x)
