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
        while i<len(data)-1:
            if data[i] == data[i + 1]:
                same_count += 1
            else:
                if same_count > 0:
                    total_count += (length + len(str(same_count + 1)))
                    same_count = 0
                else:
                    total_count += length
            i += 1

        if same_count > 0:
            total_count += (length + len(str(same_count + 1)))
        else:
            total_count += length

        total_count += remainder
        if min_count > total_count:
            min_count = total_count
    return min_count
# O(n2), n=len(s)

# new
def solution(s):
    result = len(s)

    # 슬라이싱 단위
    for check in range(1, len(s) // 2 + 1):

        start = 0
        new_str = ""

        # s를 완전 탐색한다.
        while start + check <= len(s):

            count = 1
            target = s[start:start + check]
            start += check

            # s의 범위 이내에서 target과 같은 패턴이 나온다면 count 증가
            while start + check <= len(s) and target == s[start:start + check]:
                count += 1
                start += check

            # 다른 패턴이 나왔다면 그동안 count한 값과 target을 new_str에 저장
            if count == 1:
                new_str += target
            else:
                new_str += (str(count) + target)

        # 탐색을 마치고 남은 부분을 new_str에 붙여준다.
        # 이 때, 남은 부분이 없다면 아무값도 추가되지 않는다.
        new_str += s[start:len(s)]

        # 최소 길이
        result = min(result, len(new_str))

    return result
# O(n2), n=len(s)