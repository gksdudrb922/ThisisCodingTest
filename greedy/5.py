## 모험가 길드

# my code
n=int(input())
data=list(map(int,input().split()))
data.sort()
cnt=1
result=0
for num in data:
  if num==cnt:
    result+=1
    cnt=1
  else:
    cnt+=1
print(result)
# O(nlogn)