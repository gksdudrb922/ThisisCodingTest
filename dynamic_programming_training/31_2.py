## 금광
"""
// problem
N*M 크기의 금광이 있다. 금광은 1*1 크기의 칸으로 나누어져 있다.
채굴자는 첫 번째 열, 어느 행에서 출발하여 금을 캐기 시작한다.
이후에 m번에 걸쳐 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동한다.
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 구한다.
// input
첫째 줄에 테스트 케이스 T (1 ~ 1000)
매 테스트 케이스 첫째 줄에 n, m (1 ~ 20)
둘째 줄에 n*m개의 위치에 매장된 금의 개수 (1 ~ 100)
// output
매 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력한다.
"""
# study, 풀지 못함
# 테스트 케이스(Test Case) 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)
# O(nm)
"""
// learn
dp테이블을 2차원으로 잡아 dp[i][j]를 해당 위치까지의 금의 최대 크기로 설정한다.
"""