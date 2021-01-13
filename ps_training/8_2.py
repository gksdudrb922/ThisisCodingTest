## 문자열 재정렬
"""
// problem
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 있다.
모든 알파벳을 오름차순으로 정렬하여 출력한 뒤에, 모든 숫자를 더한 값을 이어서 출력한다.
// input
문자열 S (len(s) : 1 ~ 10,000)
// output
문제에서 요구하는 정답
"""
# study
data=input()
result=[]
value=0
for x in data:
  if x.isalpha():
    result.append(x)
  else:
    value+=int(x)
result.sort()
if value!=0:
  result.append(str(value))
print(''.join(result))
# O(nlogn), n = len(s)
"""
// learn
"""