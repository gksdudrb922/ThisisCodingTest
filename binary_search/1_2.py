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
n=int(input())
data=set(map(int,input().split()))
m=int(input())
target=list(map(int,input().split()))
for x in target:
  if x in data:
    print('yes',end=' ')
  else:
    print('no',end=' ')
# O(n)
"""
// learn
집합을 사용해 더욱 간결하게 코드를 작성한다.
파이썬의 in 을 적극 활용하자.
"""
