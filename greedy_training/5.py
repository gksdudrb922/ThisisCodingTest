## 볼링공 고르기
"""
// problem
두 사람이 서로 무게가 다른 볼링공을 고르려고 한다.
// input
첫 째줄 -> 볼링공의 개수 N(1 ~ 1000), 공의 최대 무게 M(1 ~ 10)
둘 째줄 -> 각 볼링공의 무게 K (1 ~ M)
// output
두 사람이 볼링공을 고르는 경우의 수
"""
# my code
n,m=map(int,input().split())
data=list(map(int,input().split()))
result=0
for i in range(n-1):
  for j in range(i,n):
    if data[i] != data[j]:
      result+=1
print(result)
# O(n2)

n,m=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
count=1
result=0
for i in range(n-1):
  if data[i]!=data[i+1]:
    result+=count*(n-i-1)
    count=1
  else:
    count+=1
print(result)
#O(nlogn)