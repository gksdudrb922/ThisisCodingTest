## 큰 수의 법칙
"""
// problem
N개의 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만들어야 한다.
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
// input
첫째 줄 -> N(2 ~ 1,000), M(1 ~ 10,000), K(1 ~ 10,000) (K <= M)
둘째 줄 -> N개의 자연수 (1 ~ 10,000)
// output
큰 수의 법첵이 따라 더해진 답
"""
# my code
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

result = 0
first = data[-1]
second = data[-2]
for i in range(m):
    if (i + 1) % (k + 1) != 0:
        result += first
    else:
        result += second

print(result)
# O(nlogn + m)
