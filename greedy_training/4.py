## 만들 수 없는 금액
"""
// problem
N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구한다.
// input
첫째 줄 -> N : 동전의 개수 (1 ~ 1,000)
둘째 줄 -> 동전의 화페 단위, N 개의 자연수 (1,000,000 이하)
// output
주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값
"""
# my code
n=int(input())
data=list(map(int,input().split()))
data.sort()
sum=0
for i in range(n):
  if sum+1<data[i]:
    break
  sum+=data[i]
result=sum+1
print(result)
# O(nlogn)