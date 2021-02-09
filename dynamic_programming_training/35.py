## 못생긴 수
"""
// problem
못생긴 수란 오직 2,3,5만을 소인수로 가지는 수를 의미한다. 1은 못생긴 수라고 가정한다.
n번째 못생긴 수를 찾아라.
// input
n (1 ~ 1,000)
// output
n번째 못생긴 수를 출력한다.
"""
# my code
n=int(input())
dp=set()
dp.add(1)
num=2
count=1
result=0
while count<n:
  for k in [2,3,5]:
    if (num%k)==0 and (num//k) in dp:
      dp.add(num)
      count+=1
      break
  num+=1
print(num-1)
# O(num)