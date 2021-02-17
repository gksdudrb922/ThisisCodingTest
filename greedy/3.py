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
# my code
n,k=map(int,input().split())
result=0
while n>1:
  if n%k==0:
    n//=k
  else:
    n-=1
  result+=1
print(result)
# O(n)

