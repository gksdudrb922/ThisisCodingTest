## 공유기 설치
"""
// problem
도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고,
집 여러개가 같은 좌표를 가지는 일은 없다.
도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다.
최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고,
가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
// input
첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다.
둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.
// output
첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.
"""
# study, 풀지 못함
# 집의 개수(N)와 공유기의 개수(C)를 입력 받기
n, c = list(map(int, input().split(' ')))

# 전체 집의 좌표 정보를 입력 받기
array = []
for _ in range(n):
     array.append(int(input()))
array.sort() # 이진 탐색 수행을 위해 정렬 수행

start = 1 # 가능한 최소 거리(min gap)
end = array[-1] - array[0] # 가능한 최대 거리(max gap)
result = 0

while(start <= end):
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
    # 첫째 집에는 무조건 공유기를 설치한다고 가정
    value = array[0]
    count = 1
    # 현재의 mid 값을 이용해 공유기를 설치하기
    for i in range(1, n): # 앞에서부터 차근차근 설치
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c: # C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가시키기
        start = mid + 1
        result = mid # 최적의 결과를 저장
    else: # C개 이상의 공유기를 설치할 수 없는 경우, 거리를 감소시키기
        end = mid - 1

print(result)
# O(nlogn)
"""
// learn
각 집의 좌표가 최대 10억이고, 거리의 최댓값을 구하는 문제기 때문에 이진 탐색을 통한 파라메트릭 서치 문제라고 생각할 수 있다.
1. 구하고자 하는 거리의 최댓값을 구하기 위해 거리 값이 될 수 있는 범위를 먼저 구한다.
2. 지정한 범위에 대해 최대, 최소 조건에 맞춰 이진 탐색을 수행한다.
3. input의 경우 sys를 사용해야 시간초과가 나지 않는다.
"""
