## 연산자 끼워 넣기
"""
// problem
N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다.
또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다.
연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.
우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.
식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다.
또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다.
즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
// input
첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다.
둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100)
셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데,
차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다.
// output
첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다.
연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다.
또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.
"""
# my code
from itertools import product
n=int(input())
a=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())
op_product=list(product(['+','-','*','/'],repeat=(n-1)))

def calcurate(a,operands):
  result=a[0]
  for i in range(len(a)-1):
    if operands[i]=='+':
      result+=a[i+1]
    elif operands[i]=='-':
      result-=a[i+1]
    elif operands[i]=='*':
      result*=a[i+1]
    elif operands[i]=='/':
      if result<0:
        result*=-1
        result//=a[i+1]
        result*=-1
      else:
        result//=a[i+1]
  return result

result_min=1e9
result_max=-1e9
for operands in op_product:
  if operands.count('+')==add and operands.count('-')==sub and operands.count('*')==mul and operands.count('/')==div:
    result=calcurate(a,operands)
    result_min=min(result_min,result)
    result_max=max(result_max,result)
print(result_max)
print(result_min)
"""
// learn
permutations 대신 product를 사용하면 더 빠르다.
사칙연산 ['+','-','*','/']에 대해 n-1만큼 product를 수행한 후
각 순열에 대해 입력 받은 조건 add, sub, mul, div의 값과 일치할 때만 계산을 수행한다.

시간 비교 : permutations(10!) > product(4^10) -> product가 훨씬 빠르다
"""