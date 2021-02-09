## 편집 거리
"""
// problem
두 개의 문자열 A와 B가 주어졌을 때, 문자열 A를 편집하여 문자열 Bㄹ 만들고자 한다.
문자열 A를 편집할 때는 다음의 세 연산 중에서 한 번에 하나씩 선택하여 이용할 수 있다.
1. 삽입 : 특정한 위치에 하나의 문자를 삽입한다.
2. 삭제 : 특정한 위치에 있는 하나의 문제를 삭제한다.
3. 교체 : 특정한 위치에 있는 하나의 문자를 다른 문자로 교체한다.
이때 편집 거리란 문자열 A를 편집하여 문자열 B로 만들기 위해 사용한 연산의 수를 의미한다.
문자열 A를 문자열 B로 만드는 최소 편집 거리를 계산하라.
// input
문자열 A, B
각 문자열은 영문 알파벳으로만 구성되어 있으며, 각 문자열의 길이는 1보다 크거나 같고, 5,000보다 작거나 같다.
// output
최소 편집 거리를 출력한다.
"""
# my code
a=input()
b=input()
m=len(a)
n=len(b)
dp=[[0]*(n+1) for _ in range(m+1)]
for i in range(1,m+1):
  dp[i][0]=i
for j in range(1,n+1):
  dp[0][j]=j

for j in range(1,n+1):
  for i in range(1,m+1):
    if a[i-1]==b[j-1]:
      dp[i][j]=dp[i-1][j-1]
    else:
      dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
print(dp[m][n])

# O(mn), m=len(a), n=len(b)