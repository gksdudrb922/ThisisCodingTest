## 외벽 점검
"""
// problem
레스토랑의 구조는 완전히 동그란 모양이고 외벽의 총 둘레는 n미터이며,
레스토랑의 정북 방향 지점을 0으로 나타내며,
취약 지점의 위치는 정북 방향 지점으로부터 시계 방향으로 떨어진 거리로 나타낸다.
또, 친구들은 출발 지점부터 시계, 혹은 반시계 방향으로 외벽을 따라서만 이동한한다
// input
외벽의 길이 n,
취약 지점의 위치가 담긴 배열 weak,
각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열 dist가 매개변수로 주어진다.
// output
취약 지점을 점검하기 위해 보내야 하는 친구 수의 최솟값을 출력한다.
"""
# study, 풀지 못함
from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약한 지점을 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count) # 최솟값 계산
    if answer > len(dist):
        return -1
    return answer
# O(??), 변수들의 값이나 길이가 작아 측정이 힘들다.
"""
// learn
my code와 거의 유사하다.
for x,y in data: 구문, 1e9와 같은 수 표현
"""