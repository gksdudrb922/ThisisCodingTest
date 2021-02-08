## 효율적인 화폐 구성
"""
// problem
N가지 종류의 화폐가 있다. 이 화페들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 한다.
화폐는 몇 개라도 사용할 수 있다.
// input
N (1 ~ 100), M (1 ~ 10,000)
이후 N개의 줄에는 각 화폐의 가치가 주어진다. (<= 10,000)
// output
M원을 만들기 위한 최소한의 화폐 개수를 출력한다.
불가능할 때는 -1을 출력한다.
"""
# study, 풀지 못함
# 정수 N, M을 입력 받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
# O(nm)
"""
// learn
금액을 기준으로 DP를 수행한다.
"""