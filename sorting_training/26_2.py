## 실패율
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
# study, 풀지 못함
import heapq

n = int(input())

# 힙(Heap)에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

# 힙(Heap)에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)
# O(nlogn)
"""
// learn
greedy 아이디어를 생각해내지 못했음.
heapq를 사용해 보았다. 원소를 전부 넣었다 빼도 O(nlogn)이 소요된다.
"""