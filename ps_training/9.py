## 문자열 압축
"""
// problem
알파벳 소문자로만 이루어진 문자열 s를 압축한다. 문자열의 1개 이상의 단위로 자라서 압축하여 더 짧은 문자열로 표현한다.
예를 들어, ababcdcdababcdcd의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만,
2개 단위로 잘라서 압축한다면 2ab2cd2ab2cd로 표현할 수 있습니다.
다른 방법으로 8개 단위로 잘라서 압축한다면 2ababcdcd로 표현할 수 있으며,
이때가 가장 짧게 압축하여 표현할 수 있는 방법이다.
// input
문자열 S (len(s) : 1 ~ 1000)
// output
압축하여 표현한 문자열 중 가장 짧은 것의 길이
"""
# my code
def solution(s):
    min_count = len(s)
    for length in range(1, len(s) // 2 + 1):
        data = list(map(''.join, zip(*[iter(s)] * length)))
        remainder = len(s) % length
        i = 0
        same_count = 0
        total_count = 0
        while True:

            if i == len(data) - 1:
                if same_count > 0:
                    total_count += (length + len(str(same_count + 1)))
                else:
                    total_count += length
                break

            if data[i] == data[i + 1]:
                same_count += 1
            else:
                if same_count > 0:
                    total_count += (length + len(str(same_count + 1)))
                    same_count = 0
                else:
                    total_count += length
            i += 1

        total_count += remainder
        if min_count > total_count:
            min_count = total_count
    return min_count

s = "zxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
print(solution(s))
# O(n2), n=len(s)