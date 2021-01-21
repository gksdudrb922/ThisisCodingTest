## 위에서 아래로
"""
// problem
수열을 내림차순으로 정렬한다.
// input
첫째 줄 -> 수열에 속해 있는 수의 개수 N (1 ~ 500)
둘째 줄부터 N+1번째 줄까지 N개의 수가 입력된다. (1 ~ 100,000)
// output
수열을 내림차순으로 정렬
"""
# my code
n=int(input())
data=[]
for _ in range(n):
  data.append(int(input()))
result=sorted(data,reverse=True)
for i in result:
  print(i,end=' ')
# O(nlogn)