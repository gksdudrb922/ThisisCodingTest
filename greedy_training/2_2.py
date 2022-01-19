## 곱하기 혹은 더하기
"""
// problem
각 자리가 숫자(0부터 9)로만 이루어진 문자열 S에 대해
왼쪽부터 오른쪽으로 '+' 혹은 '*' 연산자를 넣어 결과적으로 만들어질 수 있는
가장 큰 수를 구한다.
// input
첫째 줄 -> 여러 개의 숫자로 구성된 문자열 S (len(S) : 1 ~ 20)
// ouput
만들어질 수 있는 가장 큰 수
"""
# study
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
# O(n), n=len(data)
