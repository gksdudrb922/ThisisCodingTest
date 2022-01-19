## 숫자 카드 게임
"""
// problem
N*M 형태의 카드들이 있다. 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
1. 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
2. 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑는다.
3. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.
// input
첫째 줄 -> N, M(1 ~ 100)
둘째 줄부터 N개의 줄 -> 각 카드 행에 적힌 숫자 (1 ~ 10,000)
// output
게임의 룰에 맞게 선택한 카드에 적힌 숫자
"""
# my code
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    result = max(result, min(data))

print(result)
# O(nm)
