## 시각
"""
// problem
00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구한다.
// input
정수 N (0 ~ 23)
// output
00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수
"""
# study 풀지 못함
n=int(input())
result=0
for i in range(n+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i)+str(j)+str(k):
        result+=1
print(result)