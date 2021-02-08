## 개미 전사
"""
// problem
메뚜기 마을의 여러 개의 식량창고에는 정해진 수의 식량을 저장하고 있다.
최소한 한 칸 이상 떨어진 식량창고를 약탈하면서 최대한 많은 식량을 얻어야 한다.
// input
정수 N (3 ~ 100)
각 식량창고에 저장된 식량의 개수 K (0 ~ 1,000)
// output
얻을 수 있는 식량의 최댓값
"""
# my code
n = int(input())

data = list(map(int, input().split()))
data.insert(0, 0)

d = [0] * 101
d[1] = data[1]
d[2] = data[2]

for i in range(3, n + 1):
    for k in range(i - 2, 0, -1):
        d[i] = max(d[i], d[k] + data[i])

print(max(d[n], d[n - 1]))
# O(n2)