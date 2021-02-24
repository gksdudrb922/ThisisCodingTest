## 위에서 아래로
"""
// problem
수열을 내림차순으로 정렬한다.
// input
첫째 줄 -> 수열에 속해 있는 수의 개수 N (1 ~ 500)
둘째 줄부터 N+1번째 줄까지 N개의 수가 입력된다. (1 ~ 100,000)
// output
수열을 내림차순으로 정렬
"""
# study

# N 입력 받기
n = int(input())

# N개의 정수를 입력 받아 리스트에 저장
array = []
for i in range(n):
  array.append(int(input()))

# 파이썬 정렬 라이브러리를 이용하여 내림차순 정렬 수행
array = sorted(array, reverse=True)

# 정렬이 수행된 결과를 출력
for i in array:
  print(i, end=' ')
# O(nlogn)
"""
// learn
my code와 동일하다.
"""