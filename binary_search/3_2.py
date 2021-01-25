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
# study
def count_by_value(data, x):
    n = len(data)
    a = first(data, x, 0, n - 1)
    if a == None:
        return 0
    b = last(data, x, 0, n - 1)
    return b - a + 1


def first(data, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if target == data[mid] and (mid == 0 or data[mid] > data[mid - 1]):
        return mid
    elif target > data[mid]:
        return first(data, target, mid + 1, end)
    else:
        return first(data, target, start, end - 1)


def last(data, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if target == data[mid] and (mid == n - 1 or data[mid] < data[mid + 1]):
        return mid
    elif target >= data[mid]:
        return last(data, target, mid + 1, end)
    else:
        return last(data, target, start, end - 1)


n, x = map(int, input().split())
data = list(map(int, input().split()))
count = count_by_value(data, x)
if count == 0:
    print(-1)
else:
    print(count)

# O(logn)
"""
// learn
이진 탐색을 이용하는 방법
"""
