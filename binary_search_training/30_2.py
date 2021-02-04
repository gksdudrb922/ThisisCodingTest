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
# study, 풀지 못함
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 모든 단어들을 길이마다 나누어서 저장하기 위한 리스트
array = [[] for _ in range(10001)]
# 모든 단어들을 길이마다 나누어서 뒤집어 저장하기 위한 리스트
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words: # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
        array[len(word)].append(word) # 단어를 삽입
        reversed_array[len(word)].append(word[::-1]) # 단어를 뒤집어서 삽입

    for i in range(10001): # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
        array[i].sort()
        reversed_array[i].sort()

    for q in queries: # 쿼리를 하나씩 확인하며 처리
        if q[0] != '?': # 접미사에 와일드 카드가 붙은 경우
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else: # 접두사에 와일드 카드가 붙은 경우
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        # 검색된 단어의 개수를 저장
        answer.append(res)
    return answer
# O(nlogn)
"""
// learn
bisect를 사용한다.
모든 단어를 길이마다 나누어서 저장한 뒤 각각 정렬한다는 것이 중요하다.
이후 와일드카드를 a, z로 바꾸어 그 사이값의 개수를 구한다.
"""
