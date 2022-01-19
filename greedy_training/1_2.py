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
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력
# O(nlogn)
