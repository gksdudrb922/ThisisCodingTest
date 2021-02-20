## 럭키 스트레이트
"""
// problem
N의 자릿수를 반으로 나누어 양 쪽의 자릿수들의 합이 같다면 럭키 스트레이트를 사용할 수 있다.
// input
정수 N (10 ~ 99,9999,9999) 단, 자릿수는 항상 짝수
// output
럭키 스트레이트를 사용할 수 있다면 "LUCKY", 그렇지 않다면 "READY"
"""
# study
n = input()
length = len(n) # 점수 값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수의 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수의 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")
# O(1)
"""
// learn
my code와 풀이가 같다.
다만 여기서는 summary 변수 하나만 사용해서 왼쪽 부분과 오른쪽 부분의 합이 같은지 체크했다.
"""