## 럭키 스트레이트
"""
// problem
N의 자릿수를 반으로 나누어 양 쪽의 자릿수들의 합이 같다면 럭키 스트레이트를 사용할 수 있다.
// input
정수 N (10 ~ 99,9999,9999) 단, 자릿수는 항상 짝수
// output
럭키 스트레이트를 사용할 수 있다면 "LUCKY", 그렇지 않다면 "READY"
"""
# my code
data=list(input())
sum1=0
sum2=0
for i in range(len(data)//2):
  sum1+=int(data[i])
for i in range(len(data)//2,len(data)):
  sum2+=int(data[i])
result="LUCKY" if sum1==sum2 else "READY"
print(result)
# O(1)