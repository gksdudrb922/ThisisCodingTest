## 고정점 찾기
"""
// problem
고정점이란, 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미한다.
서로 다른 N개 원소로 이루어진 수열이 오름차순으로 정렬되어 있을 때 고정점을 출력하라. 고정점은 최대 1개이다.
// input
첫째 줄 -> N(1 ~ 1,000,000)
둘째 줄 -> 오름차순 수열(각 원소 값 : -10^9 ~ 10^9)
// output
고정점을 출력한다.. 고정점인 원소가 하나도 없다면 -1 출력.
"""
# my code
def binary_search(array,start,end):
  if start>end:
    return None
  mid=(start+end)//2
  if array[mid]==mid:
    return mid
  elif array[mid]<mid:
    return binary_search(array,mid+1,end)
  else:
    return binary_search(array,start,mid-1)

n=int(input())
data=list(map(int,input().split()))
result=binary_search(data,0,n-1)
if result==None:
  print(-1)
else:
  print(result)
# O(logn)
