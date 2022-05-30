import sys


input = sys.stdin.readline
n, c = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()
start = 1
end = data[-1] - data[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    count = 1
    flag = data[0]
    for i in range(1, n):
        if data[i] - flag >= mid:
            count += 1
            flag = data[i]

    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
