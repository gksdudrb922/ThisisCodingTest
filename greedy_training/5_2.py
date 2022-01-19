## 볼링공 고르기
"""
// problem
두 사람이 서로 무게가 다른 볼링공을 고르려고 한다.
// input
첫 째줄 -> 볼링공의 개수 N(1 ~ 1000), 공의 최대 무게 M(1 ~ 10)
둘 째줄 -> 각 볼링공의 무게 K (1 ~ M)
// output
두 사람이 볼링공을 고르는 경우의 수
"""
# study
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱해주기

print(result)
# O(n)
"""
// learn
각 무게별 개수를 배열에 저장하고 무게 1부터 m까지 무게별 개수와 남은 무게의 개수를 곱해서 result에 더한다.
"""