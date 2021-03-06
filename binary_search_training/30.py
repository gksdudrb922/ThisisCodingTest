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


def logic(query, data):
  index = query.count('?')
  left_value = query[:len(query) - index] + ('a' * index)
  right_value = query[:len(query) - index] + ('z' * index)
  return count_by_range(data[len(query)], left_value, right_value)


def solution(words, queries):
  reverse_words = []
  for word in words:
    reverse_words.append(word[::-1])

  words.sort()
  reverse_words.sort()

  data = [[] for _ in range(10001)]
  reverse_data = [[] for _ in range(10001)]
  for i in range(len(words)):
    data[len(words[i])].append(words[i])
    reverse_data[len(reverse_words[i])].append(reverse_words[i])

  answer = []
  for query in queries:
    if query[0] != '?':
      answer.append(logic(query, data))
    else:
      answer.append(logic(query[::-1], reverse_data))
  return answer
# O(aloga or blogb), a=len(words), b=len(queries)
