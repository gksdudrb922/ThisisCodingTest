## 실패율
"""
// problem
실패율은 다음과 같이 정의한다.
- 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
// input
전체 스테이지의 개수 N(1 ~ 500)
게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages(길이 : 1 ~ 200,000)
stages는 1 ~ N+1의 자연수가 담겨있다. N+1은 모든 스테이지를 클리어한 유저이다.
// output
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.
만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
"""
# my code
def solution(N, stages):
  count = [0] * (N + 2)
  for i in range(len((stages))):
    count[stages[i]] += 1

  data = []
  for i in range(1, N + 1):
    summary = sum(count[i:])
    if summary > 0:
      fail = count[i] / summary
    else:
      fail = 0
    data.append((i, fail))

  data = sorted(data, key=lambda x: (-x[1], x[0]))

  answer = []
  for i in data:
    answer.append(i[0])
  return answer
# O(n2 or len(stages))