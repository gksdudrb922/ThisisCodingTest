## 바닥 공사
"""
// problem
가로 N, 세로 2인 직사각형을 1*2, 2*1, 2*2의 덮개로 채우고자 한다.
// input
정수 N (1 ~ 1,000)
// output
채우는 모든 경우의 수
"""
# study
# 정수 N을 입력 받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1001

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

# 계산된 결과 출력
print(d[n])
# O(n)
"""
// learn
my code와 동일하다. 다만, my code는 중복 처리를 위해 d[i-2]를 따로 빼주었다면
study code는 애초에 중복을 고려하지 않고 계산했다.
"""