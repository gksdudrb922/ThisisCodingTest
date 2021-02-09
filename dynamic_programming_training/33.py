## 퇴사
"""
// problem
N일 동안 상담을 하려 하는데, 하루에 하나씩 서로 다른 상담을 잡아놓았다.
각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.
상담을 적절히 했을 때, 얻을 수 있는 최대 수익을 구하라.
// input
첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며,
1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)
// output
첫째 줄에 얻을 수 있는 최대 이익을 출력한다.
"""
# my code
n=int(input())
data=[(0,0)]
for _ in range(n):
  t,p=map(int,input().split())
  data.append((t,p))
dp=[0]*(n+1)
for i in range(1,n+1):
  dp[i]=dp[i-1]
  for k in range(5):
    if i-k>0 and data[i-k][0]==k+1:
      dp[i]=max(dp[i],dp[i-k-1]+data[i-k][1])
print(dp[n])
# O(n)
