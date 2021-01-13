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
# my code
s=input()
list=[]
sum=0
for c in s:
  if 'A'<=c<='Z':
    list.append(c)
  elif '0'<=c<='9':
    sum+=int(c)
result="".join(sorted(list))
if sum!=0:
  result+=str(sum)
print(result)
# O(nlogn), n = len(s)