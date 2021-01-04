## 큰 수의 법칙

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