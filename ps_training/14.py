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
# my code
from itertools import permutations


def solution(n, weak, dist):
    answer = 1e9
    dist_permutations = list(permutations(dist, len(dist)))
    goal_count = len(weak)
    for i in range(len(weak)):
        weak.append(weak[i] + n)

    for dist_permutation in dist_permutations:
        for start_index in range(0, len(weak)//2):
            start = weak[start_index]
            check_count = 0
            friend_count = 0
            for d in dist_permutation:
                friend_count += 1
                end = start + d
                for i in range(start_index, len(weak)):
                    if end >= weak[i]:
                        check_count += 1
                    else:
                        start_index = i
                        start = weak[start_index]
                        break

                if check_count >= goal_count:
                    answer = min(answer, friend_count)
                    break

    if answer == 1e9:
        return -1
    return answer


n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]
print(solution(n, weak, dist))
