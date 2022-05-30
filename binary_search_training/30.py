## 가사 검색
"""
// problem
가사에 사용된 단어들 중에 특정 키워드가 몇 개 포함되어 있는지 구한다.
키워드는 와일드카드 문자중 하나인 '?'가 포함된 패턴 형태의 문자열을 뜻한다.
와일드카드 문자인 '?'는 글자 하나를 의미하며, 어떤 문자에도 매치된다고 가정한다.
// input
- 가사 단어 제한사항
words의 길이(가사 단어의 개수)는 2 이상 100,000 이하다.
각 가사 단어의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없다.
전체 가사 단어 길이의 합은 2 이상 1,000,000 이하다.
가사에 동일 단어가 여러 번 나올 경우 중복을 제거하고 words에는 하나로만 제공된다.
각 가사 단어는 오직 알파벳 소문자로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정한다.
- 검색 키워드 제한사항
queries의 길이(검색 키워드 개수)는 2 이상 100,000 이하다.
각 검색 키워드의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없다.
전체 검색 키워드 길이의 합은 2 이상 1,000,000 이하다.
검색 키워드는 중복될 수도 있다.
각 검색 키워드는 오직 알파벳 소문자와 와일드카드 문자인 '?' 로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정한다.
검색 키워드는 와일드카드 문자인 '?'가 하나 이상 포함돼 있으며, '?'는 각 검색 키워드의 접두사 아니면 접미사 중 하나로만 주어진다.
// output
각 키워드 별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환한다.
"""
# my code
from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


def solution(words, queries):
    words_by_count = [[] for _ in range(10001)]
    words_by_count_reverse = [[] for _ in range(10001)]
    for word in words:
        length = len(word)
        words_by_count[length].append(word)
        words_by_count_reverse[length].append(word[::-1])

    for i in range(1, len(words_by_count)):
        words_by_count[i].sort()
        words_by_count_reverse[i].sort()

    answer = []
    for query in queries:
        if query[0] != "?":
            answer.append(count_by_range(words_by_count[len(query)], query.replace("?", "a"), query.replace("?", "z")))
        else:
            query_reverse = query[::-1]
            answer.append(count_by_range(words_by_count_reverse[len(query)], query_reverse.replace("?", "a"), query_reverse.replace("?", "z")))

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))

# O(aloga or blogb), a=len(words), b=len(queries)
