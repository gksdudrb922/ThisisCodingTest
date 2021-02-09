## 퇴사
"""
// problem
N일 동안 상담을 하려 하는데, 하루에 하나씩 서로 다른 상담을 잡아놓았다.
각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.
상담을 적절히 했을 때, 얻을 수 있는 최대 수익을 구하라.
// input
첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며,
1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)
// output
첫째 줄에 얻을 수 있는 최대 이익을 출력한다.
"""
# study
n = int(input())  # 전체 상담 개수
t = []  # 각 상담을 완료하는데 걸리는 기간
p = []  # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1)  # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)
# O(n)
"""
// learn
my code와 달리 뒤쪽 날짜부터 거꾸로 확인하는 방식으로 접근한다.
dp[i]를 i번째 날부터 마지막 날까지 낼 수 있는 최대 이익으로 잡는다.
"""