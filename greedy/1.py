## 큰 수의 법칙
"""
// problem
N개의 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만들어야 한다.
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
// input
첫째 줄 -> N(2 ~ 1,000), M(1 ~ 10,000), K(1 ~ 10,000) (K <= M)
둘째 줄 -> N개의 자연수 (1 ~ 10,000)
// output
큰 수의 법첵이 따라 더해진 답
"""
# my code
n,m,k=map(int,input().split())
data=list(map(int,input().split()))
first=max(data)
data.remove(first)
second=max(data)
result=0
cnt=0
for _ in range(m):
  if cnt<k:
    result+=first
    cnt+=1
  else:
    result+=second
    cnt=0
print(result)
# O(min(N,M))