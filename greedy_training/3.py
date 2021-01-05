## 문자열 뒤집기
"""
// problem
0과 1로만 이루어진 문자열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집어서
문자열에 있는 모든 숫자를 전부 같게 만든다.
// input
첫 째줄 -> 0과 1로만 이루어진 문자열 S (len(S) <=1000000)
// output
뒤집기 최소 횟수
"""
# my code
data=input()
original=int(data[0])
flag=0
result=0
for i in range(1,len(data)):
  if int(data[i]) != original:
    flag=1
  if flag==1 and (int(data[i])==original or i==len(data)-1):
    flag=0
    result+=1
if result==0:
  result=1
print(result)
# O(n)