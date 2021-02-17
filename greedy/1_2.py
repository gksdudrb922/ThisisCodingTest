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
# study

# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort()  # 입력 받은 수들 정렬하기
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

print(result)  # 최종 답안 출력
# O(nlogn)
"""
// learn
first * k + second를 하나의 수열로 보고 count 값을 계산했다.
"""