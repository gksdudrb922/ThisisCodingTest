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
# study
def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
        # 남아있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer
# O(n2), n=len(s)
"""
// learn
my code와 동일한 풀이다. 
for문에서 3번 째 항으로 증감값을 설정할 수 있다는 것을 기억하자. while문에 비해 더 깔끔하다.
"""