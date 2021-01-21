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
n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort(reverse=True)
for i in range(k):
  if a[i]<b[i]:
    a[i],b[i]=b[i],a[i]
  else:
    break
print(sum(a))
# O(nlogn)
"""
// learn
A의 가장 작은 원소가 B의 가장 큰 원소보다 작을 때만 swap을 실행해야 한다.
my code는 틀린 코드이다.
"""