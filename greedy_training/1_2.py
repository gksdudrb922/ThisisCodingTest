## 모험가 길드
"""
// problem
N명의 모함가를 대상으로 '공포도'를 측정했다.
공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있다.
// input
첫째 줄 -> N : 모험가의 수 (1 ~ 100,000)
둘째 줄 -> 각 모험가의 공포도 값 (<= N)
// output
여행을 떠날 수 있는 그룹 수의 최댓값
"""
# study
n=int(input())
data=list(map(int,input().split()))
data.sort()
cnt=0
result=0
for i in data:
  cnt+=1
  if cnt>=i:
    result+=1
    cnt=0
print(result)
# O(nlogn)