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
result=0
if 1 not in data:
  result=1
elif n==1:
  result=n
else:
  data.sort()
  sum=data[0]
  for i in range(1,n):
    sum+=data[i]
    if i==n-1 or (data[i+1]-sum)>=2:
      result=sum+1
      break
print(result)
# O(nlogn)