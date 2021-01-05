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
# study
data=input()
count0=0
count1=0
if data[0]=='1':
  count0+=1
else:
  count1+=1
for i in range(len(data)-1):
  if data[i]!=data[i+1]:
    if data[i+1]=='1':
      count0+=1
    else:
      count1+=1
print(min(count0,count1))
# O(n)