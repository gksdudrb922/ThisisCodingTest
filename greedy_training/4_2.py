## 만들 수 없는 금액
"""
// problem
N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구한다.
// input
첫째 줄 -> N : 동전의 개수 (1 ~ 1,000)
둘째 줄 -> 동전의 화페 단위, N 개의 자연수 (1,000,000 이하)
// output
주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값
"""
# study
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)
# O(nlogn)
"""
// learn
my code와 동일한 풀이다.
다만, 여기서는 target을 my code의 sum+1로 잡았다.
"""