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
# study
n,m=map(int,input().split())
data=list(map(int,input().split()))
array=[0]*11
result=0
for x in data:
  array[x]+=1
for i in range(1,m+1):
  n-=array[i]
  result+=(array[i]*n)
print(result)
# O(n), m은 10 이하이기 때문에 무시 가능