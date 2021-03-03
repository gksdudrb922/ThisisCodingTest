## 카드 정렬하기
"""
// problem
N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 구하는 프로그램을 작성하시오.
(두 묶음(A,B)을 합쳐서 하나로 만드는 데에는 A+B의 연산이 필요하다.)
// input
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000) 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 각각의 크기가 주어진다.
숫자 카드 묶음의 크기는 1,000보다 작거나 같은 양의 정수이다.
// output
첫째 줄에 최소 비교 횟수를 출력한다.
"""
# my code
import heapq
n=int(input())
data=[]
for _ in range(n):
  heapq.heappush(data,int(input()))

result=0
while len(data)>1:
  first=heapq.heappop(data)
  second=heapq.heappop(data)
  summary=first+second
  result+=summary
  heapq.heappush(data,summary)
print(result)
#O(nlogn)