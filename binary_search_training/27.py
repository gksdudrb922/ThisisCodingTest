## 정렬된 배열에서 특정 수의 개수 구하기
"""
// problem
N개의 원소를 가진 오름차순 수열에서 x의 개수를 구하라. 단, O(logN)으로 구하라.
// input
첫째 줄 -> N(1 ~ 1,000,000), x(-10^9 ~ 10^9)
둘째 줄 -> 오름차순 수열(각 원소 값 : -10^9 ~ 10^9)
// output
수열의 원소 중에서 값이 x인 원소의 개수를 구하라. x인 원소가 하나도 없다면 -1 출력.
"""
# my code
from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


n, x = map(int, input().split())
data = list(map(int, input().split()))

result = count_by_range(data, x, x)
if result > 0:
    print(result)
else:
    print(-1)

# O(logn)
