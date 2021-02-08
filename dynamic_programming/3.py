## 바닥 공사
"""
// problem
가로 N, 세로 2인 직사각형을 1*2, 2*1, 2*2의 덮개로 채우고자 한다.
// input
정수 N (1 ~ 1,000)
// output
채우는 모든 경우의 수
"""
# my code
n=int(input())

d=[0]*1001
d[1]=1
d[2]=3

for i in range(3,n+1):
  d[i]=d[i-1]+d[i-2]*3-d[i-2]

print(d[n]%796796)
# O(n)