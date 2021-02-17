## 1이 될 때까지
"""
// problem
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택한다.
단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
1. N에서 1을 뺀다.
2. N을 K로 나눈다.
// input
첫째 줄 -> N(2 ~ 100,000), K(2 ~ 100,000) (N >= K)
// output
N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값
"""
# study
# N, K공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
#O(logn)
"""
// learn
N의 최댓값이 100,000이기에 my code, study 코드 모두 통과한다.
다만, study code는 N의 값이 매우 클 때 사용할 만한 코드이다.
N이 K로 나누어떨어지는 값(target)을 한 번에 구해서 계산하는 로직이다.
"""