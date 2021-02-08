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
# study
# 정수 N을 입력 받기
n = int(input())
# 모든 식량 정보 입력 받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

# 계산된 결과 출력
print(d[n - 1])
# O(n)
"""
// learn
my code에 비해 시간 복잡도가 낮다. 다이나믹 프로그래밍을 잘 사용한 코드이다.
my code : d[i]는 i번째 data를 포함해서 가장 큰 값
study : d[i]는 i번째 index 까지 고려했을 때 최댓값
"""