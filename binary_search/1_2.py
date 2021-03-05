## 부품 찾기
"""
// problem
N개의 부품에서 M개 종류의 부품이 있는지 확인한다.
// input
첫째 줄 -> 부품 개수 N(1 ~ 1,000,000)
둘째 줄 -> 부폼 번호 N개(각각 1 ~ 1,000,000)
셋째 줄 -> 정수 M(1 ~ 100,000)
넷째 줄 -> M개 정수(1 ~ 1,000,000)
// output
손님이 요청한 부품 번호의 순서대로 부품을 확인해 있으면 yes, 없으면 no를 출력한다.
"""
# study
#1. 이진 탐색

# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
      return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
      end = mid - 1
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
    else:
      start = mid + 1
  return None


# N(가게의 부품 개수) 입력
n = int(input())
# 가게에 있는 전체 부품 번호를 공백을 기준으로 구분하여 입력
array = list(map(int, input().split()))
array.sort()  # 이진 탐색을 수행하기 위해 사전에 정렬 수행
# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백을 기준으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
  # 해당 부품이 존재하는지 확인
  result = binary_search(array, i, 0, n - 1)
  if result != None:
    print('yes', end=' ')
  else:
    print('no', end=' ')
# O((n+m)logn)

#2. 계수 정렬
# N(가게의 부품 개수) 입력
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력 받아서 기록
for i in input().split():
    array[int(i)] = 1

# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백을 기준으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
#O(max(n,m))

#3. 집합

# N(가게의 부품 개수) 입력
n = int(input())
# 가게에 있는 전체 부품 번호를 입력 받아서 집합(Set) 자료형에 기록
array = set(map(int, input().split()))

# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백을 기준으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
  # 해당 부품이 존재하는지 확인
  if i in array:
    print('yes', end=' ')
  else:
    print('no', end=' ')
#O(m)

"""
// learn
3가지 풀이 방식이 있다.
#1. 이진 탐색 방법은 my code와 동일한 풀이다.
#2. 계수 정렬에서 사용하는 count 리스트를 이용했다. 이처럼 정수 리스트에서 정수를 찾을 때 사용하면 유용하다.
#3. 집합은 탐색이 O(1)이기 때문에 가장 빠른 코드를 만들 수 있다.
"""
