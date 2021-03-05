## 부품 찾기
"""
// problem
N개의 부품에서 M개 종류의 부품이 있는지 확인한다.
// input
첫째 줄 -> 부품 개수 N(1 ~ 1,000,000)
둘째 줄 -> 부폼 번호 N개(각각 1 ~ 1,000,000)
셋째 줄 -> 정수 M(1 ~ 100,000)
넷째 줄 -> M개 정수(1 ~ 1,000,000)
// output
손님이 요청한 부품 번호의 순서대로 부품을 확인해 있으면 yes, 없으면 no를 출력한다.
"""
# my code
import sys
input=sys.stdin.readline
n=int(input())
data=list(map(int,input().split()))
data.sort()
m=int(input())
demand=list(map(int,input().split()))

def binary_search(target,start,end):
  if start>end:
    return None
  mid=(start+end)//2
  if data[mid]==target:
    return mid
  elif data[mid]>target:
    return binary_search(target,start,mid-1)
  else:
    return binary_search(target,mid+1,end)

for target in demand:
  if binary_search(target,0,len(data)-1)==None:
    print('no', end=' ')
  else:
    print('yes', end=' ')
# O((m+n)logn)
