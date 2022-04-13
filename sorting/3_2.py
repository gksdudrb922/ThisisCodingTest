## 두 배열의 원소 교체
"""
// problem
N개의 원소로 구성된 두 배열 A와 B이 있다. 서로 K번 원소를 바꿔치기 해 A의 모든 원소의 값이 최대가 되도록 하라.
// input
첫째 줄 -> N(1 ~ 100,000), K(0 ~ N)
둘째 줄 -> A의 원소들
셋째 줄 -> B의 원소들
// output
최대 K번 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값
"""
# study
n, k = map(int, input().split()) # N과 K를 입력 받기
a = list(map(int, input().split())) # 배열 A의 모든 원소를 입력받기
b = list(map(int, input().split())) # 배열 B의 모든 원소를 입력받기

a.sort() # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a)) # 배열 A의 모든 원소의 합을 출력
# O(nlogn)
"""
// learn
A의 가장 작은 원소가 B의 가장 큰 원소보다 작을 때만 swap을 실행해야 한다.
아니라면 반복문을 나가도 된다.
"""