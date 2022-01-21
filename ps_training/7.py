## 럭키 스트레이트
"""
// problem
N의 자릿수를 반으로 나누어 양 쪽의 자릿수들의 합이 같다면 럭키 스트레이트를 사용할 수 있다.
// input
정수 N (10 ~ 99,9999,9999) 단, 자릿수는 항상 짝수
// output
럭키 스트레이트를 사용할 수 있다면 "LUCKY", 그렇지 않다면 "READY"
"""
# my code
n = input()

length = len(n)
first = n[:length//2]
second = n[length//2:]

first_sum = 0
for x in first:
    first_sum += ord(x) - ord('0')

second_sum = 0
for x in second:
    second_sum += ord(x) - ord('0')

if first_sum == second_sum:
    print('LUCKY')
else:
    print('READY')
# O(1)