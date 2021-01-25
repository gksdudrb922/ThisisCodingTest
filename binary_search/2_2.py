## 떡볶이 떡 만들기
"""
// problem
절단기에 높이를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고,
낮은 떡은 잘리지 않는다. 자르고 남은 떡은 손님이 가져간다.
// input
첫째 줄 -> 떡의 개수 N(1 ~ 1,000,000), 요청한 떡의 길이 M(1 ~ 2,000,000,000)
둘째 줄 -> 떡의 개별 높이 (<=1,000,000,000)
// output
적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값
"""
# study, 풀지 못함
n,m=map(int,input().split())
data=list(map(int,input().split()))
start=0
end=max(data)
result=0
while start<=end:
  mid=(start+end)//2
  s=0
  for x in data:
    if x>mid:
      s+=(x-mid)
  if s>m:
    result=mid
    start=mid+1
  else:
    end=mid-1
# O(klogk * n), k=len(max(data))
"""
// learn
이진 탐색을 문제에 적용하는 데 아직 어려움이 있다.
"""
