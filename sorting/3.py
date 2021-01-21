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
# my code
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
for i in range(k):
  a[i],b[n-1-i]=b[n-1-i],a[i]
print(sum(a))
# O(nlogn)