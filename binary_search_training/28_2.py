## 고정점 찾기
"""
// problem
고정점이란, 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미한다.
서로 다른 N개 원소로 이루어진 수열이 오름차순으로 정렬되어 있을 때 고정점을 출력하라. 고정점은 최대 1개이다.
// input
첫째 줄 -> N(1 ~ 1,000,000)
둘째 줄 -> 오름차순 수열(각 원소 값 : -10^9 ~ 10^9)
// output
고정점을 출력한다.. 고정점인 원소가 하나도 없다면 -1 출력.
"""
# study
# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 고정점을 찾은 경우 인덱스 반환
    if array[mid] == mid:
        return mid
    # 중간점이 가리키는 값보다 중간점이 작은 경우 왼쪽 확인
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    # 중간점이 가리키는 값보다 중간점이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, mid + 1, end)

n = int(input())
array = list(map(int, input().split()))

# 이진 탐색(Binary Search) 수행
index = binary_search(array, 0, n - 1)

# 고정점이 없는 경우 -1 출력
if index == None:
    print(-1)
# 고정점이 있는 경우 해당 인덱스 출력
else:
    print(index)
# O(logn)
"""
// learn
my code와 동일하다.
"""
